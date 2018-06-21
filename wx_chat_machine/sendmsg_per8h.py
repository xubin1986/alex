# coding: utf-8
from wxpy import *
import time

@dont_raise_response_error
def send_msg(someone,msg):
    someone.send(msg)
def run():
    bot = Bot(cache_path=True)
    company_group1 = bot.groups().search('世界杯头像运维保障群（讯飞）')[0]

    while True:
        current_time=time.localtime()
        lastest_hour = current_time.tm_hour
        lastest_date = time.strftime('%Y-%m-%d', current_time)

        msg1 = '时间：%s（0:00-9:00）\n结论：前置平台正常' % lastest_date
        msg2 = '时间：%s（9:00-18:00）\n结论：前置平台正常' % lastest_date
        msg3 = '时间：%s（18:00-0:00）\n结论：前置平台正常' % lastest_date

        if lastest_hour == 9 and current_time.tm_min == 0:
            send_msg(company_group1,msg1)
        elif lastest_hour == 18 and current_time.tm_min == 0:
            send_msg(company_group1,msg2)
        elif lastest_hour == 0 and current_time.tm_min == 0:
            send_msg(company_group1,msg3)
        else:
            continue
        time.sleep(7200)

if __name__ == '__main__':

    count = 1
    while True:
        print("start run the %s time" %count)
        try:
            run()
            count += 1
        except Exception as e:
            print(e)
            continue