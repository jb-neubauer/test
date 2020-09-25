#To get pip3 installed use apt install python3-pip
#port scanner, use PIP3install to get the ipy library

import socket
from IPy import IP

def scan(target):
    converted_ip = check_ip(target)
    print('\n' + '[-: Scanning target]' + str(target))
    for port in range(1,100):
        scan_port(converted_ip, port)

def check_ip(ip):
    try:
        IP(ip)
        return(ip)
    except ValueError:
        return socket.gethostname(ip)

def get_banner(s):
    return s.recv(1024)

def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)
        sock.connect((ipaddress.port))
        try
            banner = get_baner(sock)
            print('[+] Open Port ' + str(port)  + ' : ' + str(banner.decode().strip('\n')))
        except:
            print('[+] Open Port ' + str(port))
    except:
        pass 


targets = input('[+] Enter target/s to Scan(Multiple targets can be entered by using a ,): ')
if ',' in targets:
    for ip_add in targets.split(','):
        scan(ip_add.strip(' '))
else:
    scan(targets)
