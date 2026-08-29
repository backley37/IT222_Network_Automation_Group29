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

CONFIG = [
    "hostname SW2",
    "vlan 57",
    "name Newsroom",
    "exit",
    "vlan 87",
    "name PostProduction",
    "exit",
    "interface GigabitEthernet0/0",
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan 57,87",
    "no shutdown",
    "exit",
    "interface GigabitEthernet0/1",
    "switchport mode access",
    "switchport access vlan 57",
    "spanning-tree portfast",
    "no shutdown",
    "exit",
    "interface GigabitEthernet0/2",
    "switchport mode access",
    "switchport access vlan 87",
    "spanning-tree portfast",
    "no shutdown",
]

with ConnectHandler(**DEVICE) as conn:
    print(conn.send_config_set(CONFIG))
    print(conn.send_command("write memory"))
