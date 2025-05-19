
# Write a program to find whether a given username contains less than 10
# characters or not.

username = input("enter username : ")

character = len(username)

if( character <= 10 ):
    print("yes" , character)
else:
    print("no" , character)

    