# f5-get_inventory

This Python script connects to each F5 BIG-IP devices in your inventory via REST API and collects some information ie. version, platform, serial number, base mac address. The script will export the collected information to a json file.

The F5 BIG-IP credential information are in the inventory.json file as below format.

```json
{
    "bigip1": {
        "inventory_network_os": "f5.bigip",    
        "inventory_network_location": "Home",         
        "inventory_host": "192.168.1.245",
        "inventory_user": "admin",
        "inventory_pass": "password",
        "inventory_cli_port": "22",        
        "inventory_rest_port": "443"
    },
    "bigip2": {
        "inventory_network_os": "f5.bigip",    
        "inventory_network_location": "Home",         
        "inventory_host": "192.168.1.246",
        "inventory_user": "admin",
        "inventory_pass": "password",
        "inventory_cli_port": "22",        
        "inventory_rest_port": "443"
    },
     "bigip11": {
        "inventory_network_os": "f5.bigip",    
        "inventory_network_location": "Home",         
        "inventory_host": "192.168.1.231",
        "inventory_user": "admin",
        "inventory_pass": "password",
        "inventory_cli_port": "22",        
        "inventory_rest_port": "443"
    }                                                                                                                                                                                                                                                                                                                        
}
```

## Usage:
```bash

python f5-get_inventory.py
```

## Files
- f5-get_inventory.py >> This script file
- inventory.json >> F5 BIG-IP information ie management ip, username, password, location etc.
- f5-get_inventory-export-datetimenow.json >> Output file format

## output File Example
the output file name format will be f5-get_inventory-export-datetimenow.json

When we run the script, bigip7 and bigip9 was unreachable. So that the information is missing for these unreachable devices in the output json file.

