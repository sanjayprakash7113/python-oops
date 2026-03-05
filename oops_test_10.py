class emp():
    count=0
    com="tcs"
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def show(self):
        print(self.name)
        print(self.salary)
        print(emp.com)
    @classmethod
    def total_emp(clg,count):
        b=len(self.name)
        if b>count:
            
            count=b
            print(count)
    @staticmethod
    def is_high_salary(salary):
        print(max(salary))
a=emp("victor",550000)
a.show()
a.total_emp()
