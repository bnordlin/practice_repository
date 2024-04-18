#Brian Nordlinger
from dog import Dog

dogs = []
with open("dogs.txt") as file:
    for i, line in enumerate(file):
        stripped_line=line.strip()
        tokens = stripped_line.split()
        dogs.append(Dog(tokens[0], tokens[1], tokens[2], tokens[3]))
        print(dogs[i])
    
    print(dogs[0].get_name())
    print(dogs[0].get_breed())
    print(dogs[0].get_trick())
    print(dogs[0].isHungry())
    dogs[0].speak()
    dogs[0].feed()
    dogs[0].change_trick("fetch")
    print(dogs[0].get_name())
    print(dogs[0].get_breed())
    print(dogs[0].get_trick())
    print(dogs[0].isHungry())