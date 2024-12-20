class Employee:
    def show(self, name, salary):
        return name + ' ' + salary
    
employee = Employee()
print(employee.show('John', '5000'))
