cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

car = 'Audi'
match = car.lower() == 'audi' # car.lower() doesn't change original value
print(match)
print(car)