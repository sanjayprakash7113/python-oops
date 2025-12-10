class A:
    def show(self):
        print("A")

class B:
    def show(self):
        print("B")

class C(A, B):
    pass

obj = C()
obj.show()

class a():
    def show(self):
        print("a")
class b(a):
    def show(self):
        print("b")
        super().show()
class c(a):
    def show(self):
        print("c")
        super().show()
class d(b,c):
    def show(self):
        print("d")
obj=d()
obj.show()
