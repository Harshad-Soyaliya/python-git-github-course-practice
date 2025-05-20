
# Write a program to print the following star pattern.
# * * *
# *   * 
# * * *


number = int(input("enter number : "))

for i in range(1 , number+1):
    if (i==1 or i == number):
        print("*"* number , end="")
    else:
        print("*" , end="")
        print(" "*(number-2) , end="")
        print("*" , end="")
    print("")
