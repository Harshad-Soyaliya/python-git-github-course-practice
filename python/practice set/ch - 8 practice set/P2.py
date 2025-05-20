
# Write a python program using function to convert Celsius to Fahrenheit.


Celsius = float(input("enter Celsius : "))

def convert(c):
    return (c * 9/5) + 32


Fahrenheit = convert(Celsius)
print(Fahrenheit)


