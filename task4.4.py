def check_if_similar(list1,list2):
    return list1 == list2




list1 = [1,2,3,4]
list1.sort()
list2 = [4,2,1,3,5]
list2.sort()

print("Are list1 and list2 similar : ",check_if_similar(list1,list2))
