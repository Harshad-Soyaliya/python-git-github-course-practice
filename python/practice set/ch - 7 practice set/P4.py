
# Write a program to find whether a given number is prime or not

number = int(input("enter number : "))

for i in range(2 , number):
    if (number%1) == 0 :
        print("this numebr is not prime")
        break
else:
    print("this numebr is  prime")


