'''write the program to input 10 numbers.'''

list= []
print ( "the 10 numbers are:")

for i in range(1,11):
    num= int(input())
    list.append(num)

print ("numbers are : " , list)

index= int(input("enter the index you want to delete: "))
list.pop(index)
print ("numbers are : " , list)


'''output
the 10 numbers are:
1
2
3
4
5
6
7
8
numbers are :  [1, 2, 3, 4, 5, 6, 7, 8]
enter the index you want to delete: 2
numbers are :  [1, 2, 4, 5, 6, 7, 8]
'''