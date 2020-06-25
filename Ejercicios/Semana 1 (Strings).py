#!/usr/bin/env python

# Ejercicio 1
'''
1. Create a Python script that has three variables: ip_addr1, ip_addr2, ip_addr3 (representing three corresponding IP addresses). Print these three variables to standard output using a single print statement.

Make your print statement compatible with both Python2 and Python3.

If you are using either Linux or MacOS make your program executable by adding a shebang line and by changing the files permissions (i.e. chmod 755 exercise1.py).
'''
# ip_addr1 = "192.168.1.1"
#ip_addr2 = "192.168.1.2"
#ip_addr3 = "192.168.1.3"

#print(ip_addr1, ip_addr2, ip_addr3)

#-------------------------------------------------

# Ejercicio 2
'''
2. Prompt a user to enter in an IP address from standard input. Read the IP address in and break it up into its octets. Print out the octets in decimal, binary, and hex.

Your program output should look like the following:

​ $ python exercise2.py 
Please enter an IP address: 80.98.100.240

    Octet1         Octet2         Octet3         Octet4     
------------------------------------------------------------
      80             98             100            240      
   0b1010000      0b1100010      0b1100100     0b11110000   
     0x50           0x62           0x64           0xf0      
------------------------------------------------------------


Four columns, fifteen characters wide, a header column, data centered in the column.
'''
#ip_addr1 = input('Ingrese la IP: ')

#octets = ip_addr1.split('.')

#print ('{:^15}{:^15}{:^15}{:^15}'.format('Octet1', 'Octet2', 'Octet3', 'Octet4;',))
#print('-' * 60)
#print ('{:^15}{:^15}{:^15}{:^15}'.format(*octets))
#print ('{:^15}{:^15}{:^15}{:^15}'.format(bin(int(octets[0])), bin(int(octets[1])), bin(int(octets[2])), bin(int(octets[3]))))
#print ('{:^15}{:^15}{:^15}{:^15}'.format(hex(int(octets[0])), hex(int(octets[1])), hex(int(octets[2])), hex(int(octets[3]))))
#print('-' * 60)

#-------------------------------------------------

# Ejercicio 3
'''
3.   Create three different variables the first variable should use all lower case characters with underscore ( _ ) as the word separator. The second variable should use all upper case characters with underscore as the word separator. The third variable should use numbers, letters, and underscore, but still be a valid variable Python variable name.

Make all three variables be strings that refer to IPv6 addresses.

Use the from future technique so that any string literals in Python2 are unicode.

compare if variable1 equals variable2
compare if variable1 is not equal to variable3
'''
#YO
#ip_addr1 = 'aaaa_bbbb_cccc_dddd_eeee_ffff_gggg_hhhh'
#ip_addr2 = ip_addr1.upper()
#ip_addr3 = '1A1a_2b2B_3C3c_4d4d_5E5e_6F6F_7g7G_8H8h'

#print(ip_addr1)
#print(ip_addr2)
#print(ip_addr3)
#print(ip_addr1 == ip_addr2)
#print(ip_addr1 != ip_addr3)

# Profe

#from __future__ import unicode_literals

#ipv6_addr1 = "2001:db8:1234::1"
#IPV6_ADDR2 = "2001:db8:1234::2"
#ipV6_addR3 = "2001:db8:1234::3"

#print("")
#print("Is variable1 equal to variable2: {}".format(ipv6_addr1 == IPV6_ADDR2))
#print("Is variable1 not equal to variable3: {}".format(ipv6_addr1 != ipV6_addR3))
#print("")

#-------------------------------------------------

# Ejercicio 4
'''
4. Create a show_version variable that contains the following

 show_version = "*0        CISCO881-SEC-K9       FTX0000038X    " 


Remove all leading and trailing whitespace from the string.

Split the string and extract the model and serial_number from it.

Check if 'Cisco' is contained in the model string (ignore capitalization).

Check if '881' is in the model string.

Print out both the serial number and the model.
'''
#YO
#show_version = "*0        CISCO881-SEC-K9       FTX0000038X    " 

