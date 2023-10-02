import requests
from scyblaster.Node import NodeObj
from scyblaster.Version import Version
from scyblaster.HTML import HTMLGenerator

VERSION_LIST_ENDPOINT = (
    "https://piston-meta.mojang.com/mc/game/version_manifest_v2.json"
)

version_list = requests.get(VERSION_LIST_ENDPOINT).json()
FOUND_VERSION_FORMAT = []

MAX_ITER = 10000
DEBUG = False

if not DEBUG:
    # Iterate over each version
    for v_idx in range(min(MAX_ITER, len(version_list["versions"]) - 1), -1, -1):
        print(f"Processing version {version_list['versions'][v_idx]['id']}")
        version_descriptor = requests.get(version_list["versions"][v_idx]["url"]).json()
        rootNode = NodeObj(version_descriptor, 0)

        for madeVersion in FOUND_VERSION_FORMAT:
            assert type(madeVersion) is Version
            if madeVersion.root == rootNode:
                madeVersion.versions.append(v_idx)
                break
        else:
            print("Made new version !")
            new_version = Version()
            new_version.root = rootNode
            new_version.versions.append(v_idx)
            FOUND_VERSION_FORMAT.append(new_version)

# Computation results
print(f"Found {len(FOUND_VERSION_FORMAT)} different formats !")
for i in range(len(FOUND_VERSION_FORMAT)):
    with open(f"formats/format_{i}.txt", "w+") as format_file:
        format_file.write(str(FOUND_VERSION_FORMAT[i].root))

with open("formats/format.html", "w+") as html_output:
    html_generator = HTMLGenerator(version_list)
    html_output.write(html_generator.generate_html(FOUND_VERSION_FORMAT))
