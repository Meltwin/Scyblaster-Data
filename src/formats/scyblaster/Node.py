from typing import Any, Tuple
from abc import ABC, abstractmethod
from copy import deepcopy

Primitives = [int, float, bool, str]
STEP = "\t"


class Node(ABC):
    def __init__(self, depth: int, colapse_at: int) -> None:
        self.child = None
        self.depth = depth
        self.colapse_at = colapse_at
        self.n_groups = 0

    @abstractmethod
    def update(self, json: dict | str | float) -> None:
        pass

    @abstractmethod
    def __eq__(self, __value: Any) -> bool:
        pass

    def __str__(self) -> str:
        return self.print_dif()

    @abstractmethod
    def __contains__(self, item) -> bool:
        pass

    @abstractmethod
    def print_dif(self, previous=None, after=None, show_diff=False, line_begin: str = "") -> str:
        pass


class NodeObj(Node):
    """
    Node representing a json object. \n
    Childs are marked by a str key and can have multiple values.
    """

    def __init__(self, json: dict, depth=0, colapse_at=4) -> None:
        super().__init__(depth, colapse_at)
        self.child = {}
        self.update(json)

    def get_group_str(self, l: list[str]) -> str:
        for n in l:
            if "str_" in n:
                return n
        self.n_groups += 1
        return f"str_{self.n_groups}"
    
    def has_group_str(self, l: list[str]) -> bool:
        for n in l:
            if "str_" in n:
                return True
        return False

    def update(self, json: dict[str, Any]) -> None:
        for name, elem in json.items():
            names_found = []

            # Detecting if the object is already created with another tag, hence don't make it two times
            if type(elem) is dict:
                obj = NodeObj(elem,colapse_at=self.colapse_at)
            elif type(elem) is list:
                obj = NodeArray(elem,colapse_at=self.colapse_at)
            else:
                obj = elem

            # Check if there are cloned structures in childs
            for child_name in self.child.keys():
                if len(self.child[child_name]):
                    if (type(self.child[child_name][0]) is type(obj)) and (self.child[child_name][0] == obj):
                        names_found.append(deepcopy(child_name))
            
            # If too much clones, just group them
            if (len(names_found) >= self.colapse_at or self.has_group_str(names_found)):
                group = self.get_group_str(names_found)
                if group not in names_found:
                    self.child[group] = [self.child[names_found[0]][0]]
                for n in names_found:
                    if n != group:
                        self.child.pop(n)

            # Else add it normaly 
            else:
                # Look if key exist or not
                # Create array at this key if not
                if name not in self.child.keys():
                    self.child[name] = []

                # If primitive, put it in the array
                if type(elem) in Primitives:
                    for child_elem in self.child[name]:
                        if type(child_elem) is type(elem):
                            break
                    else:
                        self.child[name].append(elem)

                # If obj, merge it with the NodeObj elem inside
                if type(elem) is dict:
                    for child_elem in self.child[name]:
                        if type(child_elem) is NodeObj:
                            child_elem.update(elem)
                            break
                    else:
                        self.child[name].append(NodeObj(elem, self.depth + 1, self.colapse_at))

                # If list, merge it with the NodeArray elem inside
                if type(elem) is list:
                    for child_elem in self.child[name]:
                        if type(child_elem) is NodeArray:
                            child_elem.update(elem)
                            break
                    else:
                        self.child[name].append(NodeArray(elem, self.depth + 1, self.colapse_at))

    def __eq__(self, __value: Node) -> bool:
        if type(__value) is not NodeObj:
            return False

        # Test the number of childs
        if self.child.keys() != __value.child.keys():
            return False

        for name in self.child.keys():
            for dist_elem in __value.child[name]:
                for self_elem in self.child[name]:
                    if (type(self_elem) is type(dist_elem)) and (
                        (type(self_elem) in Primitives)
                        or (
                            (type(self_elem) in [NodeArray, NodeObj])
                            and (self_elem == dist_elem)
                        )
                    ):
                        break
                else:
                    return False
        return True

    def __contains__(self, item: Tuple[str, Any]) -> bool:
        if item[0] not in self.child.keys():
            return False
        for elem in self.child[item[0]]:
            if type(elem) is type(item[1]):
                found = True
                break
        else:
            found = False
        return found

    def print_dif(self, previous=None, after=None, show_diff=False, line_begin: str = "") -> str:
        prefix = line_begin+STEP * (self.depth + 1)
        out = line_begin+"{\n"

        for name in self.child.keys():
            first = True
            for sub_child in self.child[name]:
                prefix_html = ""
                suffix_html = ""
                new_after = None
                new_previous = None

                # Check for existence in last, and if found, get it for descendent analysis
                if (previous != None) and (show_diff):
                    if (name, sub_child) not in previous:
                        prefix_html += '<span class="addition">'
                        suffix_html += "</span>"
                    else:
                        for v in previous.child[name]:
                            if type(v) is type(sub_child):
                                new_previous = v
                                break

                # Check for existence in next, and if found get it for descendent analysis
                if (after != None) and (show_diff):
                    if (name, sub_child) not in after:
                        prefix_html += '<span class="removal">'
                        suffix_html += "</span>"
                    else:
                        for v in after.child[name]:
                            if type(v) is type(sub_child):
                                new_after = v
                                break

                out += prefix_html
                if not first:
                    out += prefix
                else:
                    out += f"{prefix}\"{name}\": "

                if type(sub_child) in [NodeObj, NodeArray]:
                    out += (
                        sub_child.print_dif(new_previous, new_after, show_diff, line_begin)
                        + suffix_html
                    )
                else:
                    out += f"{type(sub_child).__name__},{suffix_html}\n"
                first = False
        out += line_begin+STEP * (self.depth) + "},\n"
        return out


