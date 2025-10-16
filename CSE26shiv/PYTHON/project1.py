import sys
import numpy as np
class CashHandling:
    balance = 0
    def __init__(self):
        print(f"current balance = {self.balance}")
        StartMenu()
        
    def deposit(self):
        while True:
            try:           
                x = int(input("Enter the Amount you want to deposit :- "))
                if x < 1000:
                    print("enter some positive amount greater or equal to 1000 inr !!") 
                elif x >= 1000:
                    CashHandling.balance = CashHandling.balance + x
                    print("amount added to your current balance")
                    print(f"current balance :- {CashHandling.balance}")
                    return StartMenu()
            except NameError:
                print("please enter valid integer value !!")


class StartMenu:
    def __init__(self):
        print("type 1 for checking current balance\ntype 2 for depositing money\ntype 3 for starting the game\npress enter to exit")
        y = input("your input --> ")
        if y == "1":
            return CashHandling()
        elif y == "2":
            return CashHandling.deposit(self)
        elif y == "3":
            return MainGame()
        else:
            sys.exit()

        

class MainGame:
    def __init__(self):
        print("=========================================")
        print("WELCOME TO JACKPOT ROULETTE")
        print(f"=====================\nCurrent Balance :- {CashHandling.balance}\n=====================")
        try:
            x = int(input("enter number of rows or columns :- "))
        except NameError:
            print("enter valid number")
            return MainGame()
        if x < 3:
            print("number should be 3 or more than three")
            return MainGame()
        print(f"if you get {x} same number in a row, column or in a diagnol your betting amount will be multiplied that much")
        print("Minimum Betting Amount = 5000 inr")
        print(f"note: if you dont get {x} in a row your bet amount will get lost")
        print("note: mulplier is stackable")
        print("remember higher the rows or columns higher the multiplier but lowerer the winning percentage")
        print("=========================================")
        try:                                                            
            index2 = int(input("choose 1 for manual single bet \nchoose 2 for auto multiple bet\nEnter to Exit!!"))
            if index2 == 1:
                return WorkingOfGame.manualbet(self,x)
            elif index2 == 2:
                return WorkingOfGame.autobet(self,x)
            else:
                sys.exit()
        except NameError:
            sys.exit()

