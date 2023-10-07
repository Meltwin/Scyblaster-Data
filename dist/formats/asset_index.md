# JSON Structures of the Launcher API

There are several files used by the Minecraft launcher to get all the necessary datas ready for the minecraft client. 
We will describe here the different JSON files and their structures.

## Asset Index

The asset index is the file that link the resource name to its download endpoint and hash name. This structure has not changed much from the first version, except for two field that have disappeared.

!!! info

    You can find the raw JSON structure extraction result <a href="../raw/assets/assets.html" target="_blank">on this page</a>.
    It show every asset index, when it appear/disappear, and what are the changes between the indexes.

{!formats/raw/assets/snippet.md!}