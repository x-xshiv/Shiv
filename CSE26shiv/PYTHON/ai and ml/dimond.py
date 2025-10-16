def print_diamond(n):
    if n % 2 == 0:
        print("Please enter an odd number for a symmetrical diamond.")
        return

    mid = n // 2

    
    for i in range(mid + 1):
        spaces = ' ' * (mid - i)
        stars = '*' * (2 * i + 1)
        print(spaces + stars)

    
    for i in range(mid - 1, -1, -1):
        spaces = ' ' * (mid - i)
        stars = '*' * (2 * i + 1)
        print(spaces + stars)


try:
    num = int(input("Enter an odd number to create a diamond: "))
    print_diamond(num)
except ValueError:
    print("Please enter a valid integer.")
