There is actually **18** different JSON structures for the version descriptor.
=== "F1"
	For versions:

	 - rd-132211 - 1.2.4

	``` json
	{
		"assetIndex": 	{
			"id": str,
			"sha1": str,
			"size": int,
			"totalSize": int,
			"url": str,
		},
		"assets": str,
		"complianceLevel": int,
		"downloads": 	{
			"client": 	{
				"sha1": str,
				"size": int,
				"url": str,
			},
		},
		"id": str,
		"javaVersion": 	{
			"component": str,
			"majorVersion": int,
		},
		"libraries": 	[
				{
				"downloads": 	{
					"artifact": 	{
						"path": str,
						"sha1": str,
						"size": int,
						"url": str,
					},
					"classifiers": 	{
						"natives-linux": 	{
							"path": str,
							"sha1": str,
							"size": int,
							"url": str,
						},
						"natives-osx": 	{
							"path": str,
							"sha1": str,
							"size": int,
							"url": str,
						},
						"natives-windows": 	{
							"path": str,
							"sha1": str,
							"size": int,
							"url": str,
						},
					},
				},
				"name": str,
				"rules": 	[
						{
						"action": str,
						"os": 	{
							"name": str,
							"version": str,
						},
					},
				],
				"extract": 	{
					"exclude": 	[
						str,
					],
				},
				"natives": 	{
					"linux": str,
					"osx": str,
					"windows": str,
				},
			},
		],
		"mainClass": str,
		"minecraftArguments": str,
		"minimumLauncherVersion": int,
		"releaseTime": str,
		"time": str,
		"type": str,
	},

	```

=== "F2"
	For versions:

	 - 1.2.5 - 13w16a
	 - 1.5.2 - 13w23b

	``` json
	{
		"assetIndex": 	{
			"id": str,
			"sha1": str,
			"size": int,
			"totalSize": int,
			"url": str,
		},
		"assets": str,
		"complianceLevel": int,
		"downloads": 	{
			"client": 	{
				"sha1": str,
				"size": int,
				"url": str,
			},
			"server": 	{
				"sha1": str,
				"size": int,
				"url": str,
			},
			"windows_server": 	{
				"sha1": str,
				"size": int,
				"url": str,
			},
		},
		"id": str,
		"javaVersion": 	{
			"component": str,
			"majorVersion": int,
		},
		"libraries": 	[
				{
				"downloads": 	{
					"artifact": 	{
						"path": str,
						"sha1": str,
						"size": int,
						"url": str,
					},
					"classifiers": 	{
						"natives-linux": 	{
							"path": str,
							"sha1": str,
							"size": int,
							"url": str,
						},
						"natives-osx": 	{
							"path": str,
							"sha1": str,
							"size": int,
							"url": str,
						},
						"natives-windows": 	{
							"path": str,
							"sha1": str,
							"size": int,
							"url": str,
						},
					},
				},
				"name": str,
				"rules": 	[
						{
						"action": str,
						"os": 	{
							"name": str,
							"version": str,
						},
					},
				],
				"extract": 	{
					"exclude": 	[
						str,
					],
				},
				"natives": 	{
					"linux": str,
					"osx": str,
					"windows": str,
				},
			},
		],
		"mainClass": str,
		"minecraftArguments": str,
		"minimumLauncherVersion": int,
		"releaseTime": str,
		"time": str,
		"type": str,
	},

	```

=== "F3"
	For versions:

	 - 13w16b - 13w16b

	``` json
	{
		"assetIndex": 	{
			"id": str,
			"sha1": str,
			"size": int,
			"totalSize": int,
			"url": str,
		},
		"assets": str,
		"complianceLevel": int,
		"downloads": 	{
			"client": 	{
				"sha1": str,
				"size": int,
				"url": str,
			},
			"server": 	{
				"sha1": str,
				"size": int,
				"url": str,
			},
		},
		"id": str,
		"javaVersion": 	{
			"component": str,
			"majorVersion": int,
		},
		"libraries": 	[
				{
				"downloads": 	{
					"artifact": 	{
						"path": str,
						"sha1": str,
						"size": int,
						"url": str,
					},
					"classifiers": 	{
						"natives-linux": 	{
							"path": str,
							"sha1": str,
							"size": int,
							"url": str,
						},
						"natives-osx": 	{
							"path": str,
							"sha1": str,
							"size": int,
							"url": str,
						},
						"natives-windows": 	{
							"path": str,
							"sha1": str,
							"size": int,
							"url": str,
						},
					},
				},
				"name": str,
				"rules": 	[
						{
						"action": str,
						"os": 	{
							"name": str,
							"version": str,
						},
					},
				],
				"extract": 	{
					"exclude": 	[
						str,
					],
				},
				"natives": 	{
					"linux": str,
					"osx": str,
					"windows": str,
				},
			},
		],
		"mainClass": str,
		"minecraftArguments": str,
		"minimumLauncherVersion": int,
		"releaseTime": str,
		"time": str,
		"type": str,
	},

	```

