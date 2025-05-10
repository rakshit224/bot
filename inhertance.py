class Animal:
    def speak(self):
        print("animal speaks ")
class dog(Animal):
    def bark(self):
        print("dog barks")
class puppy(dog):
    def weep(self):
        print("puppy weeps")

p=puppy()
p.speak()
p.bark()
p.weep()       