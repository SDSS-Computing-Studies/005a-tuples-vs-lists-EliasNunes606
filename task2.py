#!python3

"""
Create a variable that contains an empy list.
Ask a user to enter 5 words.  Add the words into the list.
Print the list
inputs:
string 
string
string
string
string

outputs:
string

example:
Enter a word: apple
Enter a word: worm
Enter a word: dollar
Enter a word: shingle
Enter a word: virus

['apple', 'worm', 'dollar', 'shingle', 'virus']
"""

word1 = (input("Enter a word:")).strip()
word2 = (input("Enter a word:")).strip()
word3 = (input("Enter a word:")).strip()
word4 = (input("Enter a word:")).strip()
word5 = (input("Enter a word:")).strip()
word6 = []
word6.append(word1)
word6.append(word2)
word6.append(word3)
word6.append(word4)
word6.append(word5)
word6.append(word6)
print(word6)
pass