=== "F4"
	For versions:

	 - 13w24a - 13w38c

	``` json
	{
		"assetIndex": 	{
			"id": str,
			"sha1": str,
			"size": int,
			"totalSize": int,
			"url": str,
		},
		"assets": str,
		"downloads": 	{
			"client": 	{
				"sha1": str,
				"size": int,
				"url": str,
			},
			"server": 	{
				"sha1": str,
				"size": int,
				"url": str,
			},
			"windows_server": 	{
				"sha1": str,
				"size": int,
				"url": str,
			},
		},
		"id": str,
		"libraries": 	[
				{
				"downloads": 	{
					"artifact": 	{
						"path": str,
						"sha1": str,
						"size": int,
						"url": str,
					},
					"classifiers": 	{
						"natives-linux": 	{
							"path": str,
							"sha1": str,
							"size": int,
							"url": str,
						},
						"natives-osx": 	{
							"path": str,
							"sha1": str,
							"size": int,
							"url": str,
						},
						"natives-windows": 	{
							"path": str,
							"sha1": str,
							"size": int,
							"url": str,
						},
					},
				},
				"name": str,
				"rules": 	[
						{
						"action": str,
						"os": 	{
							"name": str,
							"version": str,
						},
					},
				],
				"extract": 	{
					"exclude": 	[
						str,
					],
				},
				"natives": 	{
					"linux": str,
					"osx": str,
					"windows": str,
				},
			},
		],
		"mainClass": str,
		"minecraftArguments": str,
		"minimumLauncherVersion": int,
		"releaseTime": str,
		"time": str,
		"type": str,
	},

	```

=== "F5"
	For versions:

	 - 13w39a - 13w41b

	``` json
	{
		"assetIndex": 	{
			"id": str,
			"sha1": str,
			"size": int,
			"totalSize": int,
			"url": str,
		},
		"assets": str,
		"complianceLevel": int,
		"downloads": 	{
			"client": 	{
				"sha1": str,
				"size": int,
				"url": str,
			},
			"server": 	{
				"sha1": str,
				"size": int,
				"url": str,
			},
			"windows_server": 	{
				"sha1": str,
				"size": int,
				"url": str,
			},
		},
		"id": str,
		"javaVersion": 	{
			"component": str,
			"majorVersion": int,
		},
		"libraries": 	[
				{
				"downloads": 	{
					"artifact": 	{
						"path": str,
						"sha1": str,
						"size": int,
						"url": str,
					},
					"classifiers": 	{
						"natives-linux": 	{
							"path": str,
							"sha1": str,
							"size": int,
							"url": str,
						},
						"natives-osx": 	{
							"path": str,
							"sha1": str,
							"size": int,
							"url": str,
						},
						"natives-windows": 	{
							"path": str,
							"sha1": str,
							"size": int,
							"url": str,
						},
					},
				},
				"name": str,
				"rules": 	[
						{
						"action": str,
						"os": 	{
							"name": str,
							"version": str,
						},
					},
				],
				"extract": 	{
					"exclude": 	[
						str,
					],
				},
				"natives": 	{
					"linux": str,
					"osx": str,
					"windows": str,
				},
			},
		],
		"logging": 	{
			"client": 	{
				"argument": str,
				"file": 	{
					"id": str,
					"sha1": str,
					"size": int,
					"url": str,
				},
				"type": str,
			},
		},
		"mainClass": str,
		"minecraftArguments": str,
		"minimumLauncherVersion": int,
		"releaseTime": str,
		"time": str,
		"type": str,
	},

	```

