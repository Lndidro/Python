#1
print('Exercise 1:')
NAT = 'ip nat inside source list ACL interface FastEthernet0/1 overload'
print (NAT.replace('Fast', 'Gigabit'),'\n')

#2
print('Exercise 2:')
MAC = 'AAAA:BBBB:CCCC'
print (MAC.replace(':','.'),'\n')

#3
print('Exercise 3:')
CONFIG = 'switchport trunk allowed vlan 1,3,10,20,30,100'
print(CONFIG.split()[4].split(','),'\n')

#4
print('Exercise 4:')
command1 = 'switchport trunk allowed vlan 1,3,10,20,30,100'
command2 = 'switchport trunk allowed vlan 1,3,100,200,300'
command1 = set(command1.split()[4].split(','))
command2 = set(command2.split()[4].split(','))
print(list(command1.intersection(command2)),'\n')

#5
print('Exercise 5:')
VLANS = [10, 20, 30, 1, 2, 100, 10, 30, 3, 4, 10]
VLANS = list(set(VLANS))
VLANS.sort()
print(VLANS,'\n')

#6
print('Exercise 6:')
ospf_route = 'O            10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
l = ospf_route.split()
dict = {
        "Protocol": "OSPF",
        "Prefix": l[1],
        "AD/Metric": l[2][1:-1],
        "Next-Hop": l[4][:-1],
        "Last update": l[5][:-1],
        "Outbound Inteface": l[6]
}
for key, value in dict.items():
    print("{0:20}\t{1}".format(key+':',value))
    
#7
print('\nExercise 7:')
MAC = 'AAAA:BBBB:CCCC'
MAC = bin(int(''.join(MAC.split(':')), 16))
print(MAC,'\n')

#8
print('Exercise 8:')
IP = '192.168.3.1'
IP = IP.split('.')
for item in IP:
    print('{:<10}'.format( int(item) ), end='')
print()
for item in IP:
    print('{:<10b}'.format( int(item) ), end='')
    
#9
print('\n\nExercise 9:')
str = [10, 2, 30, 100, 10, 50, 11, 30, 15, 7]
string = ['diamond', 'ruby', 'perl', 'ruby', 'emerald', 'diamond', 'ruby', 'perl']
a = 10
b = 'ruby'
print(len(str) - 1 - str[::-1].index(a))
print(len(string) - 1 - string[::-1].index(b))