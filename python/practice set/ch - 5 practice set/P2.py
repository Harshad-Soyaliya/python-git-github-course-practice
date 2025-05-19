
# Write a program to input eight numbers from the user and display all the unique numbers (once).

numbers = set() 

num1 = int(input("enter number 1 : "))
numbers.add(num1)

num2 = int(input("enter number 2 : "))
numbers.add(num2)

num3 = int(input("enter number 3 : "))
numbers.add(num3)

num4 = int(input("enter number 4 : "))
numbers.add(num4)

num5 = int(input("enter number 5 : "))
numbers.add(num5)

num6 = int(input("enter number 6 : "))
numbers.add(num6)

num7 = int(input("enter number 7 : "))
numbers.add(num7)

num8 = int(input("enter number 8 : "))
numbers.add(num8)

print("the unique numbers (once) : " , numbers)