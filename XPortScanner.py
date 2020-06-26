#! /bin/python
import sys
import socket
from datetime import datetime

#define our target
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) # translate hostname to IPv4
    
else:
    print("Invalid amount of arguments")
    print("Syntax python3 Xscanner.py <ip>")
    
#add a pretty banner

print ("-" * 50)
print("Made By: Xaliss Pasha")
print("\n")
print("Scanning Target " +target)
print("Time started : "+str(datetime.now()))
print("-" * 50)

try:
     for port in range(1,65535):
            s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            result= s.connect_ex((target,port)) #returns an error indicator
            if result == 0 :
                print("Port {} is open ".format(port))
                s.close()
  
except KeyboardInterrupt:
    print("\nExiting program")
    sys.exit
    
except socket.gaierror:
    print("\nHostname Couldn't be resolved")
    sys.exit
    
except socket.error:
    print("\nCouldn't connect to server")
    sys.exit 