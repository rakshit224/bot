class employee:
    def __init__(self,name,employee_id,salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary
    def display(self):
        print(f"name is {self.name} , ID is {self.employee_id}, salary is {self.salary}")
class manager(employee):
    def __init__(self,name,employee_id,salary,department):
        super().__init__(name,employee_id,salary)
        self.department = department
    def display(self):
        super().display()
        print(f"department is {self.department}")
class developer(employee):
    def __init__(self,name,employee_id,salary,programming_lang):
        super().__init__(name,employee_id,salary)
        self.programming_lang = programming_lang
    def display(self):
        super().display()
        print(f"language is {self.programming_lang}")

d=developer("rakshit",4545,50000,"python")
d.display()
m=manager("Rex",1818,60000,"HR")
m.display()