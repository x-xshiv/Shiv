import numpy as np
win = True
while win:
        arr = np.random.randint(2,5,(3,3))
        k = arr[0][-1]
        wincheck = True
        for i in range(1,len(arr)):
                if k != arr[i][-(i+1)]:
                        wincheck = False
        if wincheck:
                print('you win')
                print(arr)
                break