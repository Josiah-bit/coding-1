# User Defined Functions - code instructions that YOU write/create 

# How To Write A Function: 
# Part 1 - Function Definition \
def welcome_message():
    print ('Hello Good Morning.')  
#()-> round brakets/parameters 

# Part 2 - Function Invocation/ call 
welcome_message() 
# A function's name+() must be called to activate it

def calculate():
    num1 = int(input ("please type in a number"))
    num1 += 10 
    print(num1) 

calculate() 

# Parameters and Arguements 

# Parameters and Arguements are data that can be passed inside of a function to folloow instructsions 
#num1 and num2 aer parameters. These are placeholders for data 
#This placeholder data are NOT REAL. It is intended to be resersed for actual data

def findAvg(num1,    num2):
    print(num1 +num2) 

#Arguements are REAL data in the fuction call  
#There must be the same number if arguements as there are parameters 
#Arguement == real data --> in court, to make a arguement, you need facts 

findAvg(10,9)