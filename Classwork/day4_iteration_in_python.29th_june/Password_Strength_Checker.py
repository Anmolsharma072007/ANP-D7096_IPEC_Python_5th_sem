'''A website requires users to create a password having at least 8 characters. Keep 
asking the user to enter a password until the entered password satisfies the minimum 
length requirement. 
Sample Output 
Enter Password: hello 
Password too short.  
Enter Password: python@123 
Password Accepted.'''

#--------------------------------------------------------------------------------
#------------------------------coding-------------------------------------------

#taking input a password from user

password = input("Enter the password: ")

#------------------------------------------------------------------------------

minimum_length = 8
while (len(password) < minimum_length):
    print("password too short")
    password = input("Enter the password: ")
print ("password accepted")
    

#------------------------------------------------------------------------------


'''
output : 
<<<<<<< HEAD
Enter the password: 12
password too short
Enter the password: 111123334255676
=======
Enter the password: 1223343221
>>>>>>> 64a74d128ed8a22e5d5d7c16a0bbdd43c22fce72
password accepted
'''