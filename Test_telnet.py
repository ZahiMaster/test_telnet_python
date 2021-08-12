# Script to test specific open port on a remote host using Telnet
# Listening to the port

import socket
import telnetlib

# Import list from file with server IP and PORT
server_list = []
port_list = []
server_port_list = []
timeout_seconds=1

with open('test_list.txt', 'r') as f:
    for line in f:
        server_list.append(line.split(',')[0])
        port_list.append(int(line.split(',')[1].strip()))
        server_port_list.append((line.split(',')[0], int(line.split(',')[1].strip())))

# test each server with telnet by list servers in test_list with IP and port
for server in server_port_list:
    try:
        telnet = telnetlib.Telnet(server[0], server[1], timeout_seconds)
        telnet.close()
        print("Test passed" + " " + server[0] + ":" + str(server[1]))
    except socket.timeout:
        print("Test timeout" + " " + server[0] + ":" + str(server[1]))
    except socket.error:
        print("Test error" + " " + server[0] + ":" + str(server[1]))
