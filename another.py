bike = ['bajaj', 'powerbike', 'small']
print(bike[0].upper())
bike.append('honda')
print(bike)
del bike[1]
print(bike)
pop_bike = bike.pop()
print(bike)
print(pop_bike)
last_owned= bike.pop()
print(f"My first bike was {last_owned.upper()}.")
first_owned=bike.pop(0)
print(f"My first bike was {first_owned.upper()}.")
car = ['toyota', 'honda', 'camry']
print(car)
