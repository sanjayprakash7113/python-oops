class animal:
    def sound(self):
        print("animal")
class dog(animal):
    def sound(self):
        print("bark")
a1=[animal(),dog()]
for i in a1:
    i.sound()


class bank:
    def __init__(self,balance):
        self.__balance=balance

    def deposite(self,amount):
         self.__balance+=amount
         print(self.__balance)
    def withdraw(self,amo):
        if amo<=self.__balance:
             self.__balance-=amo
             print(self.__balance)
        else:
            print("your balance low")
    def show_balance(self):
        print(self.__balance)
a1=bank(1000)
a1.deposite(500)
a1.withdraw(300)
a1.show_balance()


s = "Accenture"
print(s[-5:-1])
print(s[1:7:2]) 
