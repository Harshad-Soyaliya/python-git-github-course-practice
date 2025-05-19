
# A spam comment is defined as a text containing following keywords:
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program
# to detect these spams.

comment = input("give comment : ")

comment1 = comment.upper()

print(comment1)

if( ("MAKE A LOT OF MONEY" in comment1) or ("BUY NOW" in comment1) or ("SUBSCRIBE THIS" in comment1) or ("CLICK THIS" in comment1)):
    print("SCAME!!")
else:
    print("NOT SCAME")