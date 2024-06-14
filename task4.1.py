list = [1,1,2,4,3,5,6,3,3,4,5,6,7,1,5,8,2]

uniquelist = []

duplicatelist = []

for i in list:
    if i not in uniquelist:
        uniquelist.append(i)
    elif i not in duplicatelist:
        duplicatelist.append(i)
        
print(duplicatelist)

