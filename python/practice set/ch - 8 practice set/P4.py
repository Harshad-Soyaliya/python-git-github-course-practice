
# Write a recursive function to calculate the sum of first n natural numbers.

# 5 = 5 + 4 + 3 + 2 + 1 

number = int(input("enter number : "))

def natural(number):
    if number==1:
        return 1
    return natural(number-1)+number



naturalnumbr = natural(number)
print("natural number sum is : " ,naturalnumbr )

