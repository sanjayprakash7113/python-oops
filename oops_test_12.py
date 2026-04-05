class student:
    school="abc"
    def __init__(self,name,mark):
        self.name=name
        self.mark=mark
    def display(self):
        print(self.name)
        print(self.mark)
        print(self.school)
s1=student("victor",99)
s1.display()

class company:
    com="tcs"
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def show(self):
        print(self.name)
        print(self.salary)
        print(self.com)
d1=company("victor",555000)
company.com="accenture"
d1.show()


class person:
    def __init__(self,name):
        self.name=name
    def show_person(self,name):
        print(self.name)
class student(person):
    def __init__(self,name,mark):
        super().__init__(name)
        self.mark=mark
    def show_student(self):
        print(self.name)
        print(self.mark)
s1=student("victor",99)
s1.show_student()
