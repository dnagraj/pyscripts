from socket import *
import time
starttime=time.time()

target=input('Enter a host to be scanned:')
t_ip=gethostbyname(target)
print("Starting scan on host: ",t_ip)
for i in range(100,500):
    s=socket(AF_INET,SOCK_STREAM)
    conn=s.connect_ex((t_ip,i))
    if conn==0:
        print("port %d: Open " %(i,))
    s.close()
print("Time taken:",time.time()-starttime)
