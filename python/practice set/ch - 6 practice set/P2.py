
# Write a program to find out whether a student has passed or failed if it requires a
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
# take marks as an input from the user.

subject1 = int(input("enter 1st subect mark : "))
subject2 = int(input("enter 2nd subect mark : "))
subject3 = int(input("enter 3rd subect mark : "))

totalmarks = (100*(subject1 + subject2 + subject3))/300

if(totalmarks > 40 and subject1 >= 33 and subject2 >= 33 and subject3 >= 33 ):
    print("you are passed " , totalmarks)
else:
    print("you are fail" , totalmarks)