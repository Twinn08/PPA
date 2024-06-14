#FIBONACCI SERIES
def fibo_series(n):
    if n <= 1:
        return n
    else:
        return fibo_series(n-1) + fibo_series(n-2)




terms = int(input("Enter the number of terms : "))
if(terms <= 0):
    print("Enter a positive number")
else:
    print("fibo series is : ")
    for i in range (terms):
        print(fibo_series(i))
