#METHOD OVERRIDING

#Child class redefines (replaces) a method from parent class with the same name.

class a():
    def aa(self):
        print("show a")
class b(a):
    def aa(self):
        print("show b")
c=b()
c.aa()
#LWAYS the object’s class decides the method(c.aa()-- call b -- not a)


#You can still call parent method using super()
class a():
    def A(self):
        print("show-a")
class b(a):
    def A(self):
        print("show-b")
        super().A()
obj=b()
obj.A()


class a():
    def __init__(self):
        print("a")
class b(a):
    def __init__(self):
        print("b")
        super().__init__()
obj=b()




#METHOD OVERLOADING

#So how does Python simulate Overloading
# Default arguments
# *args
#**kwargs


#ethod Overloading using DEFAULT ARGUMENTS
class a():
    def add(self,a=None,b=None,c=None):
        if a and b and c:
            print(a+b+c)
        elif a and b:
            print(a+b)
        else:
            print(a)
obj=a()
obj.add(3,4,5)


class Math:
    def add(self, a=0, b=0, c=0):
        print(a + b + c)

m = Math()
m.add(10, 20)         # 10 + 20 + 0
m.add(5, 6, 7)        # 5 + 6 + 7
m.add(10)             # 10 + 0 + 0



#Method Overloading using *args


class a():
    def b(self,*args):
        print(args)
obj=a()
obj.b(12,3,45,4,78)
obj.b("sanjay","victor")

#Method Overloading using **kwargs
class a():
    def b(self,**kwargs):
        print(kwargs)
obj=a()
obj.b(name="victor",age=20,city="newyork")


class Display:
    def show(self, *args, **kwargs):
        if args:
            print("Positional:", args)
        if kwargs:
            print("Keywords:", kwargs)

d = Display()
d.show(10, 20)
d.show(name="Victor", age=21)
d.show(1, 2, 3, x=10, y=20)

































