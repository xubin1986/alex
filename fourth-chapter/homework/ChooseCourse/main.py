from core.roles import *
if __name__ == "__main__":


    #school_bj
    # 1.创建北京、上海2所学校
    school_bj=School("luffy","北京")
    school_sh=School("luffy","上海")

    # 2.创建linux, python, go 3个课程 ， linux\py在北京开， go在上海开

    linux=Course('linux',6,5000)
    linux.getinfo()
    python=Course('python',8,8000)
    go=Course('go',7,7500)

    school_bj.add_course(linux)
    school_bj.add_course(python)
    school_sh.add_course(go)

    str=school_sh.courses
    t1=Teacher('alex',22,'female', school_bj)
