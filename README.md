# f5-get_inventory

This Python script connects to each F5 BIG-IP devices in your inventory and collects some information ie. version, platform, serial number, base mac address. The script will export the collected information into a json file.

The F5 BIG-IP credential information are in the inventory.json file as below format.

```yjson
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
