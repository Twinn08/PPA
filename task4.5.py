dict = {
    "name" : "Abhishek",
    "age"  : 21,
    "city" : "Bangalore" 
    
}

#1)
print("Dict items : ")
print(dict)

#2)
print("Accessing items : ")
print(f"Name: {dict['name']}")
print(f"Age: {dict['age']}")

#3)
print("Using get()")
name = dict.get("name")
print(f"Name: {name}")

#4)
print("Changing values : ")
dict["name"] = "Abhi"

print("Updated dictionary items:")
print(dict)

#5)
print("Using len() function")
print("The length of the dict is : ",len(dict))
