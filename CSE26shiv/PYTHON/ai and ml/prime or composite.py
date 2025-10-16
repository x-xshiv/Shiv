print("|| program to print all prime and composite number from 1 to user desired limit ||")
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
            
