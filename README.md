 IT 222 – Assignment 29: Media Company Network

   1. Assignment Identification
- Course: IT 222 
- Assignment Number: 29
- Scenario: Media Company Network
- Group Number: 29
   
   2. Group Members: 
        
        1.RAMADHANI MOHAMED - 2024/1062
        
        2.BACKLEY MWEGALAWA - 2024/1530
       
        3.NASRA MWISHEHE    - 2024/1087
       
        4.THEOBAD AMOS      - 2024/1589   

   3. Scenario Description
A media company operates two facilities. Newsroom computers and PostProduction systems must use separate VLANs. The two facilities are interconnected through a routed R1–R2 link using static routing.

The automation solution is designed around the operational functions of a media company rather than being a generic VLAN exercise.

   4. Network Requirements
a. Separate Newsroom and PostProduction traffic with VLAN 57 and VLAN 87.
b. Provide router-on-a-stick inter-VLAN routing at both facilities.
c. Carry both VLANs over the switch-to-router 802.1Q trunks.
d. Interconnect the two facilities using the R1–R2 routed link.
e. Use static routing between the four site LANs.
f. Automate configuration, verification and testing with Python and Netmiko.
g. Demonstrate Newsroom and PostProduction connectivity between facilities and verify the static routes.

   5. Topology
                    R1----------Gi0/1----------R2
                     |                         |Gi0/1
                     | Gi0/1                   |
                    SW1                      SW2
                    / \                      / \
                   /   \                    /   \
            Gi0/2 /     \ Gi0/3       Gi0/2/     \Gi0/3
                 /       \                /       \
                /         \              /         \
              PC1        PC2           PC3        PC4

- SW1 Gi0/1 -> R1 Gi0/0: 802.1Q trunk, VLANs 57 and 87.
- SW2 Gi0/1 -> R2 Gi0/0: 802.1Q trunk, VLANs 57 and 87.
- SW1 Gi0/2 -> Newsroom-PC-1, VLAN 57.
- SW1 Gi0/3 -> PostProduction-PC-2, VLAN 87.
- SW2 Gi0/2 -> Newsroom-PC-3, VLAN 57.
- SW2 Gi0/3 -> PostProduction-PC-4, VLAN 87.
- R1 Gi0/1 <-> R2 Gi0/1: routed /30 link.

   6. Addressing and VLAN Plan


| Device/Site | Function        | VLAN  | Network       | Gateway/Address |

| R1 Site 1   | Newsroom        |   57  | 10.57.1.0/24  |    10.57.1.1    |
| R1 Site 2   | PostProduction  |   87  | 10.87.1.0/24  |    10.87.1.1    |
| R2 Site 3   | Newsroom        |   57  | 10.57.2.0/24  |    10.57.2.1    |
| R2 Site 4   | PostProduction  |   87  | 10.87.2.0/24  |    10.87.2.1    |
| R1-R2       | Routed backbone |   —   | 10.29.29.0/30 |   R1 .1, R2 .2  |
| PC-1        | Newsroom        |   57  | 10.57.1.0/24  |    10.57.1.10   |
| PC-2        | PostProduction  |   87  | 10.87.1.0/24  |    10.87.1.10   |
| PC-3        | Newsroom        |   57  | 10.57.2.0/24  |    10.57.2.10   |
| PC-4        | PostProduction  |   87  | 10.87.2.0/24  |    10.87.2.10   |

   7. Routing Method
          -   Static routes
R1:
- `ip route 10.57.2.0 255.255.255.0 10.29.29.2`
- `ip route 10.87.2.0 255.255.255.0 10.29.29.2`

R2:
- `ip route 10.57.1.0 255.255.255.0 10.29.29.1`
- `ip route 10.87.1.0 255.255.255.0 10.29.29.1`

  8. Scenario Requirements Analysis

| Requirement              | Configuration | Verification | Operational Test |

