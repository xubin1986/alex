#类会有一个继承的序列，使用mro可以查看
#经典类，python2中没有显示继承object的类
#新式类，python2中显示继承了object的类或子类，python3中所有类如果没有继承某个类，默认都是继承object类
#python3中，所有类都是新式类
#经典类使用深度优先查找属性
#新式类使用广度优先查找属性
#深度优先是一条道走到底，查找完第一个父亲，找第一个父亲的父亲一直到底
#广度优先是要到底的时候，换下一个父亲，下面是例子测试
#查找到共同祖宗的下一个换父亲，反正共同的血脉关系依次放在最后
class A(object):
    def test(self):
        print("from A")
class X(A):
    def test(self):
        print("from X")
class B(A):
    def test(self):
        print("from B")
class C(X):
    def test(self):
        print("from C")
class D(B):
    def test(self):
        print("from D")
class E(C):
    def test(self):
        print("from E")
class F(D):
    def test(self):
        print("from F")
class G(E):
    def test(self):
        print("from G")
class H(F,G):
    def test(self):
        print("from H")
print(H.mro())