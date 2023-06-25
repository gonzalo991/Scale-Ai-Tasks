import os

def configure_network_interfaces():
    # Open the network interfaces file in write mode
    with open('/etc/network/interfaces', 'w') as f:
        # Write the desired network configuration
        f.write('auto eth0\n')
        f.write('iface eth0 inet static\n')
        f.write('address 192.168.1.100\n')
        f.write('netmask 255.255.255.0\n')
        f.write('gateway 192.168.1.1\n')
        f.write('dns-nameservers 8.8.8.8\n')

    # Restart the networking service to apply the changes
    os.system('sudo systemctl restart networking.service')

# Call the function to configure the network interfaces
configure_network_interfaces()
