
# Write a program using functions to find greatest of three numbers



num1 = int(input("enter number : "))
num2 = int(input("enter number : "))
num3 = int(input("enter number : "))


def gnumber(num1 , num2 , num3):
    if (num1 >= num2 and num1>=num3):
        print("gratet number is : " , num1)
    elif(num2 >= num1 and num2 >= num3):
        print("gratet number is : " , num2)
    elif(num3 >= num1 and num3 >= num2):
        print("gratet number is : " , num3)


gnumber(num1 , num2 , num3)







