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

def get_status(url):
    html = requests.get(url).text
    err_count=html.count('ERROR')
    return err_count

def main():
    url = 'http://10.0.0.11:80'
    company_group=set_bot('吃饭群')
    while True:
        current_time=time.localtime()

        #日志消息
        last_time = current_time.tm_hour
        last_date = time.strftime('%Y-%m-%d', current_time)
        normal_msg = '''时间：%s（%s:58-%s:58）
        结论：前置平台正常''' % (last_date, last_time - 1, last_time)

        if current_time.tm_min == 59:
            err_count = get_status(url)
            if err_count == 0:
                send_msg(company_group,normal_msg)
            else:
                send_msg(company_group,err_msg)
            time.sleep(60)


# current_time=time.localtime()
# last_time=current_time.tm_hour
# last_date=time.strftime('%Y-%m-%d', current_time)
#
# normal_msg='''时间：%s（%s:58-%s:58）
# 结论：前置平台正常''' %(last_date, last_time - 1, last_time)

err_msg='''
时间：2018-06-12（10:58-11:58）
结论：前置平台异常
'''


# print(normal_msg)


# d2 = d1 - datetime.timedelta(hours=1)
# print(d2)