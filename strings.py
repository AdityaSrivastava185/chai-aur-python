# Strings in python 
'''
 In Python, a string is a fundamental data structure that represents a sequence of characters
 A string is a collection of characters arranged in a specific order.It can include letters, digits, symbols, spaces, and even special characters.
For example, "hello" is a string containing the characters 'h', 'e', 'l', 'l', and 'o'.

Characteristics of Strings:-
1. Immutable:- Once you create a string, you cannot modify it directly. Strings are immutable data types.

2. Encoding: Internally, Python converts strings into binary (1s and 0s) for the computer to handle. This process, called encoding, uses Unicode.

Strings can be defined using single quotes (' '), double quotes (" "), or triple double quotes (""" """)

For example - 
name = "Name"
name2 = 'Name2'

'''

print("Hello World")
print('Hello World')

# Declaring a value of string data type 

fruit = "Mango fruit"

# Accessing the characters of the string 
slice_fruit = fruit[0]
print(slice_fruit)
slice_fruit = fruit[0:5]
print(slice_fruit)
print(slice_fruit[0:5:2])
# Changing the case of the string into lower case
print(fruit.lower())
# Changing the case of the string into lower case
print(fruit.upper())
# some of the basic string operations 
print("Strip String = " , fruit.strip())
print(fruit.replace("Mango" , "Apple"))
fruit = "Mango , Apple ,  Guvava , Pineapple"
print(fruit.split(" , "))
fruit = "Mango Fruit"
print(fruit.find("i"))
print(fruit.find("Mango"))
fruit = "Mango fruit fruit fruit fruit"
fruit_type = "String"
String = "The type of the fruit is = {}"
print(String.format(fruit_type))
print(fruit.count("fruit"))
fruit_variety = ["Mango" , "Apple" , "Pineapple" , "Guvava"]
print(fruit_variety)
print("-".join(fruit_variety))
print("length of the string is = ",len(fruit))
for letter in fruit:
    print(letter)




number_list = "0123456789"
print(number_list[:7])
print(number_list[0:7:2])
print(number_list[2:5:2])
print(number_list[:9:-1])
