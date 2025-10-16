def first():
    global x
    print("1")
    x += 1
    if x <= 5:
        return second()

def second():
    print("2")
    return first()
x = 1
first()
