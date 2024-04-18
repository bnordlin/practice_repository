from car import Car

cars = []
with open("cars.txt") as file:
    for line in file:
        stripped_line=line.strip()
        tokens = stripped_line.split()
        tokens[2] = int(tokens[2])
        tokens[3] = int(tokens[3])
        cars.append(Car(tokens[0], tokens[1], tokens[2], tokens[3]))

print(cars[0])
print(cars[1])
print(cars[0].get_gas_tank())
print(cars[0].get_odometer())
cars[0].drive()
print(cars[0].get_gas_tank())
print(cars[0].get_odometer())
print(cars[1].get_gas_tank())
print(cars[1].get_odometer())
cars[1].drive()
print(cars[1].get_gas_tank())
print(cars[1].get_odometer())

'''
for i, val in enumerate(tokens):
    if (val.isdigit()):
        tokens[i] = int(val)
'''