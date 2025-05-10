class student:
    def __init__(self,name,marks):
        self.name = name
        self.marks= marks
    def get_grade(self):
         if self.marks>=90:
            return 'A'
         elif  self.marks<70 and self.marks>50:
             return "B"
         else :
             return "satifactory result, need to study more"
s1= student("rex",91)
print(s1.get_grade())         
s2= student("rex",89)
s3= student("rex",55)
print(s2.get_grade())
print(s3.get_grade())