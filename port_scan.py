import socket
from colorama import init, Fore, Back, Style #pip install colorama
import time
import threading

#import base64

def port_scan(host,port):
    host_ip = socket.gethostbyname(host)
    status = False
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        s.connect((host_ip, port))
        status = True
    except:
        status = False
    
    if status:
        print("{}:{} is ".format(host_ip,port) + (Style.BRIGHT + Fore.GREEN + "OPEN"))
    #else:
        #print("{}:{} is ".format(host_ip,port) + (Style.BRIGHT + Fore.RED + "CLOSED"))


choice = input ("***********************\nPlease Make Your Choice\n1-) Full Port Scan\n2-) Specific Port Scan\n")
 
if (choice == "1"):
    host = input("Enter the Target Address: ")
    start_time = time.time()
    for i in range (0,65535):
        thread = threading.Thread(target=port_scan,args=(host,i))
        thread.start()
    end_time = time.time()
    print("To all scan all ports it took {} seconds".format(end_time-start_time))
elif (choice == "2"):
    host = input("Enter the Target Address: ")
    port_range = input("Enter the Port Range (10-20): ")
    x = port_range.split("-")
    start_time = time.time()
    for i in range (int(x[0]),int(x[1])):
        thread = threading.Thread(target=port_scan,args=(host,i))
        thread.start()
    end_time = time.time()
    print("To all scan all ports it took {} seconds".format(end_time-start_time))
elif (choice == "q"):
    print("Good Bye..")
else:
    print("wrong choice!!")


