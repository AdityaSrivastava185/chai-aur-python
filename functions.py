import math
# Functions are block of codes which are used to pefeorm same task multiple times in the program by just calling the name of the function without the need to write the code block again and again in the program 

# Syntax of the function 
def square_of_num(number):
    return (number**2)

sqaure_number = square_of_num(2)
print(sqaure_number)

# Now let us consider the function and understand the basics of function 
# To define the function we use the keyword "def" and then we declare the "name of the function" then after declaring the name of the function we put the "()" and to create the block of the function we put the ":" , The "()" can be empty or we can also declare the parameters inside the "()" , Here to take the integer input we declared a variable inside the "()" which is "number" , and this only accpets the value of interger data type , Inside the code block of the function we use the keyword "return" to return the value from the function and we can store the return value in another variable outside the function , return is responsible to terminate the function and return the value , after the return statement the code will not be executed inside the code block of the function and it also may cause the error in the program 

def add(num_one , num_two):
    return (num_one + num_two)

add_numebr = add(1 , 2)
print(add_numebr)

def multiply(p1 , p2):
    return (p1*p2)

print(multiply(8,2))
print(multiply('a',2))
print(multiply(2,'a'))

def circle_stats(radius):
    area =  math.pi * radius**2
    circumference = 2 * math.pi * radius
    return (area , circumference)

print(circle_stats(2))


def greeting(name="User"):
    return "Hello " , name

print(greeting("Sir"))

cube = lambda x : x**3
print(cube(3))

def sum_all(*args):
    return sum(args)

print(sum_all(1,2))
print(sum_all(1,2,3))
print(sum_all(1,2,3,4,5))

def print_kwargs(first_name , last_name):
    print("First Name" , first_name , "Last name" , last_name)
print_kwargs(first_name = "Hello" , last_name = "World")

def print_kwargs(**kwargs):
    for key , value in kwargs.items():
        print(f"{key} : {value}")
print_kwargs(first_name = "Hello" , last_name = "World" , age="10")

def even_generator(number):
    for i in range(0,number+1,2):
        yield i

for i in even_generator(10):
    print(i)


def factorial(number):
    if number == 1 :
        return number 
    return number * factorial(number - 1)
print(factorial(5))