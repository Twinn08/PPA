string = "Hello this is Abhishek M L, or 123"

w,d,u,l = 0,0,0,0

l_w = string.split()

w = len(l_w)

for c in string:
    if(c.isdigit()):
        d = d+1
    
    if(c.isupper):
        u = u + 1
        
    if(c.islower):
        l =  l + 1
        
        
        
print("Number of words : ",w)
print("Number of digits : ",d)
print("Number of uppercase : ",u) 
print("Number of lowercase : ",l)       

