import paramiko,threading,sys,time,os
import configparser
class SSHThread(threading.Thread):
    def __init__(self,ip,port,user,pwd,timeout,cmd):
        # threading.Thread.__init__(self)
        super().__init__()
        self.ip = ip
        self.port = port
        self.user = user
        self.pwd = pwd
        self.timeout = timeout
        self.cmd = cmd
        self.LogFile="./test.log"
    def run(self):
        print("start try ssh => %s" % self.ip)
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(self.ip,self.port,username=self.user,password=self.pwd,timeout=self.timeout)
            print("[%s] Login %s => %s" %(self.ip,self.user,self.pwd))
            open(self.LogFile,"a").write("[ %s ] IP => %s, port => %d " %(time.asctime(time.localtime(time.time())),self.ip,self.port))
            print("[%s] exec: %s" %(self.ip,self.cmd))
            open(self.LogFile,"a").write("[%s] exec : %s" %(self.ip,self.cmd))
            stdin,stdout,stderr = ssh.exec_command(self.cmd)
            print("[%s] exec result: %s" %(self.ip,stdout.read()))
            return True
        except:
            print("[%s] Error %s => %s" %(self.ip,self.user,self.pwd))
            open(self.LogFile,"a").write("[%s]" %(self.ip))
            return False
def ViolenceSSH(ip,port,user,pwd,timeout,cmd):
    ssh_scan = SSHThread(ip,port,user,pwd,timeout,cmd)
    ssh_scan.start()

if __name__ == '__main__':
    conf = configparser.ConfigParser()
    conf.read('default.conf',encoding="utf8")
    ipList = conf['default']['hosts'].split(',')
    port = int(conf['default']['port'])
    user = conf['default']['user']
    password = conf['default']['password']
    timeout = int(conf['default']['timeout'])
    # cmd='uptime'
    cmd = None
    try:
        cmd=sys.argv[1]
    except IndexError:
        print("usage: %s [command]" % sys.argv[0])
    for ip in ipList:
        threading.Thread(target=ViolenceSSH,args=(ip,port,user,password,timeout,cmd)).start()