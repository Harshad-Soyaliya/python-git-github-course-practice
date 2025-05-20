
# Write a python function to print multiplication table of a given number


number = int(input("enter number : "))

def multiplicationt(num):
    for i in range(1 , 11):
        print(f"{num} x {i} = {num*i}")


multiplicationt(number)

