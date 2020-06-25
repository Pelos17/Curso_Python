from pprint import pprint
with open("C:/Users/a007e/code/Curso Python/show_ip_int_brief.txt") as f:
    show_ip = f.readlines()

Fe4 = show_ip[-2]
Fe4 = Fe4.split()
Fe4_Tuple = (Fe4[0], Fe4[1])
print(Fe4_Tuple)