=== "F6"
	For versions:

	 - 13w42a - 1.7.2
	 - 15w31a - 15w49a
	 - 15w49b - 16w04a

	``` json
	{
		"assetIndex": 	{
			"id": str,
			"sha1": str,
			"size": int,
			"totalSize": int,
			"url": str,
		},
		"assets": str,
		"complianceLevel": int,
		"downloads": 	{
			"client": 	{
				"sha1": str,
				"size": int,
				"url": str,
			},
			"server": 	{
				"sha1": str,
				"size": int,
				"url": str,
			},
			"windows_server": 	{
				"sha1": str,
				"size": int,
				"url": str,
			},
		},
		"id": str,
		"javaVersion": 	{
			"component": str,
			"majorVersion": int,
		},
		"libraries": 	[
				{
				"downloads": 	{
					"artifact": 	{
						"path": str,
						"sha1": str,
						"size": int,
						"url": str,
					},
					"classifiers": 	{
						"natives-linux": 	{
							"path": str,
							"sha1": str,
							"size": int,
							"url": str,
						},
						"natives-osx": 	{
							"path": str,
							"sha1": str,
							"size": int,
							"url": str,
						},
						"natives-windows": 	{
							"path": str,
							"sha1": str,
							"size": int,
							"url": str,
						},
					},
				},
				"name": str,
				"rules": 	[
						{
						"action": str,
						"os": 	{
							"name": str,
						},
					},
				],
				"extract": 	{
					"exclude": 	[
						str,
					],
				},
				"natives": 	{
					"linux": str,
					"windows": str,
					"osx": str,
				},
			},
		],
		"logging": 	{
			"client": 	{
				"argument": str,
				"file": 	{
					"id": str,
					"sha1": str,
					"size": int,
					"url": str,
				},
				"type": str,
			},
		},
		"mainClass": str,
		"minecraftArguments": str,
		"minimumLauncherVersion": int,
		"releaseTime": str,
		"time": str,
		"type": str,
	},

	```

=== "F7"
	For versions:

	 - 13w47a - 1.7.5
	 - 14w10a - 1.7.9
	 - 14w17a - 14w26c
	 - 14w28a - 1.8.8
	 - 1.8.9 - 1.8.9

	``` json
	{
		"assetIndex": 	{
			"id": str,
			"sha1": str,
			"size": int,
			"totalSize": int,
			"url": str,
		},
		"assets": str,
		"complianceLevel": int,
		"downloads": 	{
			"client": 	{
				"sha1": str,
				"size": int,
				"url": str,
			},
			"server": 	{
				"sha1": str,
				"size": int,
				"url": str,
			},
			"windows_server": 	{
				"sha1": str,
				"size": int,
				"url": str,
			},
		},
		"id": str,
		"javaVersion": 	{
			"component": str,
			"majorVersion": int,
		},
		"libraries": 	[
				{
				"downloads": 	{
					"artifact": 	{
						"path": str,
						"sha1": str,
						"size": int,
						"url": str,
					},
					"classifiers": 	{
						"natives-linux": 	{
							"path": str,
							"sha1": str,
							"size": int,
							"url": str,
						},
						"natives-osx": 	{
							"path": str,
							"sha1": str,
							"size": int,
							"url": str,
						},
						"natives-windows": 	{
							"path": str,
							"sha1": str,
							"size": int,
							"url": str,
						},
						"natives-windows-32": 	{
							"path": str,
							"sha1": str,
							"size": int,
							"url": str,
						},
						"natives-windows-64": 	{
							"path": str,
							"sha1": str,
							"size": int,
							"url": str,
						},
					},
				},
				"name": str,
				"extract": 	{
					"exclude": 	[
						str,
					],
				},
				"natives": 	{
					"linux": str,
					"osx": str,
					"windows": str,
				},
				"rules": 	[
						{
						"action": str,
						"os": 	{
							"name": str,
						},
					},
				],
			},
		],
		"logging": 	{
			"client": 	{
				"argument": str,
				"file": 	{
					"id": str,
					"sha1": str,
					"size": int,
					"url": str,
				},
				"type": str,
			},
		},
		"mainClass": str,
		"minecraftArguments": str,
		"minimumLauncherVersion": int,
		"releaseTime": str,
		"time": str,
		"type": str,
	},

	```

=== "F8"
	For versions:

	 - 14w08a - 14w08a
	 - 14w11b - 14w11b

	``` json
	{
		"assetIndex": 	{
			"id": str,
			"sha1": str,
			"size": int,
			"totalSize": int,
			"url": str,
		},
		"assets": str,
		"complianceLevel": int,
		"downloads": 	{
			"client": 	{
				"sha1": str,
				"size": int,
				"url": str,
			},
			"server": 	{
				"sha1": str,
				"size": int,
				"url": str,
			},
		},
		"id": str,
		"javaVersion": 	{
			"component": str,
			"majorVersion": int,
		},
		"libraries": 	[
				{
				"downloads": 	{
					"artifact": 	{
						"path": str,
						"sha1": str,
						"size": int,
						"url": str,
					},
					"classifiers": 	{
						"natives-linux": 	{
							"path": str,
							"sha1": str,
							"size": int,
							"url": str,
						},
						"natives-osx": 	{
							"path": str,
							"sha1": str,
							"size": int,
							"url": str,
						},
						"natives-windows": 	{
							"path": str,
							"sha1": str,
							"size": int,
							"url": str,
						},
						"natives-windows-32": 	{
							"path": str,
							"sha1": str,
							"size": int,
							"url": str,
						},
						"natives-windows-64": 	{
							"path": str,
							"sha1": str,
							"size": int,
							"url": str,
						},
					},
				},
				"name": str,
				"extract": 	{
					"exclude": 	[
						str,
					],
				},
				"natives": 	{
					"linux": str,
					"osx": str,
					"windows": str,
				},
				"rules": 	[
						{
						"action": str,
						"os": 	{
							"name": str,
						},
					},
				],
			},
		],
		"logging": 	{
			"client": 	{
				"argument": str,
				"file": 	{
					"id": str,
					"sha1": str,
					"size": int,
					"url": str,
				},
				"type": str,
			},
		},
		"mainClass": str,
		"minecraftArguments": str,
		"minimumLauncherVersion": int,
		"releaseTime": str,
		"time": str,
		"type": str,
	},

	```

