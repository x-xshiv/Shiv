import numpy as np
diagonal1win = 0
diagonal2win = 0
rowwin = 0
columnwin = 0
totalbalance = 10000
totalwins = 0
for a in range(100000):
    multiplier = 0
    if totalbalance < 1:
         print("insufficient balance")
         break
    else:
        totalbalance -= 1
        _ = np.random.randint(3,9,(3,3))
        for i in range(len(_)):
            m = _[i][0]
            wincheck1 = True
            for j in range(len(_)):
                if _[i][j] != m:
                    wincheck1 = False
        if wincheck1:
            print('you win by column')
            rowwin += 1


        for i in range(len(_)):
            n = _[0][i]
            wincheck2 = True
            for j in range(len(_)):
                if _[j][i] != n:
                    wincheck2 = False
        if wincheck2:
            print('you win by row')
            columnwin += 1


        o = _[0][0]
        wincheck3 = True
        for i in range(1,len(_)):
            if o != _[i][i]:
                wincheck3 = False
        if wincheck3:
                print('you win diagonal 1')
                diagonal1win += 1
        

        p = _[0][-1]
        wincheck4 = True
        for i in range(0,len(_)):
            if p != _[i][-(i+1)]:
                wincheck4 = False
        if wincheck4:
                print('you win by diagonal 2')
                diagonal2win += 1
    
    winlist = [wincheck1, wincheck2, wincheck3, wincheck4]
    multiplyfactor = [m,n,o,p]
    if wincheck1 or wincheck2 or wincheck3 or wincheck4:
        totalwins +=1
        multiplier = 1
        for i,j in enumerate(winlist):
            if j:
                multiplier *= multiplyfactor[i]
        print(f"congrats you win {multiplier}x the bet amount")
        print(_)
        print("__________________________________")
    totalbalance += multiplier


            
        


print(f"total wins = {totalwins}")
print(f"total diagonal1 win = {diagonal1win}")
print(f"total diagonal2 win = {diagonal2win}")
print(f"total row win = {rowwin}")
print(f"total column win = {columnwin}")
print(f"winning percentage = {round(((totalwins/(a+1))*100), 2)}%")
print(f"total balance = {totalbalance}")
    
            




