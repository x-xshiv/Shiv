try:
    x=float(input("enter number 1st : "))
    y=float(input("enter number 1st : "))
    op=str(input("enter operator (+,-,/,*) : "))
    if(op=="+"):
        print(x+y)
    elif(op=="-"):
        print(x-y)
    elif(op=="*"):
        print(x*y)
    elif(op=="/"):
        try:
            print(x/y)
        except ZeroDivisionError:
            print("denominator cannot be zero in division!!")
    else:
        print("invalid operator !!")
except ValueError:
    print("error!! invalid input")