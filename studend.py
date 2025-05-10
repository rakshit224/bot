class student:
    def __init__(self,name,age,enrol):
        self.name = name
        self.age =age
        self.enrol =enrol
    def student_info(self):
        print(f"my name is {self.name} my age is {self.age} and enrol num is {self.enrol}")
s1= student('mohit',25,665)
s1.student_info()    