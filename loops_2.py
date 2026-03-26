# program to find the factorial of a number 

num=int(input("enter  number : "))
fact=1
for i in range(1,num+1):
    fact=fact*i
print(f"factorial of {num} is {fact}")   


# program to print the odd number star pattern 

num=int(input("enter  number : "))
for i in range(1,num+1):
    print(" " * (num-i), end="")
    print("*" * (2*i-1),end="" )
    print("")  


# program to print the simple star pattern

num=int(input("enter  number : "))
for i in range(1,num+1):
    print("*"*i,end="")
    print("")


# program to print the table of a number reverse

num=int(input("enter  number : "))
for i in range(1,11):
    print(f"{num}x{11-i}={num*(11-i)}")
    
    