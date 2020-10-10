from netmiko import ConnectHandler

cisco_device = {
    'device_type': 'cisco_ios',
    'ip': '192.168.136.2',
    'username': 'danny',
    'password': 'cisco',
    'port': 22,
    'secret': 'cisco',
    'verbose': True
}

net_connect = ConnectHandler(**cisco_device)
prompter = net_connect.find_prompt()
if '>' in prompter:
    net_connect.enable()

interface = input('Enter the interface you want to enable: ')
output = net_connect.send_command('sh ip interface ' + interface)

if 'Invalid input detected' in output:
    print('You entered an invalid interface')

else:
    first_line = output.splitlines()[0]
    print(first_line)
    if not 'up' in first_line:
        print('The interface is down. Enabling the interface')
        commands = ['interface ' + interface, ' no shut', 'exit' ]
        output = net_connect.send_config_set(commands)
        print(output)
        print('#' * 40)
        print('The interface has been enabled')
    else:
        print('Interface ' + interface +  ' is already enabled')



    
