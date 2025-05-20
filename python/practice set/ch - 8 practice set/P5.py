
#  Write a python function to print first n lines of the following pattern:
# ***
# ** 
# *


number = int(input("enter number : "))

def pattern(number):
    i = 0
    for i in range(0 , number+1):
        print("*"*(number-i))

pattern(number)
