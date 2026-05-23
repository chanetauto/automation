ansible all -i 192.168.0.40, -c ansible.netcommon.network_cli -u admin -k -m cisco.ios.ios_facts -e ansible_network_os=cisco.ios.ios

ansible all -i 192.168.0.41, -c ansible.netcommon.network_cli -u admin -k -m cisco.ios.ios_command -e ansible_network_os=cisco.ios.ios -a "commands='show ip int brief'"
