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

TESTS = [
    ("R2 to R1 routed link", "10.29.29.1"),
    ("R2 to Site A Newsroom gateway", "10.57.1.1"),
    ("R2 to Site A PostProduction gateway", "10.87.1.1"),
]

with ConnectHandler(**DEVICE) as conn:
    for label, destination in TESTS:
        print(f"\n### {label}: ping {destination}")
        print(conn.send_command(f"ping {destination}"))
