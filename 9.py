class Student:
    name = 'sergey'
    surname = 'pribytkov'
    
    def show(self):
        return self.name
    
student = Student()
print(student.name)
print(student.surname)
