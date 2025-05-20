
# Write a program to find out whether a given post is talking about “Harry” or not

post = input("enter post  : ")

post1 = post.upper()

if ("HARRY" in post1):
    print("this post talking about harry")
else:
    print("this post not talking about harry")