class person:
    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last

    def name(self):
        return self.firstname + " " + self.lastname

class newPerson(person):
    def name(self):
        return self.lastname + " " + self.firstname
# Subclass has a method of the same name as the superclass, therefore it overrrides it (dynamic polymorphism)

personOne = person("Jerem", "Sajohnson")
personTwo = newPerson("James", "Kidderminster")

people = [personOne, personTwo]

for i in people:
    print(i.name())
