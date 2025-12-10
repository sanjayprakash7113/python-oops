#class variable vs instance variable
class a:
    uiu="ere"
    def __init__(self,name,age):
        self.name=name
        self.age=age
p=a("victor",19)
p1=a("sanjay",20)
w1=a("b",7)
print(p.name,p.age)
print(p1.name,p1.age)
p.uiu="abc"
print(p.uiu)
print(p1.uiu)
a.uiu="kik"
print(p1.uiu)
print(w1.uiu)

#type of init(validasion check)
class bank:
    def __init__(self,bal):
        if bal>0:
            raise ValueError("bal not zero")
        self.bal=bal

z=bank(0)
print(z.bal)

#file handling
class file:
    def __init__(self,oops_1):
        self.f=open(oops_1,"r")
oops=file("oops_1.py")
print(oops.f.read())

#one tie startup
import random
class count():
    def __init__(self):
        self.id=random.randint(10,99)
co=count()
print(co.id)


#default setup
class Car:
    def __init__(self, brand="BMW", speed=0):
        self.brand = brand
        self.speed = speed


