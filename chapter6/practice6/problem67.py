# Write a program to find out whether a given post is talking about "Sabina" or not.


post = input("Enter the post: ")


if("sabina" in post.lower()):
    print("This post is talking about sabina")

else:
    print("This post is not talking about sabina")