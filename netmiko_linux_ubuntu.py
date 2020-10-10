from netmiko import ConnectHandler

linux = {
    'device_type': 'linux',
    'ip': '192.168.95.104',
    'username': 'ubuntu',
    'password': 'ubuntu',
    'port': '22',
    'secret': 'ubuntu',
    'verbose': 'True'
}

connection = ConnectHandler(**linux)

connection.enable()

output = connection.send_command('apt-get update && apt-get -y install apache2')
print(output)

connection.disconnect()

