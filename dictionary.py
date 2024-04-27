# Dicrionary in python 
name_types = {
    "f_name" : "first name",
    "l_name":"last name",
    "age":"number",
}
print(name_types)
print(name_types["f_name"])
print(name_types.get("l_name"))
name_types["age"] = "int"
print(name_types)
for n in name_types:
    print(n , name_types[n])

for key,values in name_types.items():
    print(key,values)
if "age" in name_types:
    print("The age is present in the dictionary")

print(len(name_types))

name_types["community"] = "true"
print(name_types)

name_types.pop("community")
print(name_types)

name_types.popitem()
print(name_types)

del name_types["l_name"]
print(name_types)

name_types_copy = name_types.copy()
print(name_types_copy)

sqaured_dictionary = {x:x**2 for x in range(6)}
print(sqaured_dictionary)

sqaured_dictionary.clear()
print(sqaured_dictionary)

