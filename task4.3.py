my_tuple = ("red","yellow","green")

new_tuple = my_tuple + ("Golden","silver","Blue")

print(new_tuple)

tuple_length = len(my_tuple)

print("The length of the tuple is : ",tuple_length)

item_to_check = "aaaa"

if item_to_check in my_tuple:
    print(f"{item_to_check} is present in the tuple")
else:
    print(f"{item_to_check} is not in the tuple")
    
    
for item in my_tuple:
    print(item)
    
    
    
    