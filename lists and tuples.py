# program to store four fruits in a list entered by the user

fruits=[]
f1=input("enter the fruit name of your choice")
fruits.append(f1)
f2=input("enter the fruit name of your choice")
fruits.append(f2)
f3=input("enter the fruit name of your choice")
fruits.append(f3)
f4=input("enter the fruit name of your choice")
fruits.append(f4)
print(fruits)


# program to accept marks and sort them

marks=[89,90,76,37,69,70]
print(marks) # Before sorting
marks.sort()
print(marks) # After sorting


# program to check that tuple cannot be changed 

fruits=("orange","apple","banana","papaya","watermelon","chiku","green apple")
print(fruits)
fruits[2] ="apple"
print(fruits)

# program to sum a list with 4 numbers

numbers=[1,2,3,4]
print(numbers)
total= sum(numbers)
print("sum is",total)

# program to count the number of zeros in the following tuple

a=(7,0,8,0,0,9)
print(a)
print(a.count(0))


