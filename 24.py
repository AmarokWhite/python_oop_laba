class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def getName(self):
        return self.name
    def getSalaty(self):
        return self.salary
employee = [
    Employee('Vasilyi', 53533),
    Employee('Ekaterina', 24342),
    Employee('Alya', 23424)]
for name in employee:
    print(name.getName() + " " +  str(name.getSalaty()))
