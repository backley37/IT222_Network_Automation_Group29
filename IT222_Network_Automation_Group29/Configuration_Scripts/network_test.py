from netmiko import ConnectHandler

R1 = {"device_type":"cisco_ios_telnet",
      "host":"192.168.56.103",
      "port":5000,
      "username":"",
      "password":"",
      "secret":""}
R2 = {"device_type":"cisco_ios_telnet",
      "host":"192.168.56.103",
      "port":5002,
      "username":"",
      "password":"",
      "secret":""}

# Each test has a scenario purpose. The PCs themselves perform the most important
# end-to-end tests; these router tests verify the same routed destinations.
TESTS_R1 = [
    ("Newsroom Site A -> Newsroom Site B gateway", "10.57.2.1"),
    ("PostProduction Site A -> PostProduction Site B gateway", "10.87.2.1"),
    ("R1 -> R2 routed backbone", "10.29.29.2"),
]

TESTS_R2 = [
    ("Newsroom Site B -> Newsroom Site A gateway", "10.57.1.1"),
    ("PostProduction Site B -> PostProduction Site A gateway", "10.87.1.1"),
    ("R2 -> R1 routed backbone", "10.29.29.1"),
]

def run(device, tests):
    with ConnectHandler(**device) as conn:
        for purpose, dst in tests:
            print(f"\n### {purpose}")
            print(conn.send_command(f"ping {dst}"))

run(R1, TESTS_R1)
run(R2, TESTS_R2)

print("""
PC END-TO-END TESTS TO PERFORM IN GNS3
1. Newsroom-PC-A (10.57.1.10) -> Newsroom-PC-B (10.57.2.10)
2. PostProduction-PC-A (10.87.1.10) -> PostProduction-PC-B (10.87.2.10)
3. Newsroom-PC-A -> local PostProduction gateway (10.87.1.1)
4. PostProduction-PC-A -> local Newsroom gateway (10.57.1.1)
5. Newsroom-PC-B -> PostProduction-PC-B if inter-VLAN communication is intended.
""")
