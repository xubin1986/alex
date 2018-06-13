from wxpy import *
import time
import requests
import re
import datetime



def set_bot(groupname):
    bot = Bot(cache_path=True)
    company_group = bot.groups().search(groupname)[0]
    return company_group

def send_msg(someone,msg):
    someone.send(msg)

def get_log(log_file):
    f=open(log_file,'r')
    # with open(log_file,'r') as f: #发现不好用，日志文件未更新，怀疑容易锁住，手动关闭
    data=f.read()
    f.close()
    #以Logs of AI group:字符分割日志，获取最新的部分即最后的一个元素
    latest_data=data.split('Logs of AI group:')[-1]
    res=re.findall('Found Errors.*',latest_data)
    if not res:
        print("have no errors")
        return None
    else:
        #获取错误的最后一个日志，待完善，前面的错误没有获取到，应该可以用正则来匹配所有错误，打印
        res_info=latest_data.split('check below')[-1]
        return res_info

def run():
    company_group=set_bot('世界杯头像运维保障群（讯飞）')
    #日志文件为xshell保存到本地笔记本的日志路径，xshell终端需要tail -f 打印终端日志到控制台
    #需要确认本地日志是在59分之前获取到了，否者后面的检查时间应该延迟
    log_file = 'D:\monitor.log'
    while True:
        current_time=time.localtime()

        #日志消息，获取时间
        last_time = current_time.tm_hour
        last_date = time.strftime('%Y-%m-%d', current_time)
        #正常的时候打印的正常的日志,为了保证微信内格式顶格，这里也顶格，因为检查时间是下个点的01分,所以需要-2,-1
        normal_msg = '''
时间：%s（%s:58-%s:58）
结论：前置平台正常''' % (last_date, last_time - 2, last_time - 1)

        #时间为01分钟的时候检查远程保存的日志,需确保日志已经获取到了,因为之前发现日志没有更新，所以将时间延后
        if current_time.tm_min == 1:
        # if current_time.tm_min == 59:
            #检查远程保存的日志
            log_info = get_log(log_file)
            #如果错误日志为空就发送正常信息
            if not log_info:
                send_msg(company_group,normal_msg)
            #如果错误日志有内容，就发送错误日志
            else:
                #发送错误信息+日志
                err_msg = '''时间：%s（%s:58-%s:58）
                结论：前置平台异常
                info:%s''' % (last_date, last_time - 2, last_time - 1,log_info)

                send_msg(company_group,err_msg)
            #睡眠1200秒，发送后才sleep，不然会有可能刚好sleep过发送的时间节点
            time.sleep(1200)
            print("sleep....",current_time)

        # time.sleep(60)
if __name__ == '__main__':
    run()