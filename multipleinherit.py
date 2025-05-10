class father:
    def skills(self):
        print("gardening and carpentry ")
class mother:
    def skills(self):
        print("cooking and painting ")
class child(father,mother):
    def skills(self):
        father.skills(self)
        mother.skills(self)
        print("playing and dancing ")
c=child()
c.skills()                        