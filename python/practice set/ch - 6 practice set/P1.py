
# Write a program to find the greatest of four numbers entered by the user

num1 = int(input("enter number1 : "))
num2 = int(input("enter number2 : "))
num3 = int(input("enter number3 : "))
num4 = int(input("enter number4 : "))

if ((num1 >= num2) and (num1 >= num3) and (num1 >= num4)) :
    print("greatest number is : " , num1)

elif((num2 >= num1) and (num1 >= num3) and (num1 >= num4)):
    print("greatest number is : " , num2)

elif((num3 >= num1) and (num1 >= num2) and (num1 >= num4)):
    print("greatest number is : " , num3)

else:
    print("greatest number is : " , num4)

print("end program")




