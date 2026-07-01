'''#-----------------------Number Guessing Game----------------------------------------
<<<<<<< HEAD

=======
>>>>>>> 64a74d128ed8a22e5d5d7c16a0bbdd43c22fce72
A secret number is 37. 
Keep asking the user to guess the number until the correct number is entered. 
Display whether the entered number is too high, too low, or correct.
'''

<<<<<<< HEAD
#-----------------------------------------------------------------------------


=======
>>>>>>> 64a74d128ed8a22e5d5d7c16a0bbdd43c22fce72
#taking input numbers from user

numbers = int(input("Enter the guessing number: "))

<<<<<<< HEAD
#-----------------------------------------------------------------------------

=======
>>>>>>> 64a74d128ed8a22e5d5d7c16a0bbdd43c22fce72

#validating the user guessing number until the correct number is entered

secret_num = 37
while (numbers != secret_num):
    if (numbers < secret_num):
        print("the entered number is too low ")
        numbers = int(input("Enter the guessing number: "))
    else:
        print("the entered number is too high ")
        numbers = int(input("Enter the guessing number: "))
<<<<<<< HEAD
print("the entered number is correct ")


#-----------------------------------------------------------------------------


'''
output :
Enter the guessing number: 22
the entered number is too low 
Enter the guessing number: 43
the entered number is too high 
Enter the guessing number: 37
the entered number is correct 
'''
=======
print("the entered number is correct ")
>>>>>>> 64a74d128ed8a22e5d5d7c16a0bbdd43c22fce72
