#Normal functions cannot receive those values during object creation,
#even if the class is inherited
class a():
    def b(self,name):
        self.name=name
    def c(self,age):
        self.age=age
class d(a):
    def e(self):
        print(self.name)
        print(self.age)
q=d()
q.b("victor")
q.c(20)
q.e()



#If you want to pass values from Child → Parent at the time of creating the object →
#you MUST use __init__

class a():
    def __init__(self,name,age):
        self.name=name
        self.age=age
class b(a):
    def c(self):
        print(self.name)
        print(self.age)
w=b("vic",100)
w.c()



