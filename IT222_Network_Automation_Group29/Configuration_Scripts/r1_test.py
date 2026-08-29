from netmiko import ConnectHandler

# Replace the GNS3 console details before running.
DEVICE = {
    "device_type": "cisco_ios_telnet",
    "host": "192.168.56.103",   # GNS3 VM/server IP
    "port": 5000,              
    "username": "",
    "password": "",
    "secret": "",
}

TESTS = [
    ("R1 to R2 routed link", "10.29.29.2"),
    ("R1 to Site B Newsroom gateway", "10.57.2.1"),
    ("R1 to Site B PostProduction gateway", "10.87.2.1"),
]

with ConnectHandler(**DEVICE) as conn:
    for label, destination in TESTS:
        print(f"\n### {label}: ping {destination}")
        print(conn.send_command(f"ping {destination}"))
