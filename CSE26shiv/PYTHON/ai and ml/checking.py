def count_divisible_numbers(left, right, k):
    x = 0
    for i in range (left,left+1):
        if (i%k==0):
            print(f"hello {i}")
    print(x)
count_divisible_numbers(1,101,7)
