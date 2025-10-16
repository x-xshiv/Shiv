def function():
    try:
        x=int(input("type any integer :- "))
        print(x)
    except ValueError:
        print("error type valid integer!!")
        return function()
