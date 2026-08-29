from netmiko import ConnectHandler

DEVICES = {
    "R1": {"device_type":"cisco_ios_telnet","host":"192.168.56.103","port":5000,"username":"","password":"","secret":""},
    "R2": {"device_type":"cisco_ios_telnet","host":"192.168.56.103","port":5002,"username":"","password":"","secret":""},
    "SW1":{"device_type":"cisco_ios_telnet","host":"192.168.56.103","port":5004,"username":"","password":"","secret":""},
    "SW2":{"device_type":"cisco_ios_telnet","host":"192.168.56.103","port":5006,"username":"","password":"","secret":""},
}

CHECKS = {
    "R1": ["show ip interface brief", "show ip route static", "show running-config | section ip route"],
    "R2": ["show ip interface brief", "show ip route static", "show running-config | section ip route"],
    "SW1": ["show vlan brief", "show interfaces trunk", "show interface status", "show mac address-table",],
    "SW2": ["show vlan brief", "show interfaces trunk", "show interface status", "show mac address-table",],
}

for name, device in DEVICES.items():
    print("\n" + "="*70)
    print(name)
    print("="*70)
    try:
        with ConnectHandler(**device) as conn:
            for cmd in CHECKS[name]:
                print(f"\n### {cmd}")
                print(conn.send_command(cmd))
    except Exception as exc:
        print(f"ERROR connecting to {name}: {exc}")
