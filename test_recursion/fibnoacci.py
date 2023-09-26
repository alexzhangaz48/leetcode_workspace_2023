def fibnoacci(x):
    if x == 0 or x==1:
        return x
    else:
        return fibnoacci(x-2) + fibnoacci(x-1)
    
print(fibnoacci(3))