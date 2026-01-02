class emp():
    def work(self):
        print("emp work")
class manager(emp):
    def work(self):
        super().work()
        print("manager work")
a=manager()
a.work()


class a():
    def show(self):
        print("a")
class b(a):
    def show(self):
        super().show()
        print("b")
class c(a):
    def show(self):
        super().show()
        print("c")
class d(c,b):
    def show(self):
        super().show()
        print("d")

aa=d()
aa.show()
