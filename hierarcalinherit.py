class animal:
    def sound(self):
        print("animal sound")
class dog(animal):
    def bark(self):
        print("dog barks") 
class cat(animal):
    def meow(self):
        print("cat meows")
d=dog()
c=cat()
d.bark()
d.sound()
c.meow()                       
c.sound()