#Ejercicio 1
'''
Read the "show_vlan.txt" file into your program. 
Loop through the lines in this file and extract all of the VLAN_ID, VLAN_NAME combinations. 
From these VLAN_ID and VLAN_NAME construct a new list where each element in the list is a tuple consisting of (VLAN_ID, VLAN_NAME). 
Print this data structure to the screen. Your output should look as follows:

[('1', 'default'),
 ('400', 'blue400'),
 ('401', 'blue401'),
 ('402', 'blue402'),
 ('403', 'blue403')]
'''
#YO

#from pprint import pprint
#with open('/home/juanv/Escritorio/Code/learning_python/lesson3/show_vlan.txt') as f:
#    output = f.readlines()
#    lista= []
#    for line in output:
#        corte = line.split()
#        Vlan_Id = corte[0]
#        Vlan_Name = corte[1]
#        if Vlan_Id == 'Et6,' or Vlan_Id == 'Et7':
#            continue
#        else:
#            tuplas = (Vlan_Id, Vlan_Name)
#            lista = lista + [tuplas]
#pprint (lista[2:])

#PROFESOR

#from __future__ import unicode_literals, print_function
#from pprint import pprint

#vlan_list = []
#with open("/home/juanv/Escritorio/Code/learning_python/lesson3/show_vlan.txt") as f:
#    show_vlan = f.read()

#for line in show_vlan.splitlines():
    # Skip certain lines
#    if 'VLAN' in line or '-----' in line or line.startswith('  '):
#        continue
#    fields = line.split()
#    vlan_id = fields[0]
#    vlan_name = fields[1]
#    vlan_list.append((vlan_id, vlan_name))

#print()
#pprint(vlan_list)
#print()


#Ejercicio 2
'''
Read the contents of the "show_arp.txt" file. Using a for loop, iterate over the lines of this
file. Process the lines of the file and separate out the ip_addr and mac_addr for each entry into a
separate variable.

Add a conditional statement that searches for '10.220.88.1'. If 10.220.88.1 is found, print out the
string "Default gateway IP/Mac" and the corresponding IP address and MAC Address.

Using a conditional statement, also search for '10.220.88.30'. If this IP address is found, then
print out "Arista3 IP/Mac is" and the corresponding ip_addr and mac_addr.

Keep track of whether you have found both the Default Gateway and the Arista3 switch. Once you have
found both of these devices, 'break' out of the for loop.
'''
#YO
#with open("/home/juanv/Escritorio/Code/learning_python/lesson3/show_arp.txt") as f:
#    Arp = f.readlines()
#    Default_gateway = 0
#    Arista3 = 0
#    for lines in Arp:
#        if 'Protocol' in lines:
#            continue
#        else:
#            Arp_proc = lines.split()
#            ip_addr = Arp_proc[1]
#            mac_addr = Arp_proc[3]
#            if ip_addr == '10.220.88.1':
#                print ('Default gateway IP/Mac: {}/{}'.format(ip_addr, mac_addr))
#                Default_gateway = 1
#            elif ip_addr == '10.220.88.30':
#                print ('Arista3 IP/Mac is: {}/{}'.format(ip_addr, mac_addr))
#                Arista3 = 1
#            elif Default_gateway == 1 and Arista3 == 1:
#                print('Se encontro Default Gateway y Arista3')
#                break

#PROFESOR
#with open("/home/juanv/Escritorio/Code/learning_python/lesson3/show_arp.txt") as f:
#    show_arp = f.read()

#print()
#found1, found2 = (False, False)
#for line in show_arp.splitlines():
#    if 'protocol' in line.lower():
#        continue
#    fields = line.split()
#    ip_addr = fields[1]
#    mac_addr = fields[3]
#    if ip_addr == '10.220.88.1':
#        print("Default gateway IP/Mac is: {}/{}".format(ip_addr, mac_addr))
#        found1 = True
#    elif ip_addr == '10.220.88.30':
#        print("Arista3 IP/Mac is: {}/{}".format(ip_addr, mac_addr))
#        found2 = True

