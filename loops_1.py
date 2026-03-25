# program to print a table of a number entered by the user using for loop

num=int(input("enter number : "))

for i in range(1,11):
    print(f"{num}x{i}={num*i}")


# program to greet persons in list 'l' which starts with 's'

l=["nikhil","sania","sanju","diya"]

for name in l:
    if name.startswith("s"):
        print(f"hello{name}")

# problem 1 using while loop


num=int(input("enter number : "))
i=1
while(i<11):
    print(f"{i}x{num}={i*num}")
    i=i+1

# program to find whether a given number is prime or not

num=int(input("enter number : "))
for i in range (2,num):
 if  num%i==0:
    print("not a prime number")
else:
    print("prime number")    


# program to find the sum of first n natural numbers


num=int(input("enter number: "))
i=1
sum=0
while(i<=num):
   sum=sum+i
   i=i+1
print(sum)   





