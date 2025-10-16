#1. Positive, Negative, or Zero?
def function1():
    try:
        n = int(input("enter your number : "))
        if n>0:
            print("Positive")
        elif n<0:
            print("Negative")
        else:
            print("Zero")
        return index()
    except ValueError:
        print("ERROR! please, enter a integer type value")
        return function1()

#2. The Number Game
def function2():
    try:
        n = int(input("enter your number : "))
        if n%3==0 and n%5==0:
            print("FizzBuzz")
        elif n%3==0:
            print("Fizz")
        elif n%5==0:
            print("Buzz")
        else:
            print(n)
        return index()
    except ValueError:
        print("ERROR! please, enter a integer type value")
        return function2()
        
#3. Movie Ticket Price Checker
def function3():
    try:
        age = int(input("Enter your age : "))
        if age < 0:
            print("age should be a positve number")
            return function3()
        elif age < 5:
            print("Free")
        elif age <= 12:
            print("₹100")
        elif age <= 60:
            print("₹150")
        else:
            print("₹120")
        print("Thank you for visiting!")
        return index()
    except ValueError:
        print("ERROR! please, enter a integer type value")
        return function3()

#4. Multiplication Table Maker
def function4():
    try:
        n = int(input("Enter a Number : "))
        if n <= 0:
            print("please, enter a positive integer")
            return function4()
        for i in range(1,11):
            print(f"{n} x {1} = {n*i}")
        return index()
    except ValueError:
        print("ERROR! please, enter a integer type value")
        return function4()

#5. Print the Stars
def function5():
    try:
        n = int(input("Enter a Number : "))
        string = "*"
        if n<=0:
            print("please, enter a positive number")
            return function5()
        for i in range(1,n+1):
            print(string*i)
        return index()
    except ValueError:
        print("ERROR! please, enter a integer type value")
        return function5()

#6. Add It Up!
def function6():
    sum = 0
    for i in range(1,101):
        sum += i
    print(f"sum of numbers from 1 to 100 is {sum}")
    return index()

#7. Countdown Time!
def function7():
    try:
        n = int(input("Enter a Number : "))
        if n<=0:
            print("please, enter a positive number")
            return function7()
        for i in range(n,0,-1):
            print(i)
        print("Liftoff! 🚀")
        return index()
    except ValueError:
        print("ERROR! please, enter a integer type value")
        return function7()
#8. Secret Code Detector
def function8():
    password = "python123"
    x = input("Password Required : ")
    count = 0
    if x == password:
        print("Access Granted ✅")
        return index()
    else:
        print("Wrong password! Try again 🔐")
        return function8()

# this is where we can access all function.         
def index():
    print("function 1 is Positive, Negative, or Zero?")
    print("function 2 is The Number Game")
    print("function 3 is Movie Ticket Price Checker")
    print("function 4 is Multiplication Table Maker")
    print("function 5 is Print the Stars")
    print("function 6 is Add It Up!")
    print("function 7 is Countdown Time!")
    print("function 8 is Secret Code Detector")
    try:     
        x = int(input("enter a function number you want to use : "))
        if x == 1:
            return function1()
        elif x == 2:
            return function2()
        elif x == 3:
            return function3()
        elif x == 4:
            return function4()
        elif x == 5:
            return function5()
        elif x == 6:
            return function6()
        elif x == 7:
            return function7()
        elif x == 8:
            return function8()
        else:
            print("function do not exist. please enter a valid number")
            return index()
    except ValueError:
        print("function do not exist. please enter a valid number")
        return index()

# calling the index function.
index()
        
        
