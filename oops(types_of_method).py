#instance method
class a():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def b(self):
        print(self.name)
        print(self.age)
c=a("victor",20)
c.b()

#class method
class a():
    x="car"
    @classmethod
    def b (cls):
        print(cls.x)
s=a()
s.b()

class a():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    @classmethod
    def b(cls,name,birth_year):
        age=2026-birth_year
        return cls(name,age)
v=a.b("victor",2004)
print(v.name,v.age)

#static method
class s():
    @staticmethod
    def __init__(a,d):
            print(a+d)

a=s(3,4)
