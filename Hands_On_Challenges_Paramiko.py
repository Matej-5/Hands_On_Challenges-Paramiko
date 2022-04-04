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


# import paramiko
# #import getpass
# import time
#
# ssh_client = paramiko.SSHClient()
# ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#
# #print('Connecting to client')
# #my_password = getpass.getpass('Enter your password:')
#
# router = {'hostname': '10.1.1.10', 'port' :  '22', 'username': 'u1', 'password': 'cisco', 'look_for_keys': False, 'allow_agent': False}
# print(f'Connection to {router ["hostname"]}')
# ssh_client.connect(**router)
#
# shell = ssh_client.invoke_shell()
# shell.send('show users\n')
# time.sleep(1)
#
# output = shell.recv(10000).decode()
# print(output)
#
# if ssh_client.get_transport().is_active():
#     print('Closing connection')
#     ssh_client.close()


# import paramiko
# import time
#
# ssh_client = paramiko.SSHClient()
# ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh_client.connect(hostname='10.1.1.10', port= '22', username='u1', password='cisco', look_for_keys=False, allow_agent=False)
#
# shell = ssh_client.invoke_shell()
# shell.send('enable\n')
# shell.send('cisco\n')
# shell.send('terminal length 0\n')
# shell.send('show running-config\n')
# time.sleep(1)
#
# output = shell.recv(100000).decode()
#
# with open('Outputs_2.txt', 'w') as f:
#     f.write(output)
#
# if ssh_client.get_transport().is_active():
#     print('Closing connection')
#     ssh_client.close()

# import paramiko
# import time
#
#
# ssh_client = paramiko.SSHClient()
# ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#
# ssh_client.connect(hostname='10.1.1.10', port='22', username='u1', password='cisco',
#                    look_for_keys=False, allow_agent=False)
#
# shell = ssh_client.invoke_shell()
#
# commands = ['enable', 'cisco', 'conf t', 'username admin1 secret cisco', 'access-list 1 permit any', 'end',
#             'terminal length 0',  'sh run | i user']
#
# for cmd in commands:
#     shell.send(f'{cmd}\n')
#     time.sleep(0.5)
#
# output = shell.recv(100000)
# output = output.decode()
# print(output)
#
#
# if ssh_client.get_transport().is_active():
#     ssh_client.close()



import paramiko
import time


def connect (server_ip, server_port, user, passwd):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=server_ip, port=server_port, username=user, password=passwd, look_for_keys=False, allow_agent=False)

    return ssh_client

def get_shell (ssh_client):
    shell = ssh_client.invoke_shell()
    return shell

def send_command(shell, command, timeout=1):
    shell.send(command + '\n')
    time.sleep(timeout)

def show(shell, n=10000):
    output = shell.recv(n)
    return output.decode()

def close(ssh_client):
    if ssh_client.get_transport().is_active() == True:
        ssh_client.close()

if __name__ == '__main__':
    router1 = {'server_ip': '10.1.1.10', 'server_port': '22', 'user': 'u1', 'passwd':'cisco'}
    client = connect (**router1)
    shell = get_shell(client)

    send_command(shell, 'enable')
    send_command(shell, 'cisco')
    send_command(shell, 'term len 0')
    send_command(shell, 'sh version')
    send_command(shell, 'sh ip int brief')

    output = show(shell)
    print(output)












