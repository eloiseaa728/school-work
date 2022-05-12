class pets():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def nameIs(self):
        print("My name is", self.name)

    def ageIs(self):
        print(self.name, "is", self.age, "years old")

class cat(pets):
    def talk(self):
        print(self.name, "says MEOWWWWWWWWWWWWWWWWWWW" + "W"*10000)

class dog(pets):
    def talk(self):
        print(self.name, "says", "bark"*10)

class mouse(pets):
    def talk(self):
        print(self.name, "squeeks squeek")

tom=dog("Tom","2")
tom.ageIs()
spot=cat("Spot","4")
daisy=mouse("Daisy","1")

animals = [tom, daisy, spot]
print("The animals speak")

for i in animals:
    i.talk()
