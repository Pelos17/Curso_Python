#Ejercicio 1
''' 1. Open the "show_version.txt" file for reading. Use the .read() method to read in the entire file contents to a variable. Print out the file contents to the screen. Also print out the type of the variable (you should have a string at this point).

Close the file.

Open the file a second time using a Python context manager (with statement). Read in the file contents using the .readlines() method. Print out the file contents to the screen. Also print out the type of the variable (you should have a list at this point).
'''

#f = open('C:/Users/a007e/code/Curso Python/show_version.txt')

#Parte 1
#output = f.read()
#f.close()

#print(output)
#print(type(output))

# Parte 2
#output = f.readlines()

#print (output)
#print((type(output)))


#Ejercicio 2
''' 
2. Create a list of five IP addresses.

Use the .append() method to add an IP address onto the end of the list. Use the .extend() method to add two more IP addresses to the end of the list.

Use list concatenation to add two more IP addresses to the end of the list.

Print out the entire list of ip addresses. Print out the first IP address in the list. Print out the last IP address in the list.

Using the .pop() method to remove the first IP address in the list and the last IP address in the list.

Update the new first IP address in the list to be '2.2.2.2'. Print out the new first IP address in the list.

'''
#ip = ['192.168.1.1','192.168.1.2','192.168.1.3','192.168.1.4']
#ip2 = ['192.168.1.8','192.168.1.9']
#ip.append('192.168.1.5')
#ip.extend(['192.168.1.6','192.168.1.7'])
#ip = ip + ip2 # o puede ser ip = ip + ['192.168.1.8','192.168.1.9']

#print(ip)
#print(ip[0])
#print(ip[-1])

#ip.pop(0)
#ip.pop(-1)
#print (ip)

#ip.insert(0, '2.2.2.2')
#print(ip)


#Ejercicio 3
'''
3. Read in the "show_arp.txt" file using the readlines() method. Use a list slice to remove the header line.

Use pretty print to print out the resulting list to the screen, syntax is: 

from pprint import pprint
pprint(some_var)

Use the list .sort() method to sort the list based on IP addresses.

Create a new list slice that is only the first three ARP entries.

Use the .join() method to join these first three ARP entries back together as a single string using the newline character ('\n') as the separator.

Write this string containing the three ARP entries out to a file named "arp_entries.txt".
'''
#YO

#from pprint import pprint
#f = open('C:/Users/a007e/code/Curso Python/show_arp.txt')

#arp_output = f.readlines()

#pprint(arp_output[1:])

#new_arp = arp_output.sort()
#pprint (new_arp)

#new_arp_list = arp_output[1:4]

#pprint(new_arp_list)

#joined = '\n'.join(new_arp_list)

#print (joined)

#w_arp = open('C:/Users/a007e/code/Curso Python/arp_entries.txt', mode='w')
#w_arp.write(joined)
#w_arp.flush()
#w_arp.close()

#PROFE

#from __future__ import print_function, unicode_literals
#from pprint import pprint

#with open("show_arp.txt") as f:
#    show_arp = f.readlines()

# Remove header line
#show_arp = show_arp[1:]
#pprint(show_arp)

#show_arp.sort()
# Grab only the first three entries
#my_entries = show_arp[:3]
#my_entries = '\n'.join(my_entries)

#with open("arp_entries.txt", "wt") as f:
#    f.write(my_entries)


#Ejercicio 4
'''
Read in the "show_ip_int_brief.txt" file into your program using the .readlines() method.

Obtain the list entry associated with the FastE;thernet4 interface. You can just hard-code the index at this point since we haven't covered for-loops or regular expressions. Use the string .split() method to obtain both the IP address and the corresponding interface associated with the IP.

Create a two element tuple from the result (intf_name, ip_address).

Print that tuple to the screen.

Use pycodestyle on this script. Get the warnings/errors to zero. You might need to 'pip install pycodestyle' on your computer (you should be able to type this from the shell prompt). Alternatively, you can type 'python -m pip install pycodestyle'.
'''
#YO
#from pprint import pprint
#with open("C:/Users/a007e/code/Curso Python/show_ip_int_brief.txt") as f:
#    show_ip = f.readlines()

#Fe4 = show_ip[-2]
#Fe4 = Fe4.split()
#Fe4_Tuple = (Fe4[0], Fe4[1])
#print(Fe4_Tuple)

#PROFE
#with open("C:/Users/a007e/code/Curso Python/show_ip_int_brief.txt") as f:
#    show_ip_int_brief = f.readlines()

#fa4_ip = show_ip_int_brief[5].strip()
#fields = fa4_ip.split()
#intf = fields[0]
#ip_address = fields[1]

#my_results = (intf, ip_address)
#print(my_results)


#Ejercicio 5
'''
Read the 'show_ip_bgp_summ.txt' file into your program. From this BGP output obtain the first and last lines of the output.

From the first line use the string .split() method to obtain the local AS number.

From the last line use the string .split() method to obtain the BGP peer IP address.

Print both local AS number and the BGP peer IP address to the screen.
'''
#YO
#with open("C:/Users/a007e/code/Curso Python/Archivos/show_ip_bgp_summ.txt") as f:
#    ip_bgp_summ = f.readlines()

#first_line = ip_bgp_summ[0]
#last_line = ip_bgp_summ[-1]

#As_Number = first_line.split()
#Bgp_Ip = last_line.split()

#print ('{}''\n''{}'.format(As_Number[-1], Bgp_Ip[0]))

#PROFE

#with open("C:/Users/a007e/code/Curso Python/Archivos/show_ip_bgp_summ.txt") as f:
#    bgp_summ = f.read()

#bgp_summ = bgp_summ.splitlines()

#first_line = bgp_summ[0]
#as_number = first_line.split()[-1]
#print("Local AS Number: {}".format(as_number))

#last_line = bgp_summ[-1]
#peer_ip = last_line.split()[0]
#print("BGP Peer IP Address: {}".format(peer_ip))