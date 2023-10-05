from .Node import Node
from .Version import Version
from random import randint
import os

PAGE_DIR = os.path.dirname(os.path.realpath(__file__))

def generate_colors(n: int, mix=[255, 255, 255]) -> list[str]:
    out = []
    for _ in range(n):
        R = (randint(0, 255) + mix[0]) // 2
        G = (randint(0, 255) + mix[0]) // 2
        B = (randint(0, 255) + mix[0]) // 2
        out.append("#" + format(R, "X") + format(G, "X") + format(B, "X"))
    return out


class HTMLGenerator:
    def __init__(self, version_list) -> None:
        self.__load_pattern()
        self._version_list = version_list

    def __load_pattern(self) -> None:
        with open(os.path.join(PAGE_DIR,"page.html"), "r") as page:
            self.page = page.read()

    def generate_html(self, L: list[Version]) -> str:
        self.__colors = generate_colors(len(L))
        self.__make_header(L)
        self.__make_versions(L)
        self.__make_struct(L)
        self.__make_main_versions()
        return self.page

    def __make_header(self, l: list[Version]) -> None:
        headers = ""
        for i in range(len(l)):
            headers += (
                f'<td style="background-color: {self.__colors[i]}">Format {i}</td>'
            )
        self.page = self.page.replace("${Indexes}", headers)

    def __make_versions(self, l: list[Version]):
        output_ranges = ""
        chrono = {}
        for i in range(len(l)):
            version = l[i]
            output_ranges += "<td>"
            for r in version.get_range_versions():
                output_ranges += f"{self._version_list['versions'][r['start']]['id']} - {self._version_list['versions'][r['end']]['id']}  "
                chrono[r["start"]] = {"format": i, "weight": abs(r["start"] - r["end"])}
            output_ranges += "</td>"
        self.page = self.page.replace("${Versions}", output_ranges)

        output_chrono = ""
        keys = list(chrono.keys())
        keys.sort()
        keys.reverse()
        for ch in keys:
            output_chrono += f'<div style="flex:{chrono[ch]["weight"]}; background-color: {self.__colors[chrono[ch]["format"]]};">F {chrono[ch]["format"]}</div>'
        self.page = self.page.replace("${formats}", output_chrono)

    def __make_struct(self, l: list[Version]) -> None:
        codes = ""

        last_v = None
        for i in range(len(l)):
            next_v = l[i + 1].root if i + 1 < len(l) else None
            codes += f"<td><pre>{l[i].root.print_dif(last_v, next_v, True)}</pre></td>"
            last_v = l[i].root
        self.page = self.page.replace("${struct}", codes)

    def __make_main_versions(self):
        html_out = ""

        # Get alpha
        in_set = False
        alpha = {"start": 0, "end": 0}
        for i in range(len(self._version_list["versions"]) - 1, -1, -1):
            v = self._version_list["versions"][i]
            if (v["type"] == "old_alpha") and not in_set:
                alpha["start"] = i
                in_set = True
            if (v["type"] != "old_alpha") and in_set:
                alpha["end"] = i
                break
        html_out += (
            f'<div style="flex:{abs(alpha["end"]-alpha["start"])}">Old Alpha</div>'
        )

        # Get beta
        in_set = False
        beta = {"start": 0, "end": 0}
        for i in range(len(self._version_list["versions"]) - 1, -1, -1):
            v = self._version_list["versions"][i]
            if (v["type"] == "old_beta") and not in_set:
                beta["start"] = i
                in_set = True
            if (v["type"] != "old_beta") and in_set:
                beta["end"] = i
                break
        html_out += f'<div style="flex:{abs(beta["end"]-beta["start"])}">Old Beta</div>'

        # Get main versions
        ranges = {}
        first = True
        current_range = {"start": 0, "end": 0}
        first_latest_snapshot = 0
        latest_release = ""
        for i in range(len(self._version_list["versions"]) - 1, -1, -1):
            v = self._version_list["versions"][i]
            if first and v["type"] == "release":
                current_range["start"] = i
                latest_release = v["id"]
                first_latest_snapshot = i + 1
                first = False

            if (
                (not first)
                and (self._version_list["versions"][i - 1]["type"] == "release")
                and (v["type"] == "snapshot")
            ):
                first_latest_snapshot = i

            if (
                (not first)
                and (v["type"] == "release")
                and (
                    ".".join(latest_release.split(".")[:2])
                    != ".".join(v["id"].split(".")[:2])
                )
            ):
                # Save last
                current_range["end"] = first_latest_snapshot - 1
                ranges[".".join(latest_release.split(".")[:2])] = current_range.copy()
                current_range["start"] = first_latest_snapshot
                latest_release = ".".join(v["id"].split(".")[:2])
                first_latest_snapshot = i + 1
        current_range["end"] = 0
        ranges[".".join(latest_release.split(".")[:2])] = current_range.copy()
    
        for major_v in ranges:
            r = ranges[major_v]
            html_out += f'<div style="flex:{abs(r["end"]-r["start"])}">{major_v}</div>'
        self.page = self.page.replace("${versions}", html_out)
