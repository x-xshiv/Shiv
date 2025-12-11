def add(y,z):
    return y+z

def sub(y,z):
    return y-z

def multiply(y,z):
    return y*z

def divide(y,z):
    return y/z

def remain(y,z):
    return y%z

def calculator():
    while (True):
        print("1 for addition")
        print("2 for subtract")
        print("3 for multiply")
        print("4 for divide")
        print("5 for remainder")
        print("0 for exit")
        try:
            x=int(input("enter a number of operation you want to perform : "))
            if(x==0):
                break;
            y=float(input("enter 1st number : "))
            z=float(input("enter 2nd number : "))
            if(x==1):
                print(add(y,z))
            elif(x==2):
                print(sub(y,z))
            elif(x==3):
                print(multiply(y,z))
            elif(x==4):
                if(z!=0):
                    print(divide(y,z))
                else:
                    print("Zero Division Error !!")
            elif(x==5):
                if(y==int(y) and z==int(z) and z!=0):
                    print(remain(y,z))  
                else:
                    print("remainder of decimal numbers or division with not possible !!")      
            else:
                print("error, operation do not exist !!")
        except ValueError:
            print("invalid input")
        print("##########################################")
        print("##########################################")
calculator()