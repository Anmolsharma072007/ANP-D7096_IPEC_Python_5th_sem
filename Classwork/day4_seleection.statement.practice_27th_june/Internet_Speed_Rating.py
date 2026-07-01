'''#-------------------------Internet Speed Rating-------------------------------------------

An Internet Service Provider categorizes connection quality based on download speed. 
• Less than 25 Mbps → Slow  
• 25–99 Mbps → Good  
• 100 Mbps or above → Excellent  
Write a Python program to display the connection quality. 
#--------------------------------------------------------------------------
Sample Input 
120 
#--------------------------------------------------------------------------
Sample Output 
Excellent Connection
#--------------------------------------------------------------------------
'''

#--------------------------------------------------------------------------------
#---------------------coding-----------------------------------------------------

#input from user

connection_quality = int(input("Enter connection quality (in Mbps) : "))
#validating the connection quality 
if (connection_quality <= 0 ):
    exit("connection_quality cannot be negative.")
#validating the user connection_quality based on download speed
if (connection_quality <= 25):
    print("slow")
elif (connection_quality <= 99):
    print("good")
else:
    print ("excellent")