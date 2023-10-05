import requests
import os
import time
from .scyblaster.Node import NodeObj
from .scyblaster.Version import Version
from .scyblaster.HTML import HTMLGenerator

VERSION_LIST_ENDPOINT = (
        "https://piston-meta.mojang.com/mc/game/version_manifest_v2.json"
    )
OUTPUT_FOLDER = os.path.join("docs", "formats", "raw")
VERSION_RAW_FOLDER = os.path.join(OUTPUT_FOLDER, "versions")
ASSETS_RAW_FOLDER = os.path.join(OUTPUT_FOLDER, "assets")
MAX_ITER = 10000
LINE_WIDTH = 120

def get_json_structures():
    # Make the raw folder
    if not os.path.exists(VERSION_RAW_FOLDER) or not os.path.exists(ASSETS_RAW_FOLDER):
        os.mkdir(VERSION_RAW_FOLDER)
        os.mkdir(ASSETS_RAW_FOLDER)

    version_list = requests.get(VERSION_LIST_ENDPOINT).json()
    FOUND_VERSION_FORMAT = []

    n_versions = len(version_list['versions'])
    estimated_time = 0

    # Iterate over each version
    tstart = time.time()
    for v_idx in range(min(MAX_ITER, n_versions - 1), -1, -1):
        print(f"{n_versions-v_idx-1:3d}/{n_versions} Processing version {version_list['versions'][v_idx]['id']}".ljust(LINE_WIDTH, " ")+f"(est. {estimated_time:.0f} s)", end="\r")
        version_descriptor = requests.get(version_list["versions"][v_idx]["url"]).json()
        root_node = NodeObj(version_descriptor, 0)

        # Update version formats with the new version
        for made_version in FOUND_VERSION_FORMAT:
            assert type(made_version) is Version
            if made_version.root == root_node:
                made_version.versions.append(v_idx)
                break
        else:
            print("\n\t-> Made new version !")
            new_version = Version()
            new_version.root = root_node
            new_version.versions.append(v_idx)
            FOUND_VERSION_FORMAT.append(new_version)

        # Update estimated time
        estimated_time = v_idx*(time.time()-tstart)/(n_versions-v_idx)

    ###############################################################################################
    #       PART II: Computation Results
    ###############################################################################################
    # Raw JSON Structs
    print(f"Found {len(FOUND_VERSION_FORMAT)} different formats !")
    for i in range(len(FOUND_VERSION_FORMAT)):
        with open(os.path.join(VERSION_RAW_FOLDER, f"version_{i}.json"), "w+") as format_file:
            format_file.write(str(FOUND_VERSION_FORMAT[i].root))

    # Full extraction results
    with open(os.path.join(VERSION_RAW_FOLDER, "version.html"), "w+") as html_output:
        html_generator = HTMLGenerator(version_list)
        html_output.write(html_generator.generate_html(FOUND_VERSION_FORMAT))

    # Markdown snippet for integrating in docs
    with open(os.path.join(VERSION_RAW_FOLDER, "snippet.md"), 'w+') as snippet_file:
        snippet_file.write(f"There is actually **{len(FOUND_VERSION_FORMAT)}** different JSON structures for the version descriptor.\n")
        for i in range(len(FOUND_VERSION_FORMAT)):
            snippet_file.write(f"=== \"F{i+1}\"\n\tFor versions:\n\n") 
            for r in FOUND_VERSION_FORMAT[i].get_range_versions():
                snippet_file.write(f"\t - {version_list['versions'][r['start']]['id']} - {version_list['versions'][r['end']]['id']}\n")
            snippet_file.write("\n\t``` json\n"+FOUND_VERSION_FORMAT[i].root.print_dif(line_begin='\t')+"\n\t```\n\n")

if __name__ == "__main__":
    get_json_structures()