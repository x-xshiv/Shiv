with open("sample.txt") as f:
    x = f.read()
print(x)

y = {"name" : "Shiv",
     "age" : 18,
     "hobby" : "Chess"}

f = open("sample3.txt", "a")

with open("sample3.txt", "w") as f:
    f.write(f"{y}")