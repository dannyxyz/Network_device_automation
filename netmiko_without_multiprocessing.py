from netmiko import ConnectHandler
import time

def connect_and_run(device, cmd='show run'):
    print('Connecting to device: ', device['ip'])
    connection = ConnectHandler(**device)

    print('Entering enable mode....')
    connection.enable()

    print('Executing command:', cmd)
    output = connection.send_command(cmd)
    print(output)
    print('#' * 40)

if __name__ == '__main__':
    with open('devices1.txt') as f:
        devices = f.read().splitlines()

    device_list = list()

    for ip in devices:
        cisco_device = {
            'device_type': 'cisco_ios',
            'ip': ip,
            'username': 'danny',
            'password': 'cisco',
            'port': 22,
            'secret': 'cisco',
            'verbose': True

        }
        device_list.append(cisco_device)

    start = time.time()
    for device in device_list:
        connect_and_run(device, 'sh run')

    end = time.time()

    print('Script execution time', end - start)
