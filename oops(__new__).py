class A():
    def __new__(cls):
        print("hello")
        obj=super().__new__(cls)
        return obj
    def __init__(self):
        print("hi")
a=A()


# 1 NORMAL CLASS (mutable) → __init__ works

class Num:
    def __init__(self, val):
        self.val = val + 10

b = Num(10)
print("Mutable class output:", b.val)   


#IMMUTABLE TYPE (int) → __init__ does NOT work
# Correct → use __new__

class Numb(int):
    def __new__(cls, value):
        return super().__new__(cls, value + 23)

s = Numb(20)
print("Immutable int output:", s)         

#NORMAL CLASS (mutable string wrapper) → __init__ works

class Lett:
    def __init__(self, text):
        self.text = text.upper()

q = Lett("victor")
print("Mutable string wrapper:", q.text)  



# IMMUTABLE STRING (str) → __init__ cannot modify
# Correct → use __new__

class Let(str):
    def __new__(cls, text):
        return super().__new__(cls, text.upper())

w = Let("sanjay")
print("Immutable str output:", w)         # SANJAY
