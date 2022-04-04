from netmiko import ConnectHandler

cisco_device = {
    'device_type': 'cisco_ios',
    'host': '10.1.1.10',
    'username': 'u1',
    'password': 'cisco',
    'port': '22',
    'verbose': True
}

connection = ConnectHandler(**cisco_device)
output = connection.send_command('show arp')
print(output)

