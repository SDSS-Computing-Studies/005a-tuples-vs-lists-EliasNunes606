#!python3

"""
Create a LIST that contains the following strings, in order:
Cat
Fish
Dog
Bear
Turtle

Sort the list into alphabetical order and and then ask the user to enter a number corresponding
to the index of an element.  Print the element associated with that index.

inputs:
integer number

outputs:
string animal

example:
Enter the index for an animal:2
The animal at that index is Dog
"""

animals = ["Cat", "Fish", "Dog" , "Bear", "Turtle"]
animals.sort()
number = int(input("Enter your number:"))
if number == 0:
    print(animals[0])
elif number == 1:
    print(animals[1])
elif number == 2:
    print(animals[2])
elif number == 3:
    print(animals[3])
elif number == 4:
    print(animals[4])