class WorkingOfGame: 
    def manualbet(self,x):
        while True:

            try:
                bet_amount = int(input("enter amount you want to bet :- "))
                if bet_amount >= 5000:
                    if bet_amount > CashHandling.balance:
                        print(f"Insufficient Balance!! Please deposit at least {bet_amount - CashHandling.balance}")
                        return  StartMenu()
                    else:
                        print("let your fate decide outcome")
                        print("now rolling !!")
                        CashHandling.balance -= bet_amount

                        _ = np.random.randint(x,3*x,(x,x))
                        for i in range(len(_)):
                            m = _[i][0]
                            wincheck1 = True
                            for j in range(len(_)):
                                if _[i][j] != m:
                                    wincheck1 = False
                        if wincheck1:
                            print('you win by column')


                        for i in range(len(_)):
                            n = _[0][i]
                            wincheck2 = True
                            for j in range(len(_)):
                                if _[j][i] != n:
                                    wincheck2 = False
                        if wincheck2:
                            print('you win by row')


                        o = _[0][0]
                        wincheck3 = True
                        for i in range(1,len(_)):
                            if o != _[i][i]:
                                wincheck3 = False
                        if wincheck3:
                                print('you win diagonal 1')
                        

                        p = _[0][-1]
                        wincheck4 = True
                        for i in range(0,len(_)):
                            if p != _[i][-(i+1)]:
                                wincheck4 = False
                        if wincheck4:
                                print('you win by diagonal 2')
                    
                        winlist = [wincheck1, wincheck2, wincheck3, wincheck4]
                        multiplyfactor = [m,n,o,p]
                        if wincheck1 or wincheck2 or wincheck3 or wincheck4:
                            multiplier = 1
                            for i,j in enumerate(winlist):
                                if j:
                                    multiplier *= multiplyfactor[i]
                            print("=========================================")
                            print(f"congrats you win {multiplier}x the bet amount")
                            print(_)
                            print("__________________________________")
                            CashHandling.balance += bet_amount*multiplier
                            print(f"Current Balance = {CashHandling.balance}")
                            print("=========================================")
                            while True:
                                index1 = input("want to continue betting\ntype yes or no :- ")
                                if index1.lower() == "yes":
                                    return MainGame()
                                elif index1.lower() == "no":
                                    return StartMenu()
                                else:
                                    print("enter a valid input !!")


                        else:
                            print("=========================================")
                            print("You Lost!!!")
                            print(_)
                            print(f"Current Balance = {CashHandling.balance}")
                            print("=========================================")
                            while True:
                                index1 = input("want to continue betting\ntype yes or no :- ")
                                if index1.lower() == "yes":
                                    return MainGame()
                                elif index1.lower() == "no":
                                    return StartMenu()
                                else:
                                    print("enter a valid input !!")

                elif bet_amount < 5000:
                    print("bet amount should be greater than or equal to 5000")
                    return MainGame()
                return MainGame()

            except ValueError:
                print("amount should be integer")
                return MainGame()
            

    def autobet(self,x):
        while True:

            try:
                bet_amount = int(input("enter amount you want to bet :- "))
                number_of_bets = int(input("enter number of bet :- "))
                
                if bet_amount >= 5000:
                    if bet_amount*number_of_bets > CashHandling.balance:
                        print(f"Insufficient Balance!! Please deposit at least {bet_amount*number_of_bets - CashHandling.balance}")
                        return  StartMenu()
                    else:
                        for i in range(1,number_of_bets+1):

                            print("let your fate decide outcome")
                            print("now rolling !!")
                            CashHandling.balance -= bet_amount

                            _ = np.random.randint(x,3*x,(x,x))
                            for i in range(len(_)):
                                m = _[i][0]
                                wincheck1 = True
                                for j in range(len(_)):
                                    if _[i][j] != m:
                                        wincheck1 = False
                            if wincheck1:
                                print('you win by column')

                            for i in range(len(_)):
                                n = _[0][i]
                                wincheck2 = True
                                for j in range(len(_)):
                                    if _[j][i] != n:
                                        wincheck2 = False
                            if wincheck2:
                                print('you win by row')


                            o = _[0][0]
                            wincheck3 = True
                            for i in range(1,len(_)):
                                if o != _[i][i]:
                                    wincheck3 = False
                            if wincheck3:
                                    print('you win diagonal 1')
                            

                            p = _[0][-1]
                            wincheck4 = True
                            for i in range(0,len(_)):
                                if p != _[i][-(i+1)]:
                                    wincheck4 = False
                            if wincheck4:
                                    print('you win by diagonal 2')
                        
                            winlist = [wincheck1, wincheck2, wincheck3, wincheck4]
                            multiplyfactor = [m,n,o,p]
                            if wincheck1 or wincheck2 or wincheck3 or wincheck4:
                                multiplier = 1
                                for i,j in enumerate(winlist):
                                    if j:
                                        multiplier *= multiplyfactor[i]
                                print("=========================================")
                                print(f"congrats you win {multiplier}x the bet amount")
                                print(_)
                                print("__________________________________")
                                CashHandling.balance += bet_amount*multiplier
                                print(f"Current Balance = {CashHandling.balance}")
                                print("=========================================")

                            else:
                                print("=========================================")
                                print("You Lost!!!")
                                print(_)
                                print(f"Current Balance = {CashHandling.balance}")
                                print("=========================================")

                elif bet_amount < 5000:
                    print("bet amount should be greater than or equal to 5000")
                    return MainGame()
                return MainGame()

            except ValueError:
                print("amount should be integer")
                return MainGame()

StartMenu()