| Separate Newsroom traffic | VLAN 57 + access ports | `show vlan brief`, `show interfaces status` | Newsroom PC-1 -> PC-3 |

| Separate PostProduction traffic | VLAN 87 + access ports | `show vlan brief`, `show interfaces status` | PostProduction PC-2 -> PC-4 |

| Carry both functions to router | 802.1Q trunk | `show interfaces trunk` | Gateway pings |

| Route between VLANs locally | R1/R2 subinterfaces | `show ip interface brief` | PC -> other local gateway |

| Connect facilities | 10.29.29.0/30 routed link | `show ip interface brief`, `show ip route` | R1 -> R2 |

| Reach remote Newsroom network | Static route on both routers | `show ip route` | Newsroom 1 -> Newsroom 3 |

| Reach remote PostProduction network | Static route on both routers | `show ip route` | PostProduction 2 -> PostProduction 4 |

   9. Configuration Strategy
- `r1_config.py`: configures R1 subinterfaces, routed backbone and static routes.
- `r2_config.py`: configures R2 subinterfaces, routed backbone and static routes.
- `sw1_config.py`: creates VLANs, access ports and trunk on SW1.
- `sw2_config.py`: creates VLANs, access ports and trunk on SW2.

   10. Verification Strategy
Verification scripts collect evidence that the intended configuration exists:
- routers: interfaces, subinterfaces and static routes;
- switches: VLANs, access-port status, trunk state and MAC learning;
- integrated network: evidence from all four devices.

   11. Testing Strategy

| Source | Destination | Purpose | Expected Result |

| Newsroom-PC-1 | Newsroom-PC-3 | Verify Newsroom inter-facility operation | Successful ping |
| PostProduction-PC-2 | PostProduction-PC-4 | Verify PostProduction inter-facility operation | Successful ping |
| Newsroom-PC-1 | 10.87.1.1 | Verify local inter-VLAN routing | Successful ping |
| PostProduction-PC-2 | 10.57.1.1 | Verify local inter-VLAN routing | Successful ping |
| R1 | 10.29.29.2 | Verify routed backbone | Successful ping |
| R2 | 10.29.29.1 | Verify routed backbone | Successful ping |

   12. How to Run

a. Open the GNS3 project.
b. Start R1, R2, SW1, SW2 and all required end devices.
c. Confirm each GNS3 TELNET console port.
d. Update `host` and `port` in each Python script.
e. Install Netmiko:
   ```powershell
   pip install netmiko
   ```
f. Run configuration scripts in this order:
   ```powershell
   python r1_config.py
   python r2_config.py
   python sw1_config.py
   python sw2_config.py
   ```
g. Run device verification:
   ```powershell
   python r1_verify.py
   python r2_verify.py
   python sw1_verify.py
   python sw2_verify.py
   ```
h. Run device tests.
i. Run:
   ```powershell
   python network_verify.py
   python network_test.py
   ```
j. From the GNS3 PCs, perform the required end-to-end pings.

   13. Expected Results
- VLAN 57 exists as Newsroom on both switches.
- VLAN 87 exists as PostProduction on both switches.
- Gi0/0 trunks carry VLANs 57 and 87.
- Router subinterfaces are up/up with the correct gateway addresses.
- R1 and R2 can reach each other over 10.29.29.0/30.
- Static routes to the remote Newsroom and PostProduction networks appear in the routing table.
- Newsroom hosts can communicate between facilities.
- PostProduction hosts can communicate between facilities.

   14. Assumptions
The assignment guide specifies the VLANs, LAN networks, routed link and static-routing requirement, but it does not provide individual host addresses or a per-device port table for Assignment 29. Therefore this implementation uses:
- `.1` as each VLAN gateway;
- `.10` as the example end-device address;
- Gi0/0 on each router as the trunk-facing interface;
- Gi0/1 on each router as the R1–R2 routed interface;
- Gi0/1 on each switch as the trunk;
- Gi0/2 as VLAN 57 access;
- Gi0/3 as VLAN 87 access.

