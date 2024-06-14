from difflib import SequenceMatcher

def similar(str1,str2):
    return SequenceMatcher(None,str1,str2).ratio()



str1 = "Hello"
str2 = "Hello"
result = similar(str1,str2)
print("The similarity b/w two strings is : ",str(result))