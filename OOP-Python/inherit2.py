class person:
    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last

    def name(self):
        return self.firstname + " " + self.lastname

class employee(person):
    def __init__(self, first, last, staffNum):
        person.__init__(self, first, last)
        self.staffnumber = staffNum

    def showEmployee(self):
        return self.name() + ", " + self.staffnumber

    def name(self):
        return self.lastname + " " + self.firstname

    def nameFirstLast(self):
        return super (employee, self).name()

x = person("Marge", "Simpson")
y = employee("Homer", "Simpson", "1067")

print(x.name())
print(y.showEmployee())
print(y.nameFirstLast())
print(y.name())
