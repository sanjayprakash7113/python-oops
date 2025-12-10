#single inheritance
class a():
    def aa(self):
        print("sanjay")
class b(a):
    def bb(self):
        print("prakash")
c=b()
c.bb()
c.aa()


#If child class has no __init__, parent __init__ is used.
class a():
    def __init__(self,name):
        self.name=name
class b(a):
    def bb(self):
        print(self.name)
x=b("sanjay")
x.bb()

#If child class has its own __init__, parent __init__ is ignored unless you use super() manually.
class a():
    def __init__(self,name):
        self.name=name
class b(a):
    def __init__(self,name,age):
        super().__init__(name)
        self.age=age
        print(name)
        print(age)
g=b("victor",20)


class a():
    def ashow(self):
        print("start-a")
        print("end-a")
class b(a):
    def bshow(self):
        print("start-b")
        super().ashow()
        print("end-b")
class c(b):
    def cshow(self):
        print("c-start")
        super().bshow()
        print("c-end")
d=c()
d.cshow()




#If a parent class creates an attribute → children automatically get it.
class a():
    def __init__(self):
        self.x=4
class b(a):
    pass
c=b()
print(c.x)



#If A, B, C all have the same attribute name, child overrides it.
class a():
    def __init__(self):
        self.name="victor"
    def showa(self):
        print(self.name)
class b(a):
    def __init__(self):
        super().__init__()
        self.age=20
    def showb(self):
        print(self.age)
c=b()
c.showa()
c.showb()


class A:
    def __init__(self):
        self.x = "A"

class B(A):
    def __init__(self):
        super().__init__()
        self.x = "B"

class C(B):
    def __init__(self):
        super().__init__()
        self.x = "C"

obj = C()
print(obj.x)







