for i in range(1,10):
    bag=""
    for j in range(1,10):
        if(i>= int(j/2) and i<int(j) ):
            bag = bag + "*"
        else:
            bag = bag + " "
    print(bag)
