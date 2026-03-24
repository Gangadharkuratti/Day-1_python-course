# program to find the greatest of four numbers entered by the user

num1=int(input("Enter number1 : "))
num2=int(input("Enter number2 : "))
num3=int(input("Enter number3 : "))
num4=int(input("Enter number4 : "))

if (num1 >= num2 and num1 >= num3 and num1 >= num4):
    print("largest is ",num1)

elif(num2 >= num1 and num2 >= num3 and num2 >= num4):
    print("largest is ",num2)

elif(num3 >= num1 and num3 >=num2 and num3 >= num4):
    print("largest is ",num3)

else:
    print("largest is ",num4)


# program to find whether a student has passed or failed


marks1=int(input("Enter marks of 1st subject : "))
marks2=int(input("Enter marks of 2nd subject : "))
marks3=int(input("Enter marks of 3rd subject : "))

percent=(marks1+marks2+marks3)/300*100

if percent>=40 and marks1>=33 and marks2>=33 and marks3>=33:
    print("you have passed in exam ")
else:
    print("Better luck next time") 

print(percent)


# program to find the whether a given username contains less than 10 characters or not


name=input("Enter your name : ")
if len(name)>10:
    print("more than 10 characters")
else:
    print("less than 10 characters")    


# program to find whether a given name is present in list or not

name=input("Enter our name")
l=["diya","naveen","manoj","guru"]

if (name in l):
    print("yes your name is in the list")

else :
    print("no your name is not there in the list")


# program to print grade of the students


marks=int(input("Enter marks : "))
if marks < 0 and marks >100:
    print("invalid marks")
elif marks>=90 and marks<=100:
    print("excellent")
elif marks>=80 and marks<90:
    print("grade : A")
elif marks>=70 and marks<80:
    print("grade : B")
else:
    print("grade : F")        
 
    