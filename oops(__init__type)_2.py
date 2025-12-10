#Default / Mutable Argument Pitfall in __init__

class demo:
    def __init__(self,item=[]):
        self.item=item
d1=demo()
d2=demo()
d1.item.append(1)
print(d1.item)
print(d2.item)

class dem:
    def __init__(self,item=None):
        if item is None:
            self.item=[]
        else:
            self.item=list(item)

a1=dem([1,2,3])
print(a1.item)
a2=dem()
print(a2.item)


class Person:
    def __init__(self, info=None):
        self.info = {} if info is None else info

p1 = Person()
p2 = Person()

p1.info['name'] = 'Amit'
print(p1.info) 
print(p2.info)  
