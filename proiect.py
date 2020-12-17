import socket
import sys

def dword_to_ip(val):

    return "{}.{}.{}.{}".format((val >> 24 & 255),(val >> 16 & 255),(val >> 8 & 255),(val & 255))

def check_range(val1,val2,val3):

    va1_1=val1 >> 24 & 255
    va1_2=val1 >> 16 & 255
    va1_3=val1 >> 8 & 255
    va1_4=val1 & 255

    va2_1=val2 >> 24 & 255
    va2_2=val2 >> 16 & 255
    va2_3=val2 >> 8 & 255
    va2_4=val2 & 255

    ip3 = val3.split(".")

    ip3_1=int(ip3[0])
    ip3_2=int(ip3[1])
    ip3_3=int(ip3[2])
    ip3_4=int(ip3[3])

    if not ip3_1>=va1_1 and ip3_1<=va2_1:
        return False
    if not ip3_2>=va1_2 and ip3_2<=va2_2:
        return False
    if not ip3_3>=va1_3 and ip3_3<=va2_3:
        return False
    if not ip3_4>=va1_4 and ip3_4<=va2_4:
        return False

    return True


def check_ip(addr):
    try:
        socket.inet_aton(addr)
        return True
    except socket.error:
        return False


if "/" in sys.argv[1]:
    ip_and_mask=sys.argv[1].split("/")
    ip=ip_and_mask[0]
    netmask=ip_and_mask[1]
    netmask=int(netmask)
else:
    print("invalid input")
    exit(1)
if check_ip(ip) == True:
    pass
else:
    print("ip is not valid")
    exit(1)
if netmask<0 or netmask>32:
    print("mask is not valid")
    exit(1)



ip = ip.split(".")
new_ip = 0
for i in range(len(ip)):
    new_ip = new_ip << 8
    new_ip += int(ip[i],10)

mask = int("1" * netmask + "0"*(32-netmask),2)
rev_mask = int("1"*(32-netmask),2)

start = new_ip & mask
stop = start | rev_mask

if len(sys.argv)==2:
    print("Range start: {}".format(dword_to_ip(start)))
    print("Range stop : {}".format(dword_to_ip(stop)))
elif len(sys.argv) ==3:
    ip2= sys.argv[2]

    if check_ip(ip2) == True:
        pass
    else:
        print("second ip is not valid")
        exit(1)
    if check_range(start,stop,ip2) == True:
        print("True")
    else:
        print("False")
