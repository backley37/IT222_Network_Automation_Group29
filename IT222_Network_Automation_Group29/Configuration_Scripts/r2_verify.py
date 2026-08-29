from netmiko import ConnectHandler

# Replace the GNS3 console details before running.
DEVICE = {
    "device_type": "cisco_ios_telnet",
    "host": "192.168.56.103",   # GNS3 VM/server IP
    "port": 5002,               
    "username": "",
    "password": "",
    "secret": "",
}

COMMANDS = ['show ip interface brief',
            'show interfaces GigabitEthernet0/0.57', 
            'show interfaces GigabitEthernet0/0.87', 
            'show ip route static', 
            'show running-config | section interface GigabitEthernet0/0'
            'show running-config | section interface GigabitEthernet0/1',
            ]

with ConnectHandler(**DEVICE) as conn:
    for command in COMMANDS:
        print("\n###", command)
        print(conn.send_command(command))
