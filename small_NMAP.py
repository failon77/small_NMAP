import socket
import time

startTime = time.time()

target = input("Enter target IP: ")
target_ip = socket.gethostbyname(target)

print("Scanning ports of", target)

list_of_ports = [80]

for i in list_of_ports:
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn = scanner.connect_ex((target_ip,i))

    if conn == 0:
        print("port %s OPEN" %(i))
    else:
        print("NO OPEN PORTS FOUND!!")
    scanner.close()
