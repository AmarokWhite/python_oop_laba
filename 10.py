class Employee:
    name = 'john'
    salary = '5000'
    
    def show(self):
        return self.cape(self.name)

    def cape(self,stri):
        return stri.upper()

employee = Employee()

print(employee.name)
print(employee.salary)
