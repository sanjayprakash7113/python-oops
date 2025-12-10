#instance variable
class aa():
    def __init__(self,x):
        self.x=x
class bb(aa):
    def __init__(self,x):
        super().__init__(x)
        print(self.x)
        
rt=bb(5)

#global variable
x=10
class a():
    def __init__(self):
        pass
class b(a):
    def __init__(self):
        print(x)
x=b()

#local variable
class a():
    def __init__(self):
        e="uy"
        print(e)
r=a()
       
        


        
