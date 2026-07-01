'''#----------------------------Electricity Consumption Category--------------------------

An electricity department categorizes households based on monthly electricity consumption. 
• Up to 100 units → Low Consumption  
• 101–300 units → Moderate Consumption  
• Above 300 units → High Consumption  
Write a Python program to display the consumption category. 
#-----------------------------------------------------------------------------
Sample Input 
245 
#-----------------------------------------------------------------------------
Sample Output 
Moderate Consumption 
#-----------------------------------------------------------------------------
'''

#-----------------------------------------------------------------------------
#--------------------------------------coding---------------------------------

#taking input from user
units = int(input("Enter monthly electricity consumption (in units): "))

#validating the units
if (units <= 0):
    exit("units must be positive.")
#validating the calculation of units based on monthly electricity consumption.
if units <= 100:
    print("Low Consumption")
elif units <= 300:
    print("Moderate Consumption")
else:
    print("High Consumption")