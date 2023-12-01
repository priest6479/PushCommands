from netmiko import ConnectHandler
from netmiko import ConnectHandler, SSHDetect, NetmikoTimeoutException, NetmikoAuthenticationException
import getpass

#Obtain Username
username = input("Please enter your Username:")

# Obtain Password
password=getpass.getpass(prompt="Please enter your Password:")

# Define the netmiko parameters for SSH connection
netmiko_params = {
    "device_type": "cisco_ios_telnet",
    "username": username,
    "password": password,
    "global_delay_factor": 2,
}


# Define the filename for the devices file
devices_filename = "devices.txt"


# Open the devices file and read the list of devices
with open(devices_filename, "r") as devices_file:
    devices_list = devices_file.read().splitlines()

# Iterate over each device in the devices list
for device in devices_list:
    print("Connecting to device:", device)

    # Add the IP address or hostname to the netmiko parameters
    netmiko_params["ip"] = device

    try:
        # Connect to the device using netmiko
        net_connect = ConnectHandler(**netmiko_params)

        # Enter enable mode
        net_connect.enable()

        # Send the list of commands to the device
        output = net_connect.send_config_from_file('commands.txt')
        output += net_connect.save_config()

        # Print the output from the device
        print(output)

        # Disconnect from the device
        net_connect.disconnect()

    except (NetmikoAuthenticationException, NetmikoTimeoutException) as e:
        print("Failed to connect to", device, ":", e)
