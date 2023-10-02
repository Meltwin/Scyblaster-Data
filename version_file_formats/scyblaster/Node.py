from typing import Any, Tuple
from abc import ABC, abstractmethod

Primitives = [int, float, bool, str]
STEP = " ┊ "


class Node(ABC):
    def __init__(self, depth: int) -> None:
        self.child = None
        self.depth = depth

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
    def print_dif(self, previous=None, after=None, show_diff=False) -> str:
        pass


class NodeObj(Node):
    """
    Node representing a json object. \n
    Childs are marked by a str key and can have multiple values.
    """

    def __init__(self, json: dict, depth: int) -> None:
        super().__init__(depth)
        self.child = {}
        self.update(json)

    def update(self, json: dict[str, Any]) -> None:
        for name, elem in json.items():
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
                    self.child[name].append(NodeObj(elem, self.depth + 1))

            # If list, merge it with the NodeArray elem inside
            if type(elem) is list:
                for child_elem in self.child[name]:
                    if type(child_elem) is NodeArray:
                        child_elem.update(elem)
                        break
                else:
                    self.child[name].append(NodeArray(elem, self.depth + 1))

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

    def print_dif(self, previous=None, after=None, show_diff=False) -> str:
        prefix = STEP * (self.depth + 1)
        out = "{\n"

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
                    out += f"{prefix}{name}: "

                if type(sub_child) in [NodeObj, NodeArray]:
                    out += (
                        sub_child.print_dif(new_previous, new_after, show_diff)
                        + suffix_html
                    )
                else:
                    out += f"{type(sub_child).__name__}{suffix_html}\n"
                first = False
        out += STEP * (self.depth) + "}\n"
        return out


class NodeArray(Node):
    def __init__(self, json: list, depth: int) -> None:
        super().__init__(depth)
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
                    self.child.append(NodeObj(elem, self.depth + 1))

            # If list, merge it with the NodeArray elem inside
            if type(elem) is list:
                for child_elem in self.child:
                    if type(child_elem) is NodeArray:
                        child_elem.update(elem)
                        break
                else:
                    self.child.append(NodeArray(elem, self.depth + 1))

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

    def print_dif(self, previous=None, after=None, show_diff=False) -> str:
        prefix = STEP * (self.depth + 1)

        out = "[\n"
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
                out += f"{prefix_html}{prefix}{elem.print_dif(new_previous, new_after, show_diff)}{suffix_html}"
            else:
                out += f"{prefix_html}{prefix}{type(elem).__name__}{suffix_html}\n"
        out += STEP * (self.depth) + "]\n"

        return out