```json
{
	"bigip1": {
		"Inventory_Network_OS": "f5.bigip",
		"Management_IP": "192.168.1.245",
		"Status": "Connected",
		"Build": "0.44.2",
		"Date": "Wed Oct 25 15:58:18 PDT 2023",
		"Edition": "Engineering Hotfix",
		"Product": "BIG-IP",
		"Title": "Main Package",
		"Version": "15.1.10.2",
		"baseMac": "aa:bb:cc:b7:79:a0",
		"biosRev": " ",
		"cloudName": " ",
		"hypervisorName": "VMware Virtual Platform",
		"marketingName": "BIG-IP Virtual Edition",
		"bigipChassisSerialNum": "aabbccdd-eeff-c019-8daca9b779a0",
		"hostBoardPartRevNum": " ",
		"hostBoardSerialNum": " ",
		"platform": "Z100",
		"project_200LevelBomNum": " ",
		"switchBoardPartRevNum": " ",
		"switchBoardSerialNum": " "
	},
	"bigip2": {
		"Inventory_Network_OS": "f5.bigip",
		"Management_IP": "192.168.1.246",
		"Status": "Connected",
		"Build": "0.44.2",
		"Date": "Wed Oct 25 15:58:18 PDT 2023",
		"Edition": "Engineering Hotfix",
		"Product": "BIG-IP",
		"Title": "Main Package",
		"Version": "15.1.10.2",
		"baseMac": "aa:bb:cc:fc:66:f2",
		"biosRev": " ",
		"cloudName": " ",
		"hypervisorName": "VMware Virtual Platform",
		"marketingName": "BIG-IP Virtual Edition",
		"bigipChassisSerialNum": "aabbccdd-eeff-9f8d-d8bfa9fc66f2",
		"hostBoardPartRevNum": " ",
		"hostBoardSerialNum": " ",
		"platform": "Z100",
		"project_200LevelBomNum": " ",
		"switchBoardPartRevNum": " ",
		"switchBoardSerialNum": " "
	},
	"bigip3": {
		"Inventory_Network_OS": "f5.bigip",
		"Management_IP": "192.168.1.247",
		"Status": "Connected",
		"Build": "0.44.2",
		"Date": "Wed Oct 25 15:58:18 PDT 2023",
		"Edition": "Engineering Hotfix",
		"Product": "BIG-IP",
		"Title": "Main Package",
		"Version": "15.1.10.2",
		"baseMac": "aa:bb:cc:66:cc:f4",
		"biosRev": " ",
		"cloudName": " ",
		"hypervisorName": "VMware Virtual Platform",
		"marketingName": "BIG-IP Virtual Edition",
		"bigipChassisSerialNum": "aabbccdd-eeff-da77-58838466ccf4",
		"hostBoardPartRevNum": " ",
		"hostBoardSerialNum": " ",
		"platform": "Z100",
		"project_200LevelBomNum": " ",
		"switchBoardPartRevNum": " ",
		"switchBoardSerialNum": " "
	},
	"bigip4": {
		"Inventory_Network_OS": "f5.bigip",
		"Management_IP": "192.168.1.248",
		"Status": "Connected",
		"Build": "0.44.2",
		"Date": "Wed Oct 25 15:58:18 PDT 2023",
		"Edition": "Engineering Hotfix",
		"Product": "BIG-IP",
		"Title": "Main Package",
		"Version": "15.1.10.2",
		"baseMac": "aa:bb:cc:1b:6d:58",
		"biosRev": " ",
		"cloudName": " ",
		"hypervisorName": "VMware Virtual Platform",
		"marketingName": "BIG-IP Virtual Edition",
		"bigipChassisSerialNum": "aabbccdd-eeff-4818-a5c3811b6d58",
		"hostBoardPartRevNum": " ",
		"hostBoardSerialNum": " ",
		"platform": "Z100",
		"project_200LevelBomNum": " ",
		"switchBoardPartRevNum": " ",
		"switchBoardSerialNum": " "
	},
	"bigip5": {
		"Inventory_Network_OS": "f5.bigip",
		"Management_IP": "192.168.1.249",
		"Status": "Connected",
		"Build": "0.44.2",
		"Date": "Wed Oct 25 15:58:18 PDT 2023",
		"Edition": "Engineering Hotfix",
		"Product": "BIG-IP",
		"Title": "Main Package",
		"Version": "15.1.10.2",
		"baseMac": "aa:bb:cc:c3:64:83",
		"biosRev": " ",
		"cloudName": " ",
		"hypervisorName": "VMware Virtual Platform",
		"marketingName": "BIG-IP Virtual Edition",
		"bigipChassisSerialNum": "aabbccdd-eeff-0720-30aa71c36483",
		"hostBoardPartRevNum": " ",
		"hostBoardSerialNum": " ",
		"platform": "Z100",
		"project_200LevelBomNum": " ",
		"switchBoardPartRevNum": " ",
		"switchBoardSerialNum": " "
	},
	"bigip6": {
		"Inventory_Network_OS": "f5.bigip",
		"Management_IP": "192.168.1.250",
		"Status": "Connected",
		"Build": "0.44.2",
		"Date": "Wed Oct 25 15:58:18 PDT 2023",
		"Edition": "Engineering Hotfix",
		"Product": "BIG-IP",
		"Title": "Main Package",
		"Version": "15.1.10.2",
		"baseMac": "aa:bb:cc:04:70:ce",
		"biosRev": " ",
		"cloudName": " ",
		"hypervisorName": "VMware Virtual Platform",
		"marketingName": "BIG-IP Virtual Edition",
		"bigipChassisSerialNum": "aabbccdd-eeff-82cf-b5d5ed0470ce",
		"hostBoardPartRevNum": " ",
		"hostBoardSerialNum": " ",
		"platform": "Z100",
		"project_200LevelBomNum": " ",
		"switchBoardPartRevNum": " ",
		"switchBoardSerialNum": " "
	},
	"bigip7": {
		"Inventory_Network_OS": "f5.bigip",
		"Management_IP": "192.168.1.251",
		"Status": "HTTPSConnectionPool(host='192.168.1.251', port=443): Max retries exceeded with url: /mgmt/tm/sys/ (Caused by NewConnectionError('<urllib3.connection.HTTPSConnection object at 0x7f791c858310>: Failed to establish a new connection: [Errno 113] No route to host'))"
	},
	"bigip8": {
		"Inventory_Network_OS": "f5.bigip",
		"Management_IP": "192.168.1.244",
		"Status": "Connected",
		"Build": "0.44.2",
		"Date": "Wed Oct 25 15:58:18 PDT 2023",
		"Edition": "Engineering Hotfix",
		"Product": "BIG-IP",
		"Title": "Main Package",
		"Version": "15.1.10.2",
		"baseMac": "aa:bb:cc:02:f1:10",
		"biosRev": " ",
		"cloudName": " ",
		"hypervisorName": "VMware Virtual Platform",
		"marketingName": "BIG-IP Virtual Edition",
		"bigipChassisSerialNum": "aabbccdd-eeff-5c93-d66e5502f110",
		"hostBoardPartRevNum": " ",
		"hostBoardSerialNum": " ",
		"platform": "Z100",
		"project_200LevelBomNum": " ",
		"switchBoardPartRevNum": " ",
		"switchBoardSerialNum": " "
	},
	"bigip9": {
		"Inventory_Network_OS": "f5.bigip",
		"Management_IP": "192.168.1.252",
		"Status": "HTTPSConnectionPool(host='192.168.1.252', port=443): Max retries exceeded with url: /mgmt/tm/sys/ (Caused by NewConnectionError('<urllib3.connection.HTTPSConnection object at 0x7f791c7e35e0>: Failed to establish a new connection: [Errno 113] No route to host'))"
	},
	"bigip10": {
		"Inventory_Network_OS": "f5.bigip",
		"Management_IP": "192.168.1.243",
		"Status": "Connected",
		"Build": "0.0.12",
		"Date": "Wed Nov 15 11:32:44 PST 2023",
		"Edition": "Point Release 3",
		"Product": "BIG-IP",
		"Title": "Main Package",
		"Version": "15.1.10.3",
		"baseMac": "aa:bb:cc:b2:66:44",
		"biosRev": " ",
		"cloudName": " ",
		"hypervisorName": "VMware Virtual Platform",
		"marketingName": "BIG-IP Virtual Edition",
		"bigipChassisSerialNum": "aabbccdd-eeff-42dc-d0058db26644",
		"hostBoardPartRevNum": " ",
		"hostBoardSerialNum": " ",
		"platform": "Z100",
		"project_200LevelBomNum": " ",
		"switchBoardPartRevNum": " ",
		"switchBoardSerialNum": " "
	},
	"bigip11": {
		"Inventory_Network_OS": "f5.bigip",
		"Management_IP": "192.168.1.231",
		"Status": "Connected",
		"Build": "0.0.12",
		"Date": "Wed Nov 15 11:32:44 PST 2023",
		"Edition": "Point Release 3",
		"Product": "BIG-IP",
		"Title": "Main Package",
		"Version": "15.1.10.3",
		"baseMac": "aa:bb:cc:7b:0f:53",
		"biosRev": " ",
		"cloudName": " ",
		"hypervisorName": "VMware Virtual Platform",
		"marketingName": "BIG-IP Virtual Edition",
		"bigipChassisSerialNum": "aabbccdd-eeff-7ca0-c097497b0f53",
		"hostBoardPartRevNum": " ",
		"hostBoardSerialNum": " ",
		"platform": "Z100",
		"project_200LevelBomNum": " ",
		"switchBoardPartRevNum": " ",
		"switchBoardSerialNum": " "
	}
}
```
# Collecting Same Information via curl

