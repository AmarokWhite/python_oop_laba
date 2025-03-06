class Position:
    def __init__(self, title):
        self.title = title
class Department:
    def __init__(self, name):
        self.name = name
class User:
    def __init__(self, name, position: Position, department: Department):
        self.name = name
        self.position = position
        self.department = department
position = Position("project manager")
department = Department("development")
user = User("Amarok", position, department)
print(f"name: {user.name}")
print(f"position: {user.position.title}")
print(f"department: {user.department.name}")
