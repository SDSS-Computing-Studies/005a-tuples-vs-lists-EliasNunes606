#!python3
"""
Print the list named "people"
Ask the user to enter a word from the list
Ask the user to enter another word
Replace the first word with the second word.

inputs:
string
string

outputs:
list

example:
['Alain', 'Brian', 'Chris', 'Justin', 'Angela', 'Rick']
Choose a person from the list to replace:Rick
Enter the replacement:Dan
['Alain', 'Brian', 'Chris', 'Justin', 'Angela', 'Dan']

"""
homies = ['Alain', 'Brian', 'Chris', 'Justin', 'Angela', 'Rick']
replacement = str(input("Choose a person from the list to replace"))
replacement2 = str(input("Enter the name you want to replace it with"))
x = homies.index(replacement)
homies.pop(x)
homies.insert(x,replacement2)
print(homies)