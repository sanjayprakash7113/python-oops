class student():
    def display(self,name,rool_no):
        self.name=name
        self.rool_no=rool_no
a=student()
a.display("victor",20)
print(a.name)
print(a.rool_no)


class emp():
    def __init__(self,id,name,salary):
        self.id=id
        self.name=name
        self.salary=salary
a=emp(2,"ram",4025392)
print(a.id)


class per():
    def __init__(self,name,age):
        self.name=name
        self.age=age
class stu(per):
    def __init__(self,name,age,rool_no):
        self.rool_no=rool_no
        super().__init__(name,age)
a=stu("sanjay",20,2090)
print(a.name)
print(a.age)
