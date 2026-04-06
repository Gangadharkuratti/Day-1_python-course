# program to print reverse of a number

num=int(input("enter number : "))
rev=0
while (num>0):
    digit=num%10
    rev=(rev*10)+digit
    num=num//10
print("reversed number ",rev)


# program to print the count of digits

num = int(input("Enter number: "))

count = 0

while num > 0:
    num = num // 10  
    count = count + 1

print("Number of digits =", count)


  
     