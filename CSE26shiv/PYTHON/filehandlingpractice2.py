with open("sample3.txt","r") as f:
    for i,x in enumerate(f):
        if i == 3:
            with open("sample3.txt", "w") as f:
                f.write(f"hello")