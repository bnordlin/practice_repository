# list
lst = [10,20,30,40,50]
lst.append(5)
lst.append(6)
lst.append(7)
print(lst)

lst.remove(40)
print(lst)
lst.pop(2)
print(lst)
lst.reverse()
print(lst)
lst.sort()
print(lst)

lst[0] = 500
print(lst)

lst = lst[1:]
print(lst)

index10 = lst.index(10)
print(index10)
lst.append(20)
lst.append(20)
lst.append(20)
print(lst)
count20 = lst.count(20) #Could be helpful for homework 2
print(count20)

copy_lst = lst #common error, just copies memory address, so cannot modify one and not the other
print(copy_lst)
copy_lst[0] = 99
print(copy_lst)
print(lst)

#make an actual seperate copy
new_copy = lst.copy()
print(new_copy)
new_copy[0] = 100
print(new_copy)
print(lst)

new_copya = lst[:]
print(new_copya)
new_copya[0] = 100
print(new_copya)
print(lst)

empty_lst = []
for val in lst:
    empty_lst.append(val)
print(empty_lst)

empty_lst = [0] * 10
print(empty_lst)
empty_lst[0] = 10

#List Comprehensions 

squares = []
for i in range(1,10):
    squares.append(i*i)
print(squares)

squares = [x * x for x in range (1,10)]
print(squares)

plus5 = [squares[i] + 5 for i in range(0,9)]
print(plus5)

#or plus5 = [val + 5 for val in squares()]

values = [34,27,95,18,36,21,64,50,77]
even_values = [x for x in values if x % 2 == 0]
print(even_values)
small_values = [x for x in values if x < 20]
print(small_values)

#dictionaries (similar to hash maps in java)
fav_foods = {"Kathleen" : "pizza", "Hannah" : "Pasta", "Kush" : "Fries", "Yamill" : "Fries"}
hff = fav_foods["Hannah"]
print(hff)
for key in fav_foods:
    print(f"{key}'s favorite food is {fav_foods[key]}")

for person, food in fav_foods.items():
    print(f"{person}'s favorite food is {food}")

if "bob" in fav_foods:
    print_fav_foods["bob"]
else:
    fav_foods["bob"] = "wings"



