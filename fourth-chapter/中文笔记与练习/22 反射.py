#通过一个字符串来映射到一个对象的某个属性上
# hasattr(obj,str_name)
# getattr(obj,str_name,default)
# setattr(obj,str_name,value)
# delattr(obj,str_name)

#写一个get put的类，实现文件上传下载

class Service:
    def run(self):
        while True:
            inp=input(">:").strip()
            cmds=inp.split()
            if hasattr(self,cmds[0]):
                func=getattr(self,cmds[0])
                func(cmds)
    def get(self,cmds):
        print("get---->",cmds)
    def put(self,cmds):
        print("put---->",cmds)

obj=Service()
obj.run()
