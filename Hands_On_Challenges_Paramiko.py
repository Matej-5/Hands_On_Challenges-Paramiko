# from netmiko import ConnectHandler
#
# cisco_device = {
#     'device_type': 'cisco_ios',
#     'host': '10.1.1.10',
#     'username': 'u1',
#     'password': 'cisco',
#     'port': '22',
#     'verbose': True
# }
#
# connection = ConnectHandler(**cisco_device)
# output = connection.send_command('show arp')
# print(output)


import paramiko
#import getpass
import time

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#print('Connecting to client')
#my_password = getpass.getpass('Enter your password:')

router = {'hostname': '10.1.1.10', 'port' :  '22', 'username': 'u1', 'password': 'cisco', 'look_for_keys': False, 'allow_agent': False}
print(f'Connection to {router ["hostname"]}')
ssh_client.connect(**router)

shell = ssh_client.invoke_shell()
shell.send('show users\n')
time.sleep(1)

output = shell.recv(10000).decode()
print(output)

if ssh_client.get_transport().is_active():
    print('Closing connection')
    ssh_client.close()













