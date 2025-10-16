
def function1():
        x = int(input("enter number of rows = "))
        y = int(input("enter number of columns = "))
        n = int(input("enter the gap you want in between = "))
        if (x <= 0 or y <= 0 or n <=0):
                print("give a positive integer value which is greater than zero")
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
        z = int(input("if you want to continue using this program type 0 or if you want to use another function type 1 :- "))
        if (z==0):
                return function1()
        if (z==1):
                index()

def function2():
        x = int(input("enter a limit from 1 to desired number :- "))
        prime = 0
        composite = 0
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
        z = int(input("if you want to continue using this program type 0 or if you want to use another function type 1 :- "))
        if (z==0):
                return function2()
        if (z==1):
                index()

def index():
        print("function 1 = ladder or box pattern")
        print("function 2 = prime or composite number")
        x = int(input("enter no. of function you need to use :- "))
        if(x==1):
                function1()
        if(x==2):
                function2()
        if(x>2):
                print("function do not exist")
index()
            


