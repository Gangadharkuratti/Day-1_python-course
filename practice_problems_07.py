# program to print the fibonacci series

num=5
n1,n2=0,1
print("fibonacci series",n1,n2,end=" ")
for i in range(2,num):
    n3=n1+n2
    n1=n2
    n2=n3
    print(n3,end=" ")
print()    

# program to print the sum of the digits

num = int(input("Enter number: "))

sum = 0

while num > 0:
    digit = num % 10      
    sum = sum + digit     
    num = num // 10       

print("Sum of digits =", sum)