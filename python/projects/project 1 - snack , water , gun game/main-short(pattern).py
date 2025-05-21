'''

-1 :- snack 
0 :- water
1 :- gun

'''


import random

computer = random.choice([-1 , 0 , 1])

print("\n-----------------------------------------\n")

print("******************************\n  snack , water and gun game     \n******************************")
print("\nchoices(case-sensitive) :\nsnack :- s\nwater :- w\ngun :- g\n")
user = input("enter your choice : ")

choice = {
    "s" : -1 ,
    "w" : 0,
    "g" : 1
}

if user not in choice:
    print("**************************\n* you enter wrong choice *\n**************************")
else:
    user_choice = choice[user]

    show_choice = {
        -1 : "snack" ,
        0 : "water" ,
        1 : "gun" 
    }

    print(f"\nchoose choices :\ncomputer choice : {show_choice[computer]}\nyour choice : {show_choice[user_choice]}\n")

    if (computer == user_choice):
        print("***********\n*  draw   *\n***********")
    else:



        '''
        if(computer ==- 1 and user_choice == 1):  (compoter - user_choice) = -2
            print("************\n* You win! *\n************")

        elif(computer ==- 1 and user_choice == 0):  (compoter - user_choice) = -1
            print("*************\n* You Lose! *\n*************")

        elif(computer == 1 and user_choice == -1):  (compoter - user_choice) = 2
            print("*************\n* You Lose! *\n*************")
            
        elif(computer == 1 and user_choice == 0):  (compoter - user_choice) = 1
            print("************\n* You win! *\n************")

        elif(computer == 0 and user_choice == -1):  (compoter - user_choice) = 1
            print("************\n* You win! *\n************")

        elif(computer == 0 and user_choice == 1):  (compoter - user_choice) = -1
            print("*************\n* You Lose! *\n*************")

        else:
            print("*************************\n* Something went wrong! *\n*************************")

        '''



        if((computer - user_choice) == -1 or (computer - user_choice) == 2 ):
            print("*************\n* You Lose! *\n*************")
        else:
            print("************\n* You win! *\n************")



print("\n-----------------------------------------\n")


