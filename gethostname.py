import socket

hostname=socket.gethostname()
ip=socket.gethostbyname(hostname)
print("Name of the host is {}".format(hostname))
print("IP address is {}".format(ip))