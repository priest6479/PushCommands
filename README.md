# PushCommands
This script was designed to push network changes out Cisco Devices. 

There are times you just need to push a configuration out to alot of network devices (ACl's, Prefix-lists, SNMP strings...etc)
I wrote this script to serve just that purpose. 

To execute this script, Update the "Commands.txt" file with the commands you want to apply. 
Update the "devices.txt" with the Ip or Hostname of the devices you want to apply them on

There are two versions of this script, one for Telnet and one for SSH

(This is meant for Cisco Devices)
(This script runs Python, Netmiko and Getpass)
