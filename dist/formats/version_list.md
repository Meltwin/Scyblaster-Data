# JSON Structures of the Launcher API

There are several files used by the Minecraft launcher to get all the necessary datas ready for the minecraft client. 
We will describe here the different JSON files and their structures.

## Version list 

The first file used to check for new versions or for the version description is the version list. 
This list can be found on the Piston-Meta API at the address:

```Text
https://piston-meta.mojang.com/mc/game/version_manifest_v2.json
```

The structure of this file is:

```json
{
    "latest": {
        "release":  str, // version name
        "snapshot": str // version name
    },
    "versions": [
        {
            "id": str, // version name
            "type": str, // version type (release, snapshot ...)
            "url": str, // version descriptor url
            "time": str,
            "releaseTime": str, // version release date - time
            "sha1": str, // SHA1 hash of the version descriptor
            "complianceLevel": int
        }
        ...
    ]
}
```

!!! info "Order of the versions"
    The versions order in the `"versions"` tag goes from the newest to the oldest. Thus 0 being the latest version released by Minecraft and the last one being the first ever version released.

To get a description of the assets, libraries and other settings to check for this Minecraft version, you ought to download the file in the `"url"` field, and check its hash with the SHA-1 algorithm (and compare it with the `"sha1"` field) and finally parse it to get all the data you need.


### Version Name

This tag correspond to the public version name. There are several formats, but three main for the recent version:

- ^^*Release*^^: the release have a version name like `1.xx.yy` (e.g. 1.20.2, 1.8.1, ...),  
where xx is the major version number (big update) and yy the minor version (small changes, bug correction, ...).
- ^^*Snapshot*^^: for the snapshots, the name has the format `XXwYYc` (e.g. 23w40a, 22w09a, ...)
    - `XX` is the year of release of the snapshot,
    - `YY` is the week of release of the snapshot,
    - `c` is the order of releasing during this week (somtimes multiple snapshot are released the same week).
- ^^*Pre-Release / Release Candidate*^^: these types of version are basically pre-release to test everything and find the last urgent bugs to fix. The pre-release are the 
one  published first, then the release candidates.
They have the same base name as the release, but with a suffix:
    - `1.xx.yy-rck`, with k being the number of the release candidate for this version,
    - `1.xx.yy-prek`, with k being the number of the pre-release for this version.
- ^^*Beta version*^^: these are the old versions of Minecraft (before the 1.0.0 release). Their name are like `b1.x_yy`, with x as the major beta version and yy the minor beta version.
- ^^*Alpha version*^^: these are the oldest versions of Minecraft (before the beta release). There are several name formats, we list them from the newest to the oldest:
    - `a1.x.yy`: with `x` the major version and `yy` the minor version,
    - `inf-yyyymmdd` (used only one time): with `yyyy` the year, `mm` the month and `dd` the day of the release,
    - `c0.xx.yyc` / `c0.xx_yyc`: with `xx` the major version, `yy` the minor version and `c` the subversion order (a,b,c, ...),
    - `rd-xxxxxx`: the number following the prefix seems to be the day number, the hour and minutes of the release.
  
### Version type

This tag indicates what type of version it is. We give below a table of conversion between the differents types and the versions names:

| Versions                        | Version type tag equivalent |
| ------------------------------- | :-------------------------: |
| Release `1.xx.yy`               |          `release`          |
| Snapshot `XXwYYc`               |         `snapshot`          |
| Release Candidate `1.xx.yy-rck` |         `snapshot`          |
| Pre-Release `1.xx.yy-prek`      |         `snapshot`          |
| Beta-Release `b1.x_yy`          |         `old_beta`          |
| Alpha-Release `a1.x.yy`         |         `old_alpha`         |
| Alpha-Release `inf-yyyymmdd`    |         `old_alpha`         |
| Alpha-Release `c0.xx.yyc`       |         `old_alpha`         |
| Alpha-Release `rd-xxxxxx`       |         `old_alpha`         |
