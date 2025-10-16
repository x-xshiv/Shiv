
def function1():
        try:
                x = int(input("enter number of rows = "))
                y = int(input("enter number of columns = "))
                n = int(input("enter the gap you want in between = "))
                if (x <= 0 or y <= 0 or n <=0):
                        print("give a positive integer value which is greater than zero")
                        return function1()
                else:
                        for i in range(0,x):
                                bag = ""
                                for j in range(0,y):
                                        if i%n==0:
                                                bag=bag + "*"
                                        else:
                                                if (j==0 or j == y-1):
                                                        bag = bag + "*"
                                                else:
                                                        bag = bag + " "
                                print(bag)
        except ValueError:
                print("error!! please enter a valid integer only value")
                return function1()
        try:
                z = int(input("if you want to continue using this function type 0 or if you want use another function just press enter :- "))
                if (z==0):
                        return function1()
                if (z>0 or z<0):
                        index()
        except ValueError:
                index()
                   
def function2():
        try:
                x = int(input("enter a limit from 1 to desired number :- "))
                prime = 0
                composite = 0
                if(x<1):
                        print("error enter a positive integer !!")
                        return function2()
                else: 
                        for i in range (1,x+1):
                            factors = 0
                            for j in range (1,x+1):
                                if (i%j==0):
                                    factors += 1
                            if (factors == 2):
                                print(f"{i} is a prime number")
                                prime += 1
                            else:
                                if (factors == 1):
                                    print(f"{i} is neither prime nor composite")
                                else:
                                    print(f"{i} is a composite number")
                                    composite += 1
                        print(f"there are {prime} prime numbers in given limit")
                        print(f"there are {composite} composite numbers in given limit")
        except ValueError:
                print("error!! please enter a valid integer only value")
                return function2()
        try:
                z = int(input("if you want to continue using this function type 0 or if you want use another function just press enter :- "))
                if (z==0):
                        return function2()
                if (z>0 or z<0):
                        index()
        except ValueError:
                index()
        
def function3():
        try:
                x=str(input("enter the text you want to repeat :- "))
                y=int(input("how many time you need it to be repeated :- "))
                z=str(input("type 0 if you want to show numbers too or else just enter :- "))
                if(y<1):
                        print("error, please enter a postive integer !!")
                        return function3()
                else:
                        for i in range (1,y+1):
                                if (z!="0"):
                                        print(x)
                                else:
                                        print(f"{i}--> {x}")
        except ValueError:
                print("error!! please enter a correct value type")
                return function3()
        try:
                p = int(input("if you want to continue using this function type 0 or if you want use another function just press enter :- "))
                if (p==0):
                        return function3()
                if (p>0 or p<0):
                        index()
        except ValueError:
                index()
def function4():
        try:
                n=int(input("enter a positive odd integer :- "))
                mid = n//2
                if (n%2==0 or n<=0):
                        print("error, please enter a positive odd number !!")
                        return function4()
                else:
                        for i in range(mid+1):
                                spaces = " " * (mid - i)
                                stars = "*" * (i*2 + 1)
                                print(spaces + stars)
                        for i in range(mid-1,-1,-1):
                                spaces = " " * (mid - i)
                                stars = "*" * (i*2 + 1)
                                print(spaces + stars)
        except ValueError:
                print("error!! please enter a correct value type")
                return function4()
        try:
                p = int(input("if you want to continue using this function type 0 or if you want use another function just press enter :- "))
                if (p==0):
                        return function4()
                if (p>0 or p<0):
                        index()
        except ValueError:
                index()

def index():
        try:
                print("function 1 = ladder or box pattern")
                print("function 2 = prime or composite number")
                print("function 3 = text repeatation code")
                print("function 4 = diamond pattern")
                x = int(input("enter no. of function you need to use :- "))
                if(x==1):
                        function1()
                if(x==2):
                        function2()
                if(x==3):
                        function3()
                if(x==4):
                        function4()
                if(x>4 or x<1):
                        print("error, function do not exist !!")
                        return index()
        except ValueError:
                print("error, function do not exist !!")
                index()
index()
            