=== "F9"
	For versions:

	 - 14w27a - 14w27b

	``` json
	{
		"assetIndex": 	{
			"id": str,
			"sha1": str,
			"size": int,
			"totalSize": int,
			"url": str,
		},
		"assets": str,
		"complianceLevel": int,
		"downloads": 	{
			"client": 	{
				"sha1": str,
				"size": int,
				"url": str,
			},
			"server": 	{
				"sha1": str,
				"size": int,
				"url": str,
			},
			"windows_server": 	{
				"sha1": str,
				"size": int,
				"url": str,
			},
		},
		"id": str,
		"javaVersion": 	{
			"component": str,
			"majorVersion": int,
		},
		"libraries": 	[
				{
				"downloads": 	{
					"artifact": 	{
						"path": str,
						"sha1": str,
						"size": int,
						"url": str,
					},
					"classifiers": 	{
						"natives-linux": 	{
							"path": str,
							"sha1": str,
							"size": int,
							"url": str,
						},
						"natives-osx": 	{
							"path": str,
							"sha1": str,
							"size": int,
							"url": str,
						},
						"natives-windows": 	{
							"path": str,
							"sha1": str,
							"size": int,
							"url": str,
						},
						"natives-windows-32": 	{
							"path": str,
							"sha1": str,
							"size": int,
							"url": str,
						},
						"natives-windows-64": 	{
							"path": str,
							"sha1": str,
							"size": int,
							"url": str,
						},
					},
				},
				"name": str,
				"extract": 	{
					"exclude": 	[
						str,
					],
				},
				"natives": 	{
					"linux": str,
					"osx": str,
					"windows": str,
				},
				"rules": 	[
						{
						"action": str,
						"os": 	{
							"name": str,
						},
					},
				],
			},
		],
		"mainClass": str,
		"minecraftArguments": str,
		"minimumLauncherVersion": int,
		"releaseTime": str,
		"time": str,
		"type": str,
	},

	```

=== "F10"
	For versions:

	 - 16w05a - 1.12.2

	``` json
	{
		"assetIndex": 	{
			"id": str,
			"sha1": str,
			"size": int,
			"totalSize": int,
			"url": str,
		},
		"assets": str,
		"complianceLevel": int,
		"downloads": 	{
			"client": 	{
				"sha1": str,
				"size": int,
				"url": str,
			},
			"server": 	{
				"sha1": str,
				"size": int,
				"url": str,
			},
		},
		"id": str,
		"javaVersion": 	{
			"component": str,
			"majorVersion": int,
		},
		"libraries": 	[
				{
				"downloads": 	{
					"artifact": 	{
						"path": str,
						"sha1": str,
						"size": int,
						"url": str,
					},
					"classifiers": 	{
						"natives-linux": 	{
							"path": str,
							"sha1": str,
							"size": int,
							"url": str,
						},
						"natives-osx": 	{
							"path": str,
							"sha1": str,
							"size": int,
							"url": str,
						},
						"natives-windows": 	{
							"path": str,
							"sha1": str,
							"size": int,
							"url": str,
						},
					},
				},
				"name": str,
				"rules": 	[
						{
						"action": str,
						"os": 	{
							"name": str,
						},
					},
				],
				"extract": 	{
					"exclude": 	[
						str,
					],
				},
				"natives": 	{
					"linux": str,
					"osx": str,
					"windows": str,
				},
			},
		],
		"logging": 	{
			"client": 	{
				"argument": str,
				"file": 	{
					"id": str,
					"sha1": str,
					"size": int,
					"url": str,
				},
				"type": str,
			},
		},
		"mainClass": str,
		"minecraftArguments": str,
		"minimumLauncherVersion": int,
		"releaseTime": str,
		"time": str,
		"type": str,
	},

	```

