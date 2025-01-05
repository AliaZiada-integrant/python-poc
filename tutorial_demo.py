#!/usr/bin/env python3
animal = "Lion"
vegetable = "Apple"
mineral = "Silver"
print("Here is an animal, a vergetable, and a mineral.")
print(animal)
print(vegetable)
print(mineral)
print("-" * 80)

valueEntered = input("Please type something and press enter:")
print("You entered:")
print(valueEntered)

print("-" * 80)

# take input from user
catSaid = input()

# calculate length of input
inputLen = len(catSaid)

# print what cat syaing
print("            {0}".format("_" * inputLen))
print("          < {0} >".format(catSaid))
print("            {0}".format("-" * inputLen))
print("         /")
print("        /")
print(" /\_/\\")
print("( o.o )")
print(" > ^ <")

print("-" * 80)

perHr = 0.51
perDay = perHr * 24
perMonth = perDay * 30

print("How much does it cost to operate one server per day? {}$".format(perDay))
print("How much does it cost to operate one server per month? {}$".format(perMonth))


print("How much does it cost to operate twenty servers per day? {}$".format(perDay * 20))
print("How much does it cost to operate twenty servers per month? {}$".format(perMonth * 20))

print("How many days can I operate one server with $918? {} days".format(918 / perDay))

print("-" * 80)

miles = int(input("How far would you like to travel in miles?"))

if miles <= 30:
    print("I suggest walking to your destination.")
elif miles > 30 and miles <= 300:
    print("I suggest driving to your destination.")
else:
    print("I suggest flying to your destination.")

print("-" * 80)

to_do_items = []
def get_to_do():
    to_do_item = input("Enter a task for your to­do list. Press <enter> when done:")
    if to_do_item != "":
        to_do_items.append(to_do_item)
        get_to_do()
    else:
        print("Your To­Do List:­­­­­­­­­­­­­­­­")
        print("­­­­­­­­­­­­­­­­---------------")
        for item in to_do_items:
            print(item)

get_to_do()
print("-" * 80)

dict = {
    "Jeff" : "Is afraid of clowns." ,
    "David": "Plays the piano."     ,
    "Jason": "Can fly an airplane."
}
for key in dict:
    print("{0}: {1}".format(key, dict[key]))

print("---------")
dict["David"] = "Can't swim."

for key in dict:
    print("{0}: {1}".format(key, dict[key]))

print("---------")

dict["Jill"] = "Can hula dance."

for key in dict:
    print("{0}: {1}".format(key, dict[key]))

print("-" * 80)

with open("file.txt") as file:
    i = 0
    for line in file:
        i += 1
        print("{0}: {1}".format(i,line))
print("-" * 80)

animals = []
with open("animals.txt") as animals_file:
    for line in animals_file:
        animals.append(line)
        print(line)
    animals.sort()

with open("animals_sorted.txt", 'w') as sorted:
    for animal in animals:
        sorted.write(animal)
print("-" * 80)

from time import asctime, sleep
print(asctime())
sleep(3)
print(asctime())
print("-" * 80)
import hi_package
hi_package.say_hi()
    
    
