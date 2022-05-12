class Cat:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name, "says Meow!")

    def drink(self):
        print(self.name, "drinks its milk")
        print(self.name, "takes a nap")

romeo = Cat("Romeo")
romeo.speak()
romeo.drink()