#    if found1 and found2:
#        print("Exiting...")
#        break

#print()

#Ejercicio3
'''
Read the 'show_lldp_neighbors_detail.txt' file. Loop over the lines of this file. 
Keep reading the lines until you have encountered the remote "System Name" and remote "Port id". 
Save these two items into variables and print them to the screen. 
You should extract only the system name and port id from the lines (i.e. your variables should only have 'twb-sf-hpsw1' and '15'). 
Break out of your loop once you have retrieved these two items.
'''
#YO
#with open("/home/juanv/Escritorio/Code/learning_python/lesson3/show_lldp_neighbors_detail.txt") as f:
#    output = f.readlines()
#while True:
#    for vecinos in output:
#        if 'Port id:' in vecinos:
#            Port_Id = vecinos.split()[-1]
#        elif 'System Name:' in vecinos:
#            System_Name = vecinos.split()[-1]
#    print('Port ID:{} / System Name: {}'.format(Port_Id, System_Name))
#    break

#PROFE
#with open("/home/juanv/Escritorio/Code/learning_python/lesson3/show_lldp_neighbors_detail.txt") as f:
#    show_lldp = f.read()

#system_name, port_id = (None, None)
#for line in show_lldp.splitlines():
#    if 'System Name: ' in line:
#        _, system_name = line.split('System Name: ')
#    elif 'Port id: ' in line:
#        _, port_id = line.split('Port id: ')

#    if port_id and system_name:
#        break

#print()
#print("System Name: {}".format(system_name))
#print("Port ID: {}".format(port_id))
#print()
'''
You have the following data structure:

arp_table = [('10.220.88.1', '0062.ec29.70fe'),
 ('10.220.88.20', 'c89c.1dea.0eb6'),
 ('10.220.88.21', '1c6a.7aaf.576c'),
 ('10.220.88.28', '5254.aba8.9aea'),
 ('10.220.88.29', '5254.abbe.5b7b'),
 ('10.220.88.30', '5254.ab71.e119'),
 ('10.220.88.32', '5254.abc7.26aa'),
 ('10.220.88.33', '5254.ab3a.8d26'),
 ('10.220.88.35', '5254.abfb.af12'),
 ('10.220.88.37', '0001.00ff.0001'),
 ('10.220.88.38', '0002.00ff.0001'),
 ('10.220.88.39', '6464.9be8.08c8'),
 ('10.220.88.40', '001c.c4bf.826a'),
 ('10.220.88.41', '001b.7873.5634')] 


Loop over this data structure and extract all of the MAC addresses. 
Process all of the MAC addresses to get them into a standard format. 
Print all of the new standardized MAC address to the screen. 
The standardized format should be as follows:

00:62:EC:29:70:FE

The hex digits should be capitalized. 
Additionally, there should be a colon between each octet in the MAC address.
'''

#arp_table = [('10.220.88.1', '0062.ec29.70fe'),
# ('10.220.88.20', 'c89c.1dea.0eb6'),
# ('10.220.88.21', '1c6a.7aaf.576c'),
# ('10.220.88.28', '5254.aba8.9aea'),
# ('10.220.88.29', '5254.abbe.5b7b'),
# ('10.220.88.30', '5254.ab71.e119'),
# ('10.220.88.32', '5254.abc7.26aa'),
# ('10.220.88.33', '5254.ab3a.8d26'),
# ('10.220.88.35', '5254.abfb.af12'),
# ('10.220.88.37', '0001.00ff.0001'),
# ('10.220.88.38', '0002.00ff.0001'),
# ('10.220.88.39', '6464.9be8.08c8'),
# ('10.220.88.40', '001c.c4bf.826a'),
# ('10.220.88.41', '001b.7873.5634')]

