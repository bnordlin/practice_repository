print ("hello world")

# this is a comment

'''
this is a multi line comment
this is a multi line comment
'''

# Variables
x = 10
print (x)
s = "hello"
x = s
print (x)

# Math operators
x = 10
y = 5
print (x/y)
print (x//y)

# Math functions
x = 2
y = 3
print (pow(x,y))

# if statements 
x = 1
y = -1

if x > 0:
    print ("x is positive")
if x > y:
    print ("x is larger than y")

# loops

nums = [2,4,6,8,10]
for i in range(5):      #for
    print(i)
for i in range(2,5):    #for
    print (i)
for i in range(len(nums)):     #for
    print(nums[i])
for val in nums:             #for each
    val += 5            #doesn't modify list, modifies val
    print(val)
for i, val in enumerate(nums):              #enumerate loop
    print("i is ", i, "and val is ", val)

dogs = ["boomer", "rocky", "daisy", "archie", "jake"]
for i in range(len(dogs)):
    print(dogs[i])
for dog in dogs:
    print(dog)
for i, dog in enumerate(dogs):
    print("index:", i, "dog:", dog)

count = [1,2,3,4,5,6]
sum = 0
for i in range(len(count)):
    sum += count[i]
print ("sum:", sum)
print (f"the sum of nums is {sum}")

# Functions 

def hello(name="friend"):
    print("Hello", name)
hello("John")
hello()

# Strings

fname = 'Brian'
lname = "Nordlinger"

print("She's a great dancer")
print ('He said "Hi" to his friend')

subtotal = 14.75
subtotal_statement = 'the subtotal is ' + str(subtotal)
print(subtotal_statement)
print("My first name is " + fname + " my last name is " + lname)
print(fname[0]) #first char
print(fname[-1]) #last char

name_3 = fname * 3
print(name_3)

magician = "Harry Houdini"

if magician == "Harry Houdini":
    print("hit")

full_name = "Brian Nordlinger"
fname = full_name[0:5]
print (fname)

platform_computing = "platform computing"
p1 = platform_computing[0:8]
p2 = platform_computing[9:]
print(p1)
print(p2)

nums = [0,3,8,5,4]
print (nums)
x = nums[2]
nums[2] = nums[4]
nums[4] = x
print(nums)

