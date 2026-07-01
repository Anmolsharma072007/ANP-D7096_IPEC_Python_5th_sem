'''----------------Electricity Bill Discount-------------

An electricity provider offers a 10% discount on the total bill amount if the customer's bill is ₹5,000 
or more. Otherwise, no discount is applied. 
Write a Python program to accept the total bill amount from the user and display the final amount to 
be paid. 
#------------------------------------------------------------
Sample Input 1 
Enter the electricity bill amount: 6200
#-------------------------------------------------------------
Sample Output 1 
Discount Applied! Final Bill Amount: ₹5580.0 
#--------------------------------------------------------------
Sample Input 2 
Enter the electricity bill amount: 4200
#-------------------------------------------------------------
Sample Output 2 
No Discount Applied! Final Bill Amount: ₹4200 
'''

#input from user
bill_amount = float(input("Enter the electricity bill amount(in Rs):"))
#validating of bill amount 
if (bill_amount <= 0):
    exit ("electricity bill amount must be positive")
#-------------------------------------------
if (bill_amount >= 5000):
    print("Discount applied")
    print("final bill amount = bill amount- (bill amount * 0.10)")
else:
    print("no discount applied")
    print("final_bill_amount = ",bill_amount)

'''output :
bill_amount : 3000
no discount applied'''