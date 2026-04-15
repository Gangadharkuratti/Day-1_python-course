
# program to print the power of a number

base=int(input("enter number 1 : "))
power=int(input("enter number 2 : "))

result=1
for i in range(power):
    result=result * base
print(result)    

# 1st program using no loop

num1=int(input("enter number : "))
num2=int(input("enter number : "))

result=num1**num2
print(result)