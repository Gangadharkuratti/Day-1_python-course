# program to showcase operations on array

import array
a=array.array('i',[1,2,3,4,])
print(a)

# array operations

a.append(5)
print(a)  # after appending

print(a.index(3))

a.insert(3,4) # after inserting
print(a)

a.pop(4)
print(a) # after deleting 

# program to calculate the lenght of the string without using built-in function

a=input("enter string : ")
count=0
for i in (a):
    count+=1
print(count)    

# program to reverse a string

a=input("enter string : ")
l=len(a)-1
while l>=0:
    print (a[l],end=' ')
    i-=1