=== "F11"
	For versions:

	 - 17w43a - 1.13-pre1

	``` json
	{
		"arguments": 	{
			"game": 	[
				str,
					{
					"rules": 	[
							{
							"action": str,
							"features": 	{
								"is_demo_user": bool,
								"has_custom_resolution": bool,
							},
						},
					],
					"value": str,
						[
						str,
					],
				},
			],
			"jvm": 	[
					{
					"rules": 	[
							{
							"action": str,
							"os": 	{
								"name": str,
								"version": str,
							},
						},
					],
					"value": 	[
						str,
					],
					str,
				},
				str,
			],
		},
		"assetIndex": 	{
			"id": str,
			"sha1": str,
			"size": int,
			"totalSize": int,
			"url": str,
		},
		"assets": str,
		"complianceLevel": int,
		"downloads": 	{
			"client": 	{
				"sha1": str,
				"size": int,
				"url": str,
			},
			"server": 	{
				"sha1": str,
				"size": int,
				"url": str,
			},
		},
		"id": str,
		"javaVersion": 	{
			"component": str,
			"majorVersion": int,
		},
		"libraries": 	[
				{
				"downloads": 	{
					"artifact": 	{
						"path": str,
						"sha1": str,
						"size": int,
						"url": str,
					},
					"classifiers": 	{
						"natives-linux": 	{
							"path": str,
							"sha1": str,
							"size": int,
							"url": str,
						},
						"natives-macos": 	{
							"path": str,
							"sha1": str,
							"size": int,
							"url": str,
						},
						"natives-windows": 	{
							"path": str,
							"sha1": str,
							"size": int,
							"url": str,
						},
						"natives-osx": 	{
							"path": str,
							"sha1": str,
							"size": int,
							"url": str,
						},
					},
				},
				"name": str,
				"natives": 	{
					"linux": str,
					"osx": str,
					"windows": str,
				},
				"extract": 	{
					"exclude": 	[
						str,
					],
				},
				"rules": 	[
						{
						"action": str,
						"os": 	{
							"name": str,
						},
					},
				],
			},
		],
		"logging": 	{
			"client": 	{
				"argument": str,
				"file": 	{
					"id": str,
					"sha1": str,
					"size": int,
					"url": str,
				},
				"type": str,
			},
		},
		"mainClass": str,
		"minimumLauncherVersion": int,
		"releaseTime": str,
		"time": str,
		"type": str,
	},

	```

=== "F12"
	For versions:

	 - 1.13-pre2 - 1.14.4-pre7
	 - 19w34a - 19w35a

	``` json
	{
		"arguments": 	{
			"game": 	[
				str,
					{
					"rules": 	[
							{
							"action": str,
							"features": 	{
								"is_demo_user": bool,
								"has_custom_resolution": bool,
							},
						},
					],
					"value": str,
						[
						str,
					],
				},
			],
			"jvm": 	[
					{
					"rules": 	[
							{
							"action": str,
							"os": 	{
								"name": str,
								"version": str,
								"arch": str,
							},
						},
					],
					"value": 	[
						str,
					],
					str,
				},
				str,
			],
		},
		"assetIndex": 	{
			"id": str,
			"sha1": str,
			"size": int,
			"totalSize": int,
			"url": str,
		},
		"assets": str,
		"complianceLevel": int,
		"downloads": 	{
			"client": 	{
				"sha1": str,
				"size": int,
				"url": str,
			},
			"server": 	{
				"sha1": str,
				"size": int,
				"url": str,
			},
		},
		"id": str,
		"javaVersion": 	{
			"component": str,
			"majorVersion": int,
		},
		"libraries": 	[
				{
				"downloads": 	{
					"artifact": 	{
						"path": str,
						"sha1": str,
						"size": int,
						"url": str,
					},
					"classifiers": 	{
						"natives-linux": 	{
							"path": str,
							"sha1": str,
							"size": int,
							"url": str,
						},
						"natives-macos": 	{
							"path": str,
							"sha1": str,
							"size": int,
							"url": str,
						},
						"natives-windows": 	{
							"path": str,
							"sha1": str,
							"size": int,
							"url": str,
						},
						"natives-osx": 	{
							"path": str,
							"sha1": str,
							"size": int,
							"url": str,
						},
					},
				},
				"name": str,
				"natives": 	{
					"linux": str,
					"osx": str,
					"windows": str,
				},
				"extract": 	{
					"exclude": 	[
						str,
					],
				},
				"rules": 	[
						{
						"action": str,
						"os": 	{
							"name": str,
						},
					},
				],
			},
		],
		"logging": 	{
			"client": 	{
				"argument": str,
				"file": 	{
					"id": str,
					"sha1": str,
					"size": int,
					"url": str,
				},
				"type": str,
			},
		},
		"mainClass": str,
		"minimumLauncherVersion": int,
		"releaseTime": str,
		"time": str,
		"type": str,
	},

	```

