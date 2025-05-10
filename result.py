class Student:
    def __init__(self, name, marks):
        if 0 <= marks <= 100:
            self.name = name
            self.marks = marks
        else:
            raise ValueError("Marks must be between 0 and 100.")

    def get_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks > 75:
            return "B"
        elif self.marks > 60:
            return "C"
        else:
            return "Fail"

# Example usage
try:
    s1 = Student("Nikki", 70)
    print(s1.get_grade())
except ValueError as e:
    print("Error:", e)
