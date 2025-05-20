
# Write a program to find the sum of first n natural numbers using while loop.


number = int(input("enter number : "))

i=1
sum=0

for i in range(1 , number+1):
    sum = sum + i
    
print(sum)

