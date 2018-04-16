# coding=utf-8
import paramiko,sys
class SSHConnection(object):
    def __init__(self, host, port, username, password):
        self._host = host
        self._port = port
        self._username = username
        self._password = password
        self._transport = None
        self._sftp = None
        self._client = None
        self._connect()  # 建立连接

    def _connect(self):
        transport = paramiko.Transport((self._host,self._port))
        transport.connect(username=self._username, password=self._password)
        self._transport = transport

    #下载
    def download(self,remotepath,localpath):
        if self._sftp is None:
            self._sftp = paramiko.SFTPClient.from_transport(self._transport)
        self._sftp.get(remotepath,localpath)
    #上传
    def put(self, localpath, remotepath):
        if self._sftp is None:
            self._sftp = paramiko.SFTPClient.from_transport(self._transport)
        self._sftp.put(localpath, remotepath)
    #执行命令
    def exec_command(self, command):
        if self._client is None:
            self._client = paramiko.SSHClient()
            self._client._transport = self._transport
        stdin, stdout, stderr = self._client.exec_command(command)
        data = stdout.read()
        if len(data) > 0:
            print(data.strip())   #打印正确结果
            return data
        err = stderr.read()
        if len(err) > 0:
            print(err.strip())    #输出错误结果
            return err

    def close(self):
        if self._transport:
            self._transport.close()
        if self._client:
            self._client.close()
def upload(conn,*args):
    localpath=args[0][2]
    remotepath=args[0][3]
    conn.put(localpath, remotepath)
    conn.close()
def download(conn,*args):
    localpath=args[0][2]
    remotepath=args[0][3]
    conn.download(remotepath, localpath)
    conn.close()
def exec_command(conn,cmd_string):
    conn.exec_command(cmd_string)
    conn.close()
def main(*args):
    if len(args[0]) == 1:
        print("Usage:%s operation_type<upload,download,exec_command> options<lpath,rpath,cmd>" %args[0][0])
        exit()
    operation_type=args[0][1]
    conn = SSHConnection('192.168.131.101', 22, 'root', '123456')
    operation_dict={"upload":upload,"download":download,"exec_command":exec_command}
    if operation_type not in operation_dict:
        print("not in operation_dict")
        print("Usage:%s operation_type<upload,download,exec_command> options<lpath,rpath,cmd>" %args[0][0])
    else:
        operation_dict[operation_type](conn,sys.argv)
if __name__ == "__main__":
    main(sys.argv)