=== "F13"
	For versions:

	 - 1.14.4 - 1.14.4
	 - 19w36a - 1.18.2
	 - 22w13oneblockatatime - 22w13oneblockatatime

	``` json
	{
		"arguments": 	{
			"game": 	[
				str,
					{
					"rules": 	[
							{
							"action": str,
							"features": 	{
								"is_demo_user": bool,
								"has_custom_resolution": bool,
							},
						},
					],
					"value": str,
						[
						str,
					],
				},
			],
			"jvm": 	[
					{
					"rules": 	[
							{
							"action": str,
							"os": 	{
								"name": str,
								"version": str,
								"arch": str,
							},
						},
					],
					"value": 	[
						str,
					],
					str,
				},
				str,
			],
		},
		"assetIndex": 	{
			"id": str,
			"sha1": str,
			"size": int,
			"totalSize": int,
			"url": str,
		},
		"assets": str,
		"complianceLevel": int,
		"downloads": 	{
			"client": 	{
				"sha1": str,
				"size": int,
				"url": str,
			},
			"client_mappings": 	{
				"sha1": str,
				"size": int,
				"url": str,
			},
			"server": 	{
				"sha1": str,
				"size": int,
				"url": str,
			},
			"server_mappings": 	{
				"sha1": str,
				"size": int,
				"url": str,
			},
		},
		"id": str,
		"javaVersion": 	{
			"component": str,
			"majorVersion": int,
		},
		"libraries": 	[
				{
				"downloads": 	{
					"artifact": 	{
						"path": str,
						"sha1": str,
						"size": int,
						"url": str,
					},
					"classifiers": 	{
						"natives-macos": 	{
							"path": str,
							"sha1": str,
							"size": int,
							"url": str,
						},
						"natives-linux": 	{
							"path": str,
							"sha1": str,
							"size": int,
							"url": str,
						},
						"natives-windows": 	{
							"path": str,
							"sha1": str,
							"size": int,
							"url": str,
						},
						"natives-osx": 	{
							"path": str,
							"sha1": str,
							"size": int,
							"url": str,
						},
					},
				},
				"name": str,
				"rules": 	[
						{
						"action": str,
						"os": 	{
							"name": str,
						},
					},
				],
				"natives": 	{
					"osx": str,
					"linux": str,
					"windows": str,
				},
				"extract": 	{
					"exclude": 	[
						str,
					],
				},
			},
		],
		"logging": 	{
			"client": 	{
				"argument": str,
				"file": 	{
					"id": str,
					"sha1": str,
					"size": int,
					"url": str,
				},
				"type": str,
			},
		},
		"mainClass": str,
		"minimumLauncherVersion": int,
		"releaseTime": str,
		"time": str,
		"type": str,
	},

	```

=== "F14"
	For versions:

	 - 22w11a - 22w13a
	 - 22w14a - 22w17a

	``` json
	{
		"arguments": 	{
			"game": 	[
				str,
					{
					"rules": 	[
							{
							"action": str,
							"features": 	{
								"is_demo_user": bool,
								"has_custom_resolution": bool,
							},
						},
					],
					"value": str,
						[
						str,
					],
				},
			],
			"jvm": 	[
					{
					"rules": 	[
							{
							"action": str,
							"os": 	{
								"name": str,
								"version": str,
								"arch": str,
							},
						},
					],
					"value": 	[
						str,
					],
					str,
				},
				str,
			],
		},
		"assetIndex": 	{
			"id": str,
			"sha1": str,
			"size": int,
			"totalSize": int,
			"url": str,
		},
		"assets": str,
		"complianceLevel": int,
		"downloads": 	{
			"client": 	{
				"sha1": str,
				"size": int,
				"url": str,
			},
			"client_mappings": 	{
				"sha1": str,
				"size": int,
				"url": str,
			},
			"server": 	{
				"sha1": str,
				"size": int,
				"url": str,
			},
			"server_mappings": 	{
				"sha1": str,
				"size": int,
				"url": str,
			},
		},
		"id": str,
		"javaVersion": 	{
			"component": str,
			"majorVersion": int,
		},
		"libraries": 	[
				{
				"downloads": 	{
					"artifact": 	{
						"path": str,
						"sha1": str,
						"size": int,
						"url": str,
					},
					"classifiers": 	{
						"natives-macos": 	{
							"path": str,
							"sha1": str,
							"size": int,
							"url": str,
						},
						"natives-linux": 	{
							"path": str,
							"sha1": str,
							"size": int,
							"url": str,
						},
						"natives-windows": 	{
							"path": str,
							"sha1": str,
							"size": int,
							"url": str,
						},
					},
				},
				"name": str,
				"rules": 	[
						{
						"action": str,
						"os": 	{
							"name": str,
						},
					},
				],
				"natives": 	{
					"osx": str,
					"linux": str,
					"windows": str,
				},
				"extract": 	{
					"exclude": 	[
						str,
					],
				},
			},
		],
		"logging": 	{
			"client": 	{
				"argument": str,
				"file": 	{
					"id": str,
					"sha1": str,
					"size": int,
					"url": str,
				},
				"type": str,
			},
		},
		"mainClass": str,
		"minimumLauncherVersion": int,
		"releaseTime": str,
		"time": str,
		"type": str,
	},

	```

