a = int(input("Enter a number "))
b = int(input("Enter another number "))

double = lambda x:x*x
add = lambda x,y : x+y

print(f"Double of {a} is ",double(a))
print(f'Sum and {a} and {b} is',add(a,b))