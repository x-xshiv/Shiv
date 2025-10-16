n = int(input("enter how many terms you want :"))
a = 0
b = 1
i = 0
while i<n:
    if i == 0:
        print(a)
        i += 1
        continue
    elif i == 1:
        print(b)
        i += 1
        continue
    print(a+b)
    d=a+b
    a=b
    b=d
    i += 1
    
        
