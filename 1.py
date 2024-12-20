class Car:
    color = None
    fuel = None
    make = None
    model = None
    
    def go(self):
        pass
    def turn(self):
        pass
    def stop(self):
        pass
    
myCar = Car()
myCar.color = 'red'
myCar.fuel = 50
myCar.make = 'Volkswagen'
myCar.model = 'Amarok'
    
myCar.go()
myCar.turn()
myCar.stop()

print(myCar.color)
print(myCar.fuel)
print(myCar.make)
print(myCar.model)
