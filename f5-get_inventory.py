#f5-sdk 3.0.21 Released: Apr 11, 2019 https://github.com/F5Networks/f5-common-python

from f5.bigip import ManagementRoot
from datetime import datetime
import pprint
import json

# Define file path and file names

inventory_file_path = "./inventory.json"

# Read the content of the file and save it in a List

devices = {}

# Opening JSON file
with open(inventory_file_path) as json_file:
    devices = json.load(json_file)

#pprint.pprint(devices)

today = datetime.now()
datetimenow = today.strftime('%Y-%m-%d-%H%M%S')
export_filename = "./f5-get_inventory-export-"+datetimenow+".json"

inventory = {}
exported_inventory = {}

for device in devices:
    device_type = devices[device]["inventory_network_os"]
    management_ip = devices[device]["inventory_host"]
    device_location = devices[device]["inventory_network_location"]

    if device_type == "f5.bigip":  
    #if device_type == "f5.bigip" and device_location == "Home":               
        exported_inventory[device] = {}
        exported_inventory[device]["Inventory_Network_OS"] = device_type
        exported_inventory[device]["Management_IP"] = management_ip
        exported_inventory[device]["Status"] = ""        
        try:
        # Connect to the BigIP
            mgmt = ManagementRoot(management_ip, devices[device]["inventory_user"], devices[device]["inventory_pass"], timeout=10)
            exported_inventory[device]["Status"] = "Connected"
            sys_versions = mgmt.tm.sys.version.load()
            hardware_info = mgmt.tm.sys.hardware.load()

            version_info = sys_versions.entries["https://localhost/mgmt/tm/sys/version/0"]["nestedStats"]["entries"]
            plaform_info = hardware_info.entries["https://localhost/mgmt/tm/sys/hardware/platform"]["nestedStats"]["entries"]["https://localhost/mgmt/tm/sys/hardware/platform/0"]["nestedStats"]["entries"]
            system_info = hardware_info.entries["https://localhost/mgmt/tm/sys/hardware/system-info"]["nestedStats"]["entries"]["https://localhost/mgmt/tm/sys/hardware/system-info/0"]["nestedStats"]["entries"]

            for version_item in version_info:
                version_item_value = version_info[version_item]["description"]
                exported_inventory[device][version_item] = version_item_value
            for platform_item  in plaform_info:
                platform_item_value = plaform_info[platform_item]["description"]
                exported_inventory[device][platform_item] = platform_item_value
            for system_item  in system_info:
                system_item_value = system_info[system_item]["description"]
                exported_inventory[device][system_item] = system_item_value
            
        except Exception as e:
            exported_inventory[device]["Status"] = str(e)
        pprint.pprint(exported_inventory)
    # Convert and write JSON object to file
    with open(export_filename, "w") as outfile: 
        json.dump(exported_inventory, outfile)
