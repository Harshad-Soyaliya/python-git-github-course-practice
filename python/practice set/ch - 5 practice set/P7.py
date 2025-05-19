
# If the names of 2 friends are same; what will happen to the program in problem 6?

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