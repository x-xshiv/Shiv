def bio():
    x={
        'name':a,
        'age':b,
        'nationality':c,
        'location':d,
        'is_married':e,
        'highest_degree':f
        }
    key=list(x.keys())
    value=list(x.values())
    for i in range (len(x)):
        print(f"{(i+1)}. {key[i]} = {value[i]}")
a=str(input())
b=int(input())
c=str(input())
d=str(input())
e=bool(input())
f=str(input())
bio()
