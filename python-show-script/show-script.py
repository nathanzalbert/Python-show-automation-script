from netmiko import ConnectHandler
from getpass import getpass

# Device information
device = {
    "device_type": "cisco_ios",
    "host": "192.168.1.1",
    "username": input("Username: "),
    "password": getpass("Password: "),
}

# Connect to the device
connection = ConnectHandler(**device)

# Commands to run
commands = [
    "show ip interface brief",
    "show ip route",
    "show version"
]

# Run commands and save output
with open("network_report.txt", "w") as file:
    for command in commands:
        output = connection.send_command(command)
        file.write(f"\n--- {command} ---\n")
        file.write(output)

# Disconnect
connection.disconnect()

print("Done! Results saved to network_report.txt")