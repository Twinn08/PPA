my_list = []

my_list.insert(0,10)
my_list.insert(1,20)
my_list.insert(2,40)
my_list.insert(3,100)
print(my_list)

my_list.append(110)
my_list.append(200)
print(my_list)


my_list.remove(10)
print(my_list)

print("The length of my_list is : ",len(my_list))

popped = my_list.pop()
print("Popped element : ",popped)
print(my_list)

my_list.clear()

print(my_list)

