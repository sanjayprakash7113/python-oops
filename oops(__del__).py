class A:
    def __init__(self):
        print("I am born")

    def __del__(self):
        print("I am deleted")

a = A()      # object created → prints: I am born

del a        # object deleted → prints: I am deleted
b=A()


class a():
    def __init__(self,path):
        self.f=open(path,"r")
    def __del__(self):
        self.f.close()
