print("Hello World")
print('Hello World')
fruit = "Mango fruit"
slice_fruit = fruit[0]
print(slice_fruit)
slice_fruit = fruit[0:5]
print(slice_fruit)
print(slice_fruit[0:5:2])
print(fruit.lower())
print(fruit.upper())
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