=== "F15"
	For versions:

	 - 22w18a - 22w19a

	``` json
	{
		"arguments": 	{
			"game": 	[
				str,
					{
					"rules": 	[
							{
							"action": str,
							"features": 	{
								"is_demo_user": bool,
								"has_custom_resolution": bool,
							},
						},
					],
					"value": str,
						[
						str,
					],
				},
			],
			"jvm": 	[
					{
					"rules": 	[
							{
							"action": str,
							"os": 	{
								"name": str,
								"version": str,
								"arch": str,
							},
						},
					],
					"value": 	[
						str,
					],
					str,
				},
				str,
			],
		},
		"assetIndex": 	{
			"id": str,
			"sha1": str,
			"size": int,
			"totalSize": int,
			"url": str,
		},
		"assets": str,
		"complianceLevel": int,
		"downloads": 	{
			"client": 	{
				"sha1": str,
				"size": int,
				"url": str,
			},
			"client_mappings": 	{
				"sha1": str,
				"size": int,
				"url": str,
			},
			"server": 	{
				"sha1": str,
				"size": int,
				"url": str,
			},
			"server_mappings": 	{
				"sha1": str,
				"size": int,
				"url": str,
			},
		},
		"id": str,
		"javaVersion": 	{
			"component": str,
			"majorVersion": int,
		},
		"libraries": 	[
				{
				"downloads": 	{
					"artifact": 	{
						"path": str,
						"sha1": str,
						"size": int,
						"url": str,
					},
					"classifiers": 	{
						"linux-x86_64": 	{
							"path": str,
							"sha1": str,
							"size": int,
							"url": str,
						},
						"natives-linux": 	{
							"path": str,
							"sha1": str,
							"size": int,
							"url": str,
						},
						"natives-macos": 	{
							"path": str,
							"sha1": str,
							"size": int,
							"url": str,
						},
						"natives-windows": 	{
							"path": str,
							"sha1": str,
							"size": int,
							"url": str,
						},
					},
				},
				"name": str,
				"natives": 	{
					"linux": str,
					"osx": str,
					"windows": str,
				},
				"rules": 	[
						{
						"action": str,
						"os": 	{
							"name": str,
						},
					},
				],
			},
		],
		"logging": 	{
			"client": 	{
				"argument": str,
				"file": 	{
					"id": str,
					"sha1": str,
					"size": int,
					"url": str,
				},
				"type": str,
			},
		},
		"mainClass": str,
		"minimumLauncherVersion": int,
		"releaseTime": str,
		"time": str,
		"type": str,
	},

	```

=== "F16"
	For versions:

	 - 1.19-pre1 - 23w13a_or_b

	``` json
	{
		"arguments": 	{
			"game": 	[
				str,
					{
					"rules": 	[
							{
							"action": str,
							"features": 	{
								"is_demo_user": bool,
								"has_custom_resolution": bool,
							},
						},
					],
					"value": str,
						[
						str,
					],
				},
			],
			"jvm": 	[
					{
					"rules": 	[
							{
							"action": str,
							"os": 	{
								"name": str,
								"version": str,
								"arch": str,
							},
						},
					],
					"value": 	[
						str,
					],
					str,
				},
				str,
			],
		},
		"assetIndex": 	{
			"id": str,
			"sha1": str,
			"size": int,
			"totalSize": int,
			"url": str,
		},
		"assets": str,
		"complianceLevel": int,
		"downloads": 	{
			"client": 	{
				"sha1": str,
				"size": int,
				"url": str,
			},
			"client_mappings": 	{
				"sha1": str,
				"size": int,
				"url": str,
			},
			"server": 	{
				"sha1": str,
				"size": int,
				"url": str,
			},
			"server_mappings": 	{
				"sha1": str,
				"size": int,
				"url": str,
			},
		},
		"id": str,
		"javaVersion": 	{
			"component": str,
			"majorVersion": int,
		},
		"libraries": 	[
				{
				"downloads": 	{
					"artifact": 	{
						"path": str,
						"sha1": str,
						"size": int,
						"url": str,
					},
				},
				"name": str,
				"rules": 	[
						{
						"action": str,
						"os": 	{
							"name": str,
						},
					},
				],
			},
		],
		"logging": 	{
			"client": 	{
				"argument": str,
				"file": 	{
					"id": str,
					"sha1": str,
					"size": int,
					"url": str,
				},
				"type": str,
			},
		},
		"mainClass": str,
		"minimumLauncherVersion": int,
		"releaseTime": str,
		"time": str,
		"type": str,
	},

	```

