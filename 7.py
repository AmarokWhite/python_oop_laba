class Employee:
    name = None
    salary = None
    def show(self):
        print(self.name)
        print(self.salary)
        
employee = Employee()
employee.name = 'John'
employee.salary = '5000'
employee.show()
