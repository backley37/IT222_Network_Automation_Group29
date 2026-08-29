from netmiko import ConnectHandler

# Replace the GNS3 console details before running.
DEVICE = {
    "device_type": "cisco_ios_telnet",
    "host": "192.168.56.103",   # GNS3 VM/server IP
    "port": 5004,               
    "username": "",
    "password": "",
    "secret": "",
}

# Switch-level operational test: confirm learned MAC addresses.
with ConnectHandler(**DEVICE) as conn:
    print(conn.send_command("show mac address-table"))
