s = input("enter your string : ")
num = 0
for ch in s:
    if ch.isdigit():
        num += int(ch)
print(num)
