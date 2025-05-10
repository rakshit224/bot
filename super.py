class person:
    def __init__(self,name):
        self.name = name
    def show(self):
        print("Name is ",self.name)

class student(person):
    def __init__(self,name,roll):
        super().__init__(name)
        self.roll = roll

    def show(self):
        super().show()
        print("Roll is ",self.roll)

s=student("rakshit",45)
s.show()        
