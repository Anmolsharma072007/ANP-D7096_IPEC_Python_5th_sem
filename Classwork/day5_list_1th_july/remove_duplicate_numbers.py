'''write a program to check to create a list of 20 numbers given bt the user. ask the user to input 
any other number. if the number is present in the list then remove its all duplicate appearence 
from the list.'''

#taking input numbers from user

list =[]
print ( "the 20 numbers are:")

#using iteration
for i in range(20):
    num= int(input())
    list.append(num)

print ("numbers are : " , list)

num = int(input("Enter the numbers to be removed: "))
if num in numbers:
    while num in numbers:
        numbers.remove(num)
    print("Updated list:", numbers)
else:
    print("Number is not present in the list.")