#for ip_addr, mac_addr in arp_table:
#    mac = (mac_addr.split("."))
#    mac = "".join(mac)
#    mac = mac.upper()

#    new_mac = []
#    while len(mac) > 0:
#        entrada = mac[:2]
#        mac = mac [2:]
#        new_mac.append(entrada)
    
#    new_mac = ":".join(new_mac)
#    print (new_mac)
    


#PROFE

#print()
#for ip_addr, mac_addr in arp_table:
    # Eliminate the period and convert to upper case
#    mac_addr = mac_addr.split(".")
#    mac_addr = "".join(mac_addr)
#    mac_addr = mac_addr.upper()

    # Process two hex digits at a time
#    new_mac = []
#    while len(mac_addr) > 0:
#        entry = mac_addr[:2]
#        mac_addr = mac_addr[2:]
#        new_mac.append(entry)

    # Reunite MAC address using a colon
#    new_mac = ":".join(new_mac)
#    print(new_mac)
#print()


#Ejercicio 5
'''
[Optional/bonus] 

*** Note, to actually test this in your environment, change the test IP addresses to something in your environment that you can ping successfully. ***

Construct a list of 254 IP addresses. The base IP address should be equal to '10.10.100.0' or '10.10.100.'.

You should use the 'range' builtin to accomplish this.

Your list should have all of the IP addresses from 10.10.100.1 to 10.10.100.254.

Use Python's 'enumerate' to print out all of the IP addresses and their corresponding list index. The output should look similar to the following: 

0 ---> 10.10.100.1
1 ---> 10.10.100.2
2 ---> 10.10.100.3
3 ---> 10.10.100.4
4 ---> 10.10.100.5
...


Use a list slice to create a new list that goes from 10.10.100.3 to 10.10.100.6.

Using a loop and os.system("ping -c 3 10.10.100.3") try pinging all of the IP addresses in this short list. 
For Windows the command will probably be os.system("ping -n 3 10.10.100.3").

Put a variable at the top to define whether you are using Windows or Linux/MacOs. This should be similar to the following:

WINDOWS = False

base_cmd_linux = 'ping -c 2'
base_cmd_windows = 'ping -n 2'
# Ternary operator
base_cmd = base_cmd_windows if WINDOWS else base_cmd_linux
'''
#YO

#import os 

#rangos = list(range(1,255))
#ip_addr = []
#for rango in rangos:
#    ip = '192.168.0.' + str(rango)
#    ip_addr.append(ip)

#for ip_index in enumerate(ip_addr):
#    i, ip_dir = ip_index
#    print ('{} ---> {}'.format(i, ip_dir))

#direcciones = [ip_addr[200:201]]

#WINDOWS = True
#base_cmd_linux = 'ping -c 2'
#base_cmd_windows = 'ping -n 2'
# Ternary operator
#base_cmd = base_cmd_windows if WINDOWS else base_cmd_linux

#for direccion in direcciones:
    # cmd = base_cmd + ' ' + direccion
    # os.system(cmd)

#PROFE

#import os

# Toggle this to use Windows
#WINDOWS = False

#base_ip = '10.10.100.'
#base_cmd_linux = 'ping -c 2'
#base_cmd_windows = 'ping -n 2'
# Ternary operator
#base_cmd = base_cmd_windows if WINDOWS else base_cmd_linux

#ip_list = []
#for last_octet in range(1, 255):
#    new_ip = base_ip + str(last_octet)
#    ip_list.append(new_ip)

#for i, ip_addr in enumerate(ip_list):
#    print("{} ---> {}".format(i, ip_addr))

# Only use IP addresses 8.8.4.3 to 8.8.4.6
#ip_list = ip_list[2:6]

#print()
#print('-' * 80)
#for ip_addr in ip_list:
#    print("IP Addr: ", ip_addr)
#    return_code = os.system("{} {}".format(base_cmd, ip_addr))
#    print('-' * 80)
#print('-' * 80)
#print()