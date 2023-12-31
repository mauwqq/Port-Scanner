import socket
import sys
from datetime import datetime
import subprocess

subprocess.call('cls', shell=True)

remote_server = input('Enter a remote host to scan: ')
remote_server_ip = socket.gethostbyname(remote_server)
port_range = input('insert the port range: ')
port_range = port_range.split('-')

print('-' * 60)
print(f'Scanning remote host: {remote_server_ip}')
print('-' * 60)

time1 = datetime.now()
timeout = 0.5

try:
    for port in range (int(port_range[0]), int(port_range[1])):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((remote_server_ip, port))
        if result == 0:
            print(f'Port {port}: Open')
        sock.close()

except KeyboardInterrupt:
    print("You pressed Ctrl+C")
    sys.exit()

except socket.gaierror:
    print('Hostname could not be resolved. Exiting')
    sys.exit()

except socket.error:
    print("Couldn't connect to server")
    sys.exit()

# Checking the time again
time2 = datetime.now()

# Calculates the difference of time, to see how long it took to run the script
total =  time2 - time1

# Printing the information to screen
print(f'Scanning completed in: {total}')