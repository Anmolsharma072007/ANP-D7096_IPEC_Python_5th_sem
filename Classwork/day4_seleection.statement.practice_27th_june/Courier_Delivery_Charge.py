'''#----------------------Courier Delivery Charge--------------------------------------
A courier company calculates delivery charges based on the package weight. 
• Weight up to 2 kg → ₹50  
• Weight greater than 2 kg and up to 5 kg → ₹100  
• Weight greater than 5 kg → ₹180  
Write a Python program to display the delivery charge. 
Sample Input 
4 
Sample Output 
Delivery Charge = ₹100
'''

#input weight from the user

weight = float(input("Enter the package weight (in kg) : "))

#---------------------------------------------------------------------------

#validating the weight

if (weight <= 0):
    exit ("weight cannot be negative")

#-----------------------------------------------------------------------------

if (weight <= 2) :
    print ("delivery_charge = 50" )
elif (weight <= 5):
    print ("delivery_charge = 100")
else:
    print ("delivery_charge = 180")

print ("delivery_charge : " , weight )


'''output :
'''