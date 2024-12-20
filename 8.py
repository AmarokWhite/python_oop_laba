class Student:
    name = 'sergey'
    surname = 'pribytkov'
    
    def show(self):
        return self.cape(self.name)
        
    def cape(self,stri):
        return stri.upper()
        
print(Student.name)
print(Student.surname)
