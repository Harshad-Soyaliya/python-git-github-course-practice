
# Write a program which finds out whether a given name is present in a list or not.

list = ["harshad" , "mansi" , "parth" , "mohit" , "dip"]

name = input("enter name : ")

n = name.lower()

if n in list:
    print("prsent and your name is : " , n)
else:
    print("not prsent and your name is : " , n)
    