=== "F17"
	For versions:

	 - 23w14a - 23w17a

	``` json
	{
		"arguments": 	{
			"game": 	[
				str,
					{
					"rules": 	[
							{
							"action": str,
							"features": 	{
								"is_demo_user": bool,
								"has_custom_resolution": bool,
								"has_quick_plays_support": bool,
								"is_quick_play_singleplayer": bool,
								"is_quick_play_multiplayer": bool,
								"is_quick_play_realms": bool,
							},
						},
					],
					"value": str,
						[
						str,
					],
				},
			],
			"jvm": 	[
					{
					"rules": 	[
							{
							"action": str,
							"os": 	{
								"name": str,
								"version": str,
								"arch": str,
							},
						},
					],
					"value": 	[
						str,
					],
					str,
				},
				str,
			],
		},
		"assetIndex": 	{
			"id": str,
			"sha1": str,
			"size": int,
			"totalSize": int,
			"url": str,
		},
		"assets": str,
		"complianceLevel": int,
		"downloads": 	{
			"client": 	{
				"sha1": str,
				"size": int,
				"url": str,
			},
			"client_mappings": 	{
				"sha1": str,
				"size": int,
				"url": str,
			},
			"server": 	{
				"sha1": str,
				"size": int,
				"url": str,
			},
			"server_mappings": 	{
				"sha1": str,
				"size": int,
				"url": str,
			},
		},
		"id": str,
		"javaVersion": 	{
			"component": str,
			"majorVersion": int,
		},
		"libraries": 	[
				{
				"downloads": 	{
					"artifact": 	{
						"path": str,
						"sha1": str,
						"size": int,
						"url": str,
					},
				},
				"name": str,
				"rules": 	[
						{
						"action": str,
						"os": 	{
							"name": str,
						},
					},
				],
			},
		],
		"logging": 	{
			"client": 	{
				"argument": str,
				"file": 	{
					"id": str,
					"sha1": str,
					"size": int,
					"url": str,
				},
				"type": str,
			},
		},
		"mainClass": str,
		"minimumLauncherVersion": int,
		"releaseTime": str,
		"time": str,
		"type": str,
	},

	```

=== "F18"
	For versions:

	 - 23w18a - 23w40a

	``` json
	{
		"arguments": 	{
			"game": 	[
				str,
					{
					"rules": 	[
							{
							"action": str,
							"features": 	{
								"is_demo_user": bool,
								"has_custom_resolution": bool,
								"has_quick_plays_support": bool,
								"is_quick_play_singleplayer": bool,
								"is_quick_play_multiplayer": bool,
								"is_quick_play_realms": bool,
							},
						},
					],
					"value": str,
						[
						str,
					],
				},
			],
			"jvm": 	[
					{
					"rules": 	[
							{
							"action": str,
							"os": 	{
								"name": str,
								"arch": str,
							},
						},
					],
					"value": 	[
						str,
					],
					str,
				},
				str,
			],
		},
		"assetIndex": 	{
			"id": str,
			"sha1": str,
			"size": int,
			"totalSize": int,
			"url": str,
		},
		"assets": str,
		"complianceLevel": int,
		"downloads": 	{
			"client": 	{
				"sha1": str,
				"size": int,
				"url": str,
			},
			"client_mappings": 	{
				"sha1": str,
				"size": int,
				"url": str,
			},
			"server": 	{
				"sha1": str,
				"size": int,
				"url": str,
			},
			"server_mappings": 	{
				"sha1": str,
				"size": int,
				"url": str,
			},
		},
		"id": str,
		"javaVersion": 	{
			"component": str,
			"majorVersion": int,
		},
		"libraries": 	[
				{
				"downloads": 	{
					"artifact": 	{
						"path": str,
						"sha1": str,
						"size": int,
						"url": str,
					},
				},
				"name": str,
				"rules": 	[
						{
						"action": str,
						"os": 	{
							"name": str,
						},
					},
				],
			},
		],
		"logging": 	{
			"client": 	{
				"argument": str,
				"file": 	{
					"id": str,
					"sha1": str,
					"size": int,
					"url": str,
				},
				"type": str,
			},
		},
		"mainClass": str,
		"minimumLauncherVersion": int,
		"releaseTime": str,
		"time": str,
		"type": str,
	},

	```

