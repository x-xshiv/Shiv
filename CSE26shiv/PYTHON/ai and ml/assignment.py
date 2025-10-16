#1. Define Variable
name = "shiv goyal"
print(name)

#2. swapping variable
a,b = 5,10
a = a + b
b = a - b
a = a - b
print(a,b)

#3. identify data types
x = 25
print(type(x))
y = 3.14
print(type(y))
z = "Python"
print(type(z))
is_valid = True
print(type(is_valid))

#4. convert data types
num = 50
print(num)
num = float(num)
print(num)
num = str(int(num))
print(num)
string = "123"
print(string)
string = int(string)
print(string)

#5. basic arithmetic operations
x = 10
y = 3
print(int(x)+int(y))
print(float(x)-float(y))
print(int(x)*float(y))
print(x/y)
print(15%4)

#6. Boolean Expressions
x,y = 10,20
print(x>y)
print(x==y)
print(y!=x)

#7. If-else statement
x = 10
if x%2==0:
    print(f"{x} is even")
else:
    print(f"{x} is odd")

#8. user input and data processing
age = int(input("enter your age "))
if age >= 18:
    print("you are eligible for voting")
else:
    print("you are not eligible for voting yet")

#9. simple calculator
x = float(input("first number : "))
y = float(input("second number : "))
opt = str(input("what operation you need (+,-,*,/) : "))
if (opt == "+") :
    print(x+y)
elif (opt == "-") :
    print(x-y)
elif (opt == "*") :
    print(x*y)
elif (opt == "/"):
    print(x/y)
else:
    print("invalid operator")
