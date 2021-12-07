#1.1
print('Exercise 1.1:')
ip = input('Enter IP in the form of 10.0.1.1: ')
fb = ip.split('.')[0]

if (1 <= int(fb)<= 223):
    print('unicast')
elif (224 <= int(fb) <= 239):
    print('multicast')
elif (ip == '255.255.255.255'):
    print('local broadcast')
elif (ip == '0.0.0.0'):
    print('unassigned')
else:
    print('unused')
    
#1.2
print('\nExercise 1.2:')
ip = input('Enter IP in the form of 10.0.1.1: ')

try:
    1 / (len(ip.split('.')) == 4)
    for byte in ip.split('.'):
       1 / (0 <= int(byte) <= 255)
except ZeroDivisionError:
    print('Incorrect IPv4 address')
else:
    fb = ip.split('.')[0]
    if (1 <= int(fb)<= 223):
        print('unicast')
    elif (224 <= int(fb) <= 239):
        print('multicast')
    elif (ip == '255.255.255.255'):
        print('local broadcast')
    elif (ip == '0.0.0.0'):
        print('unassigned')
    else:
        print('unused')
        
#1.3
print('\nExercise 1.3:')
while True:
    ip = input('Enter IP in the form of 10.0.1.1: ')
    try:
        1 / (len(ip.split('.')) == 4)
        for byte in ip.split('.'):
            1 / (0 <= int(byte) <= 255)
    except ZeroDivisionError:
        print('Incorrect IPv4 address')
    else:
        break

fb = ip.split('.')[0]
if (1 <= int(fb)<= 223):
    print('unicast')
elif (224 <= int(fb) <= 239):
    print('multicast')
elif (ip == '255.255.255.255'):
    print('local broadcast')
elif (ip == '0.0.0.0'):
    print('unassigned')
else:
    print('unused')
    
#2
print('\nExercise 2:')
mac = ['aabb:cc80:7000', 'aabb:dd80:7340', 'aabb:ee80:7000', 'aabb:ff80:7000']
mac_cisco = []

for mac_addr in mac:
    mac_cisco.append('.'.join(mac_addr.split(':')))

print(mac_cisco,'\n')

#3
print('Exercise 3:')
#access_template = ['switchport mode access',
#                    'switchport access vlan',
#                    'spanning-tree portfast',
#                    'spanning-tree bpduguard enable']

trunk_template = ['switchport trunk encapsulation dot1q',
                    'switchport mode trunk',
                    'switchport trunk allowed vlan']

fast_int = {'access':{'0/12':'10','0/14':'11','0/16':'17','0/17':'150'},
            'trunk':{'0/1':['add','10','20'],
                    '0/2':['only','11','30'],
                    '0/4':['del','17']} }

#for intf, vlan in fast_int['access'].items():
#    print('interface FastEthernet' + intf)
#    for command in access_template:
#        if command.endswith('access vlan'):
#            print(' {} {}'.format(command, vlan))
#        else:
#            print(' {}'.format(command))

for intf, vlan in fast_int['trunk'].items():
    print('interface FastEthernet' + intf)
    for command in trunk_template:
        if (command.endswith('vlan')):
            if (vlan[0] == 'add'):
                print(' {} add '.format(command), end='')
            elif (vlan[0] == 'del'):
                print(' {} remove '.format(command), end='')
            elif (vlan[0] == 'only'):
                print(' {} '.format(command), end='')
            print(','.join(vlan[1:]))
        else:
            print(' {}'.format(command))