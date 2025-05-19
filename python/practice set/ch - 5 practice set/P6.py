
# Create an empty dictionary. Allow 4 friends to enter their favorite language as
# value and use key as their names. Assume that the names are unique

language = {}

name1 = input("enter your name : ")
lang1 = input("enter your favourite language : ")
language.update({ name1 : lang1 })

name2 = input("enter your name : ")
lang2 = input("enter your favourite language : ")
language.update({ name2 : lang2 })

name3 = input("enter your name : ")
lang3 = input("enter your favourite language : ")
language.update({ name3 : lang3 })

name4 = input("enter your name : ")
lang4 = input("enter your favourite language : ")
language.update({ name4 : lang4 })

print(language)
