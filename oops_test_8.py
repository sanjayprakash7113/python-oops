class animal():
    def sound(self):
        print("sound")
class dog(animal):
    def sound(self):
        print("brak")
class cat(animal):
    def sound(self):
        print("meow")
animals=[dog(),cat(),animal()]
for i in animals:
    i.sound()