```bash
curl -s -k -u "admin:password" https://192.168.1.245/mgmt/tm/sys/version | json_pp
```
```json
{
   "entries" : {
      "https://localhost/mgmt/tm/sys/version/0" : {
         "nestedStats" : {
            "entries" : {
               "Build" : {
                  "description" : "0.44.2"
               },
               "Date" : {
                  "description" : "Wed Oct 25 15:58:18 PDT 2023"
               },
               "Edition" : {
                  "description" : "Engineering Hotfix"
               },
               "Product" : {
                  "description" : "BIG-IP"
               },
               "Title" : {
                  "description" : "Main Package"
               },
               "Version" : {
                  "description" : "15.1.10.2"
               }
            }
         }
      },
      "https://localhost/mgmt/tm/sys/version/1" : {
         "nestedStats" : {
            "entries" : {
               "ID1117229_2" : {
                  "description" : "ID1117229-2"
               },
               "ID1240121_2" : {
                  "description" : "ID1240121-2"
               },
               "ID1381357_3" : {
                  "description" : "ID1381357-3"
               }
            }
         }
      }
   },
   "kind" : "tm:sys:version:versionstats",
   "selfLink" : "https://localhost/mgmt/tm/sys/version?ver=15.1.10.2"
}
```

```bash
curl -s -k -u "admin:password" https://192.168.1.245/mgmt/tm/sys/hardware | json_pp
```

```json
{
      "https://localhost/mgmt/tm/sys/hardware/platform" : {
         "nestedStats" : {
            "entries" : {
               "https://localhost/mgmt/tm/sys/hardware/platform/0" : {
                  "nestedStats" : {
                     "entries" : {
                        "baseMac" : {
                           "description" : "aa:bb:cc:b7:79:a0"
                        },
                        "biosRev" : {
                           "description" : " "
                        },
                        "cloudName" : {
                           "description" : " "
                        },
                        "hypervisorName" : {
                           "description" : "VMware Virtual Platform"
                        },
                        "marketingName" : {
                           "description" : "BIG-IP Virtual Edition"
                        }
                     }
                  }
               }
            }
         }
      },
      "https://localhost/mgmt/tm/sys/hardware/system-info" : {
         "nestedStats" : {
            "entries" : {
               "https://localhost/mgmt/tm/sys/hardware/system-info/0" : {
                  "nestedStats" : {
                     "entries" : {
                        "bigipChassisSerialNum" : {
                           "description" : "aabbccdd-eeff-c019-8daca9b779a0"
                        },
                        "hostBoardPartRevNum" : {
                           "description" : " "
                        },
                        "hostBoardSerialNum" : {
                           "description" : " "
                        },
                        "platform" : {
                           "description" : "Z100"
                        },
                        "project_200LevelBomNum" : {
                           "description" : " "
                        },
                        "switchBoardPartRevNum" : {
                           "description" : " "
                        },
                        "switchBoardSerialNum" : {
                           "description" : " "
                        }
                     }
                  }
               }
            }
         }
      }
   },
   "kind" : "tm:sys:hardware:hardwarestats",
   "selfLink" : "https://localhost/mgmt/tm/sys/hardware?ver=15.1.10.2"
}
```
