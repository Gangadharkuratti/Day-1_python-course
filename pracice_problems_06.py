# program to print tables of a number

num=int(input("enter number : "))
for i in range(1,11):
    print(f"{num}x{i}={i*num}")

# program to print numbers from 1 to n 


num=int(input("enter number : "))
for i in range(1,num+1):
    print(i)

# program to print even numbers


num=int(input("enter number : "))
for i in range(1,num+1):
   if i%2==0:
    print(i)

# program to print odd numbers


num=int(input("enter number : "))
for i in range(1,num+1):
   if i%2!=0:
    print(i)
