#Write a python program to match string using re 

import re 
str1 = input("Enter a string of your choice ")
str2 = input("Enter another stirng of your choice ")
res = re.match(str1,str2)

if res:
    print("Trueee")
else:
    print("Falseeee")