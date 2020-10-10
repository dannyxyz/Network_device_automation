from netmiko import ConnectHandler

with open('devices.txt') as f:
    devices = f.read().splitlines()

for ip in devices:

    cisco_device = {
        'device_type': 'cisco_ios',
        'ip': ip,
        'username': 'danny',
        'password': 'cisco',
        'port': '22',
        'secret': 'cisco',
        'verbose': 'True'
    }

    print('connecting to' + ' '  +  ip)
    connection = ConnectHandler(**cisco_device)

    print('Entering enable mode.....')
    connection.enable()

    output = connection.send_command('sh run')
    # print(output)

    prompt = connection.find_prompt()
    hostname = prompt[:-1]
    # print(hostname)

    import datetime

    now = datetime.datetime.now()
    today = str(now.year) + '-' + str(now.month) + '-' + str(now.day)
    file = today + '-' + hostname + '.txt'

    with open(file , 'r') as backup:
        backup.write(output)
        print('Backup of ' + hostname+ ' ' + 'completed successfully')
        print('#' * 30)

    connection.disconnect()