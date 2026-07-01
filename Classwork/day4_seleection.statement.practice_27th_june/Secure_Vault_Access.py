'''--------------------Secure Vault Access--------------------------------------------
A digital vault can only be opened if the user enters the correct security code. 
Write a Python program that accepts the entered security code. If the entered code is 7890,
display: 
#-----------------------------------------------------------------------------
"Access Granted to the Vault." 
Otherwise, do nothing. 
Sample Input 7890 
Sample Output 
Access Granted to the Vault.'''


#input from the user
security_code = int(input("Enter the correct security code:"))
#validating the security code
if (security_code <= 0):
    exit("the security_code must be positive")
#validating the user enters security code
if (security_code == 7890):
    print ("Access Granted to the Vault.")
 