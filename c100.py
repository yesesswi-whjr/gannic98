from ipaddress import summarize_address_range


class Student(object):
    def __init__(self,name,age,gender,level,grades=None):
        self.name=name
        self.age=age
        self.gender=gender
        self.level=level
        self.grades=grades or {}
    def setGrade(self,course,grade):
        self.grades[course]=grade
    def getGrade(self,course):
        return self.grades[course]
    def getCgpa(self):
        return sum(self.grades.values())/len(self.grades)
yesesswi=Student("Krishna",14,"male",9,{"maths":7.2})
yesesswi1=Student("Krishna1",14,"male",9,{"maths":3.2})
print(yesesswi.getCgpa())