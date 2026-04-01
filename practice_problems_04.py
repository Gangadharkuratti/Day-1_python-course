# program to convert fahrenheit to celsius

temp=int(input("enter temperature (fahrenheit) : "))
cel=5/9*(temp-32)
print(f"the temperature {temp} degree farhenheit in celsius is{cel} ")

# programto calculate compound interest

p=float(input("enter principal amount : "))
r=float(input("enter annual interest rate (in %) : "))
n=float(input("enter number of times per year the interest is compounded : "))
t=float(input("enter time (years) : "))

r=r/100
amount=p * (1 + r/n) ** (n*t)
compound_interest= amount-p
print("final amount is : ",amount)
print("compound interest is : ",compound_interest)

# program to find simple interest

p=float(input("enter principal amount : "))
t=float(input("enter time (years) : "))
r=float(input("enter rate of interest(in %) : "))

simple_interest=(p*t*r)/100
print("the simple_interest is : ",simple_interest)


# program to check whether the user entered is alphabet or not

ch=input("enter character : ")
if (ch>="a" and ch<="z") or (ch>="A" and ch<="Z"):
    print("entered character is alphabet")
else:
    print("entered character is not a alphabet")    