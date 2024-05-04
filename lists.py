# List is an ordered and mutable collection of data .  A list can contain values of multiple data-type . A list is a comma seperated values with square-brackets'[]' , list can be accessed using index values . Lists follows the 0-based indexing from left-to-right direction and we can also access the elements in the list from right-to-left by starting from -1 to n , where n is the length of the list 


import copy


print("************************ Printing list ********************************")
empty_list = []
fruits = ['orange', 'apple', 'pear', 'kiwi', 'apple']
print("The length of the list is - " , len(fruits)) # Gives the number of values in the list
print(fruits)

print("************************ Aceessing elements from list ********************************")

print(fruits[-1])
print(fruits[0])
print(fruits[-4])
print(fruits[1:3])
print(fruits[-4:])

print("************************ updating elements in list ********************************")

fruits[0] = "pineapple"
print(fruits)

print("************************ Adding elements in list ********************************")
fruits.append("90")
fruits.append("pineapple")
print(fruits)

print("************************ Nested list ********************************")

# list constains another list is called as nested list 
nested_list = [10 , 20 , [30 , 40 , 50] , 60 , 70]
print("The value at index number 2 is - ",nested_list[2]) 
print(nested_list)

print("************************ Traversing the list ********************************")
number_list = [10,20,30,40,50,60,70]
length = len(number_list)
for elements in range(length):
    print(number_list[elements] , end=" ")
print()
fruits_length =len(fruits)
for elements in range(fruits_length):
    print(fruits[elements] , end=" ")

print("************************ Copying a list ********************************")

new_number_list = number_list
print(new_number_list)

new_list = list(new_number_list)
print(new_list)

list1 = [10,30,30,40,50]
list2 = list1[1:4]
print("New List using slicing is - " , list2)

list3 = copy.copy(list1) # using copy method in copy module 
print("list 3 using copy module is - " , list3)

print("************************ Comparing a list ********************************")

L1 , L2 = [10,20,30,40,50] , [10,20,30,40,50]
L3 = [100,20,300,400,500]
print(L3 > L2)
print(L1 > L2)
print(L1 < L2)
print(L1 == L2)

print("************************ Operations on a list ********************************")

# Concatenation of list

string_list = ["apple" , "mango"]
string_list2 = ["pineapple" , "guvava" , 10]
string_list3 = string_list + string_list2
print("List after concatenation is - ",string_list3)

l1 = []
for elements in range(5):
    number = int(input("Enter the number - "))
    l1 = l1+[number]
print(l1)

# Replication of list

print("List after replication is - ",l1*2)

# Memebership Testing in list

print(1 in l1) # returns true if there is element 1 in the list , else return false

# List slicing 

list_1 = [21,45,67,89,90,54,34]
print("Slicing of the list - ")
print(list1[0:5])
print(list_1[:7])
print(list_1[4:])
print(list_1[::2])
print(list_1[::-1])
print(list_1[::])
print(list_1[5:1])
print(list_1[4::])