#sin_esp = show_version.strip()
#corte = sin_esp.split()
#modelo = corte[1]
#serial = corte[2]

#print('Modelo: {}, Serial Number: {}'.format(modelo, serial))

#print('cisco' in modelo.lower())

#print('881' in modelo)

#Profe


#show_version = "*0  	  CISCO881-SEC-K9       FTX0000038X    "
#show_version = show_version.strip()

#fields = show_version.split()
#model = fields[1]
#serial_number = fields[2]

#print()
#vendor_cisco = 'cisco' in model.lower()
#print("Checking if model contains Cisco: {}".format(vendor_cisco))

#model_881 = '881' in model
#print("Checking if model contains 881: {}".format(model_881))

#print("Serial Number: {}".format(serial_number))
#print("Model: {}".format(model))
#print()

#-------------------------------------------------

# Ejercicio 5
'''
5. You have the following three variables from the arp table of a router:

mac1 = "Internet  10.220.88.29           94   5254.abbe.5b7b  ARPA   FastEthernet4"
mac2 = "Internet  10.220.88.30            3   5254.ab71.e119  ARPA   FastEthernet4"
mac3 = "Internet  10.220.88.32          231   5254.abc7.26aa  ARPA   FastEthernet4"

Process these ARP entries and print out a table of "IP ADDR" to "MAC ADDRESS" mappings. The output should look like following:

             IP ADDR          MAC ADDRESS
-------------------- --------------------
        10.220.88.29       5254.abbe.5b7b
        10.220.88.30       5254.ab71.e119
        10.220.88.32       5254.abc7.26aa


Two columns, 20 characters wide, data right aligned, a header column.
'''
#YO
#mac1 = "Internet  10.220.88.29           94   5254.abbe.5b7b  ARPA   FastEthernet4"
#mac2 = "Internet  10.220.88.30            3   5254.ab71.e119  ARPA   FastEthernet4"
##mac3 = "Internet  10.220.88.32          231   5254.abc7.26aa  ARPA   FastEthernet4"

#mac1_edit = mac1.split()
#mac2_edit = mac2.split()
#mac3_edit = mac3.split()

#print('{:>20}{:>20}'.format('IP ADDR', 'MAC ADDRESS'))
#print('{} {}'.format('-'*20, '-'*20))
#print ('{:>20}{:>20}'.format(mac1_edit[1], mac1_edit[3]))
#print ('{:>20}{:>20}'.format(mac2_edit[1], mac2_edit[3]))
#print ('{:>20}{:>20}'.format(mac2_edit[1], mac3_edit[3]))

#Profe

#from __future__ import print_function, unicode_literals

#mac1 = "Internet  10.220.88.29           94   5254.abbe.5b7b  ARPA   FastEthernet4"
#mac2 = "Internet  10.220.88.30            3   5254.ab71.e119  ARPA   FastEthernet4"
#mac3 = "Internet  10.220.88.32          231   5254.abc7.26aa  ARPA   FastEthernet4"

# After we talk about loops, a for-loop would be a better solution here.
#fields = mac1.split()
#ip_addr1 = fields[1]
#mac1 = fields[3]

#fields = mac2.split()
#ip_addr2 = fields[1]
#mac2 = fields[3]

#fields = mac3.split()
#ip_addr3 = fields[1]
#mac3 = fields[3]

#print()
#print("{:>20} {:>20}".format("IP ADDR", "MAC ADDRESS"))
#print("{:>20} {:>20}".format("-" * 20, "-" * 20))
#print("{:>20} {:>20}".format(ip_addr1, mac1))
#print("{:>20} {:>20}".format(ip_addr2, mac2))
##print("{:>20} {:>20}".format(ip_addr3, mac3))
#print()
