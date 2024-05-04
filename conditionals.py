# Conditionals in python helps in dynammic decisions and code branching ,  If-Else statements are fundamental conditionals, providing a way to execute different blocks of code based on specific conditions which executes the program when the condition is true when it's inside the 'if' block and on the other hand runs the other block of code when the condition is not true when it's inside of the 'else' block

print("*****************************************************************")

number = int(input("Enter the number - "))
if(number >= 18):
    print("The person is eligible to vote")
else:
    print("The person is not eligible to vote")

print("*****************************************************************")

number2 = int(input("Enter the number - ")) # User can have more than one if blocks
if(number2 > 0):
    print("The number is positive")
elif(number2 < 0):
    print("The number is negative") # elif is the short-term for 'else-if' 
elif(number2 == 0):
    print("The number is neither positive nor negative")

print("*****************************************************************")

number3 = int(input("Enter the number - "))
if(number3 % 2 == 0):
    print("The number is even")
if(number3 % 2 != 0):
    print("The number is odd")

print("*****************************************************************")
number4 = int(input("Enter the number - "))
if(number4 % 2 == 0):
    print("The number is even")
else:
    print("The number is odd") # else block only runs when all the if conditions are false

print("*****************************************************************")

number5 = int(input("Enter the number - "))
if(number5 > 0):
    if(number5 % 2 == 0): #nested if statement is the 'if inside if statement' 
        print("The number is positive and even")
    if(number % 2 != 0):
        print("The number is positive and odd ")
else:
    print("The number is negative")

print("*****************************************************************")
number6 = 10
if number6 < 15: print("i is less than 15") # short-hand if statement