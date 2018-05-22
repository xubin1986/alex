#错误分类
'''
1.语法错误
2.逻辑错误

异常就属于逻辑错误。
# '''
#
# #常见异常类型
# '''
# AttributeError
# ConnectionError
# FileExistsError
# TypeError
# FileNotFoundError
# KeyError
# NameError
# SyntaxError
# TimeoutError
# InterruptedError
# IndexError
# '''
#
# # 可以预测的错误要用if或其他方式处理
#
# # 不可预测的错误用异常处理
#
# class MyIterator:
#     count=None
#     max_num=None
#     def __init__(self,count,max_num):
#         # if not count or not max_num:
#         if not isinstance(int,count):
#             #自己抛出异常
#             raise TypeError("不是int类型")
#         MyIterator.set_attribute(count,max_num)
#     @classmethod
#     def set_attribute(cls,count,max_num):
#         cls.count=count
#         cls.max_num=max_num
#     @classmethod
#     def rangeprint(cls):
#
#         while cls.count < cls.max_num:
#             yield cls.count
#             cls.count+=1
#         # return 'done'
#     @classmethod
#     def run(cls):
#         a = cls.rangeprint()
#         while True:
#             try:
#                 # a=cls.rangeprint()
#                 print(next(a))
#             except StopIteration as e:
#                 print("没什么大不了，一个小小的异常",e)
#                 exit(1)
#
#     @staticmethod
#     def my_error():
#         try:
#             # name
#             # k=[1,2,3]
#             # print(k[4])
#             # l={}
#             # a=l['name']
#             b=1
#             # name
#             c
#         except NameError as e:
#             print("---%s" %e)
#         except IndexError as e:
#             print("---%s" %e)
#         except Exception as e:
#             print("万能版异常：%s" %e)
#         else:
#             print("没有异常执行此处")
#         finally:
#             print("管你有没有异常都执行")
#         #
#         # a=cls.rangeprint()
#         # print(next(a))
# class A:
#     instance=None
#     def __init__(self,name):
#         self.name=name
#     def run(self,iter_name):
#         # choice=input(">:").strip()
#         try:
#             while True:
#                 a=iter_name.__next__()
#                 print(a)
#         except StopIteration:
#             print("the end of Iteration")
# a=A('alex')

# a.run(iter([1,2,3]))

# i=MyIterator(10,1000)
# i.run()
# i.my_error()



class MyError(BaseException):
    def __init__(self,msg):
        self.msg=msg
    def __str__(self):
        # print(self.msg)
        return self.msg

# try:
    # raise MyError("HAHA")
# except MyError as e:
    # print("MyError: %s" %e)


assert 1
print("haha")
assert 2
print("hehe")