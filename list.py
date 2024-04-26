fruit_varities = ["mango","apple","pineapple"]
print(fruit_varities)
print(fruit_varities[0])
print(fruit_varities[0:2])
fruit_varities[2]="guvava"
print("After chainging the last value in the list")
print(fruit_varities)
print("Adding new value in the list")
fruit_varities.append("Pineapple")
print(fruit_varities)
print(fruit_varities.pop())
print(fruit_varities)
print(fruit_varities.remove("apple"))
print(fruit_varities)
fruit_varities.insert(1 , "apple")
print(fruit_varities)
fruit_varities_copy = fruit_varities.copy()
fruit_varities_copy.append("cherry")
print(fruit_varities_copy)

squared_number = [x**2 for x in range(10)]
print(squared_number)
