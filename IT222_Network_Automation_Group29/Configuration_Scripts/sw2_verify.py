from netmiko import ConnectHandler

# Replace the GNS3 console details before running.
DEVICE = {
    "device_type": "cisco_ios_telnet",
    "host": "192.168.56.103",   # GNS3 VM/server IP
    "port": 5006,               # Change to this device's TELNET console port
    "username": "",
    "password": "",
    "secret": "",
}

COMMANDS = ['show vlan brief', 
            'show interfaces status', 
            'show interfaces trunk',
            'show interfaces GigabitEthernet0/0 switchport',
            'show interfaces GigabitEthernet0/1 switchport',
            'show interfaces GigabitEthernet0/2 switchport', 
            'show mac address-table',
            ]

with ConnectHandler(**DEVICE) as conn:
    for command in COMMANDS:
        print("\n###", command)
        print(conn.send_command(command))
