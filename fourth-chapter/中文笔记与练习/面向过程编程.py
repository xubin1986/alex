# 简化编程，流程化编程
#用户注册分三个步骤，交互输入，检查输入，注册信息
import json
def interactive():
    user=input("user:").strip()
    passwd=input("pwd:").strip()
    user_info={
        "user":user,
        "passwd":passwd
    }
    return user_info

def check(user_info):
    isvalid=True
    if user_info['user'] == "":
        print("用户名不能为空")
        isvalid=False
    if len(user_info['passwd']) < 6:
        print("密码不能少于6位")
        isvalid=False
    check_info={
        "isvalid":isvalid,
        "user_info":user_info
    }
    return check_info

def register(check_info):
    if check_info["isvalid"]:
        with open("db.json","w",encoding="utf-8") as f:
            json.dump(check_info["user_info"],f)
def main():
    user_info=interactive()
    check_info=check(user_info)
    register(check_info)
if __name__ == '__main__':
    main()
