class student():
    school="abc"
    def __init__(self,name,mark):
        self.name=name
        self.mark=mark
    def show(self):
        print(student.school)
        print(self.name)
        print(self.mark)
        print(self.school)
    @classmethod
    def change_school(clg,school):
        clg.school=school
    @staticmethod
    def is_pass(mark):
        if mark>40:
            print("pass")
        else:
            print("fail")
        
a=student("victor",88)
a.show()
a.change_school("govt")
a.show()
a.is_pass(88)
