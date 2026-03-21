# python program to display a user entered name followed by good afternoon using input function.

name=input("Enter your name : ")

print(f"Good afternoon {name}")


# program to detect double space in a string

sentence= "Hello  good afternoon nikhil "
print(sentence.find("  ")) 


# program to replace double space from program 2 with single space

sentence= "Hello  good afternoon nikhil "
print(sentence.replace("  "," "))


# program for string slicing

name= "Gangadhar"
print(name[0:7]) 
print(name[:7])  # is same as print(name[0:7])
print(name[0:])
print(name[:9])  # is same as print(name[0:9])

