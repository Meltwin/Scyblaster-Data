from .Node import NodeObj


class Version:
    def __init__(self) -> None:
        self.root = NodeObj({}, 0)
        self.versions = []

    def get_range_versions(self) -> list[dict]:
        ranges = []

        last_val = self.versions[0]
        _range = {"start": last_val, "end": 0}
        for v in self.versions[1:]:
            if (v - last_val) != -1:
                _range["end"] = last_val
                ranges.append(_range.copy())
                _range["start"] = v
            last_val = v
        _range["end"] = self.versions[-1]
        ranges.append(_range.copy())
        return ranges
