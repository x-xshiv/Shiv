wincheck1 = True
wincheck2 = False
wincheck3 = True
wincheck4 = False

m = 2
n = 3
o = 6
p = 5

winlist = [wincheck1, wincheck2, wincheck3, wincheck4]
multiplyfactor = [m,n,o,p]
if wincheck1 or wincheck2 or wincheck3 or wincheck4:
    multiplier = 1
    for i,j in enumerate(winlist):
        if j:
            multiplier *= multiplyfactor[i]

print(multiplier)