class NodeArray(Node):
    def __init__(self, json: list, depth=0, colapse_at=3) -> None:
        super().__init__(depth, colapse_at)
        self.child = []
        self.update(json)

    def update(self, json: list) -> None:
        for elem in json:
            # If primitive, put it in the array
            if type(elem) in Primitives:
                for child_elem in self.child:
                    if type(child_elem) is type(elem):
                        break
                else:
                    self.child.append(elem)

            # If obj, merge it with the NodeObj elem inside
            if type(elem) is dict:
                for child_elem in self.child:
                    if type(child_elem) is NodeObj:
                        child_elem.update(elem)
                        break
                else:
                    self.child.append(NodeObj(elem, self.depth + 1, self.colapse_at))

            # If list, merge it with the NodeArray elem inside
            if type(elem) is list:
                for child_elem in self.child:
                    if type(child_elem) is NodeArray:
                        child_elem.update(elem)
                        break
                else:
                    self.child.append(NodeArray(elem, self.depth + 1, self.colapse_at))

    def __eq__(self, __value: Any) -> bool:
        if type(__value) is not NodeArray:
            return False

        # Test the number of childs
        if len(self.child) != len(__value.child):
            return False

        # Test each element
        for dist_elem in __value.child:
            for self_elem in self.child:
                if (type(self_elem) is type(dist_elem)) and (
                    (type(self_elem) in Primitives)
                    or (
                        (type(self_elem) in [NodeArray, NodeObj])
                        and (self_elem == dist_elem)
                    )
                ):
                    break
            else:
                return False
        return True

    def __contains__(self, item: list[Any]) -> bool:
        for item_value in item:
            found = False
            for elem in self.child:
                if type(elem) is type(item_value):
                    found = True
                    break
            else:
                found = False

            if not found:
                break
        else:
            return True
        return False

    def print_dif(self, previous=None, after=None, show_diff=False, line_begin: str = "") -> str:
        prefix = line_begin+STEP * (self.depth + 1)

        out = line_begin+"[\n"
        for elem in self.child:
            prefix_html = ""
            suffix_html = ""
            new_after = None
            new_previous = None

            # Check for existence in last, and if found, get it for descendent analysis
            if (previous != None) and (show_diff):
                if [elem] not in previous:
                    prefix_html += '<span class="addition">'
                    suffix_html += "</span>"
                else:
                    for v in previous.child:
                        if type(v) is type(elem):
                            new_previous = v
                            break

            # Check for existence in next, and if found get it for descendent analysis
            if (after != None) and (show_diff):
                if [elem] not in after:
                    prefix_html += '<span class="removal">'
                    suffix_html += "</span>"
                else:
                    for v in after.child:
                        if type(v) is type(elem):
                            new_after = v
                            break
            if type(elem) in [NodeObj, NodeArray]:
                out += f"{prefix_html}{prefix}{elem.print_dif(new_previous, new_after, show_diff, line_begin)}{suffix_html}"
            else:
                out += f"{prefix_html}{prefix}{type(elem).__name__},{suffix_html}\n"
        out += line_begin+ STEP * (self.depth) + "],\n"

        return out
