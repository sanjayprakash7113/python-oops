class acc():
    def __init__(self,balance):
        self.__balance=balance
    def get(self):
        return  self.__balance
    def set(self,amount):
        if amount>0:
            self.__balance=amount
        else:
            print("zero balance")
a=acc(403213)
print(a.get())


