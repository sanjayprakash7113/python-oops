class student():
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no
    def display(self):
        print(self.name)
        print(self.roll_no)
a=student("victor",7112)
a.display()


class person():
    def __init__(self,name):
        self.name=name
    def show_name(self):
        print(self.name)
class employee(person):
        pass
    
a=employee("victor")
a.show_name()

class parent():
    def work(self):
        print("work-5hr")
class child(parent):
    def work(self):
        print("work_15hr")
a=child()
a.work()


class bank():
    def account(self,balance):
        self.__balance=balance
    def dep(self,amo):
        self.__balance+=amo
    def withdraw(self,amo):
        if amo<=self.__balance:
            self.__balance-=amo
        else:
            print("not available")
    def show(self):
        print(self.__balance)
a=bank()
a.account(5000)
a.dep(1000)
a.withdraw(700)
a.show()




from abc import ABC, abstractmethod

class shap(ABC):
    @abstractmethod
    def area(self,size):
        pass
class rectangle(shap):
    def area(self,size):
        print(size)
a=rectangle()
a.area(34)

















