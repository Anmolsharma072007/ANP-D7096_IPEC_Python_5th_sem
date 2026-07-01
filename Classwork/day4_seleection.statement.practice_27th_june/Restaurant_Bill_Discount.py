'''----------------restaurant bill discount-----------------------------------

A restaurant offers discounts based on the total bill amount. 

• Bill below ₹1000 → No Discount  
• ₹1000–₹2999 → 10% Discount  
• ₹3000 or more → 20% Discount  

Write a Python program to determine the applicable discount. 

#-----------------------------------------------------------------------
Sample Input 
3200 

#-----------------------------------------------------------------------
Sample Output 
20% Discount Applied

#-----------------------------------------------------------------------
'''

#-----------------------------------------------------------------------
#------------------------coding-----------------------------------------------

#taking input from user

total_bill_amount = float(input("Enter a total bill amount: "))

#-----------------------------------------------------------------------

#validating the toatal bill amount

if (total_bill_amount <= 0):
    exit("total_bill_amount must be positive")

#-----------------------------------------------------------------------

#validating the discount based on the total bill amount

if (total_bill_amount < 1000):
    discount_amount = 0
    print("no discount")
elif (total_bill_amount <= 2999):
    discount_amount = total_bill_amount * 0.10
    print ("10% Discount Applied")
else:
    (total_bill_amount >= 3000)
    discount_amount = total_bill_amount * 0.20
    print ("20% Discount Applied")

#-----------------------------------------------------------------------

print("discount amount =" , discount_amount)

#-----------------------------------------------------------------------


'''
output :
'''