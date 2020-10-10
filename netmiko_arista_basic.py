from netmiko import ConnectHandler
import getpass

password = getpass.getpass('Enter Arista1 Password:')

arista_device = {
    'device_type': 'arista_eos',
    'ip': '10.1.1.3',
    'username': 'admin',
    'password': password,
    'port': 22,
    'secret': password,
    'verbose': True
}

connection = ConnectHandler(** arista_device)
    
if not connection.check_enable_mode():
    connection.enable()

output = connection.send_command('show interface status')

print(output)

connection.disconnect()


    
