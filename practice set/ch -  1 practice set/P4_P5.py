
# Write a python program to print the contents of a directory using the os module.
# Search online for the function which does that.

# Label the program written in problem 4 with comments. 




# import os module/library
import os

# create variable for store path
dictonary_path = '/'

# create variavle for store list paths
conents = os.listdir(dictonary_path)

# print listed path using for loop
for iteam in conents :
    print(iteam)
