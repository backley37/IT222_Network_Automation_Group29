from netmiko import ConnectHandler

# Replace the GNS3 console details before running.
DEVICE = {
    "device_type": "cisco_ios_telnet",
    "host": "192.168.56.103",
    "port": 5000,               
    "username": "",
    "password": "",
    "secret": "",
}

CONFIG = [
    "hostname R1",
    "interface GigabitEthernet0/0",
    "no shutdown",
    "exit",
    "interface GigabitEthernet0/0.57",
    "encapsulation dot1Q 57",
    "ip address 10.57.1.1 255.255.255.0",
    "no shutdown",
    "exit", 
    "interface GigabitEthernet0/0.87",
    "encapsulation dot1Q 87",
    "ip address 10.87.1.1 255.255.255.0",
    "no shutdown",
    "exit",
    "interface GigabitEthernet0/1",
    "ip address 10.29.29.1 255.255.255.252",
    "no shutdown",
    "exit",
    "ip route 10.57.2.0 255.255.255.0 10.29.29.2",
    "ip route 10.87.2.0 255.255.255.0 10.29.29.2",
]

with ConnectHandler(**DEVICE) as conn:
    output = conn.send_config_set(CONFIG)
    print(output)
    print(conn.send_command("write memory"))
