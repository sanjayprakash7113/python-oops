class Vehicle():
    def __init__(self,name):
        self.name=name
        print(self.name)
        
class Car(Vehicle):
    def __init__(self,name,model):
        self.model=model
        print(self.model)
        super().__init__(name)
        
class ElectricCar(Car):
    def __init__(self,name,model,ele):
        self.ele=ele
        print(self.ele)
        super().__init__(name,model)
a=ElectricCar("ec4532","shark","f1")


class Dad:
    def pro(self):
        self.name = "Victor"
        print(self.name)

class Mom:
    def pro(self):
        self.age = 20
        print(self.age)

class Child(Dad, Mom):
    pass

a = Child()
a.pro()  # Calls Dad.pro() because Dad is first in MRO


class animal:
    def sount(self):
        self.sou="some sound"
        print(self.sou)
class dog:
    def sount(self):
        self.so="bark"
        print(self.so)
a=dog()
a.sount()
