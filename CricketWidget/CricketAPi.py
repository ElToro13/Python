from tkinter import *
from pycricbuzz import Cricbuzz
import time

def Cric(iD):
    root = Tk()
    Check = True
    while True:
        try:
            c = Cricbuzz()
            Total = c.livescore(iD)
            State = Total['matchinfo']['mchstate']
            numm = Total['matchinfo']['mnum']
            Runs = Total['batting']['score'][0]['runs']
            Wickets = Total['batting']['score'][0]['wickets']
            overs = Total['batting']['score'][0]['overs']
            Batsman1 = Total['batting']['batsman'][0]['name']
            Batsman1Runs = Total['batting']['batsman'][0]['runs']
            Batsman1Balls = Total['batting']['batsman'][0]['balls']
            Batsman1Fours = Total['batting']['batsman'][0]['fours']
            Batsman1Six = Total['batting']['batsman'][0]['six']

            if Check:
                Batsman2 = Total['batting']['batsman'][1]['name']
                Batsman2Runs = Total['batting']['batsman'][1]['runs']
                Batsman2Balls = Total['batting']['batsman'][1]['balls']
                Batsman2Fours = Total['batting']['batsman'][1]['fours']
                Batsman2Six = Total['batting']['batsman'][1]['six']

            Status = Total['matchinfo']['status']
            MatchTitle = Total['matchinfo']['srs']
            BattingTeam = Total['batting']['team']
            if(len(Total['bowling']['bowler'])!=2):
                Bowler1 = Total['bowling']['bowler'][0]['name']
                Bowling1Overs = Total['bowling']['bowler'][0]['overs']
                Bowling1Maiden = Total['bowling']['bowler'][0]['maidens']
                Bowling1Runs = Total['bowling']['bowler'][0]['runs']
                Bowling1Wickets = Total['bowling']['bowler'][0]['wickets']

                varbowlingteam = "Bowling Side: " + Total['bowling']['team']
                Label(root, text=varbowlingteam).grid(row=4, column=0, sticky=E)
                var4 = Bowler1 + " : " + Bowling1Overs + "-" + Bowling1Maiden + "-" + Bowling1Runs + "-" + Bowling1Wickets
                Label(root, text=var4).grid(row=5, column=0, sticky=E)
            else:
                Bowler1 = Total['bowling']['bowler'][0]['name']
                Bowling1Overs = Total['bowling']['bowler'][0]['overs']
                Bowling1Maiden = Total['bowling']['bowler'][0]['maidens']
                Bowling1Runs = Total['bowling']['bowler'][0]['runs']
                Bowling1Wickets = Total['bowling']['bowler'][0]['wickets']

                Bowler2 = Total['bowling']['bowler'][1]['name']
                Bowling2Overs = Total['bowling']['bowler'][1]['overs']
                Bowling2Maiden = Total['bowling']['bowler'][1]['maidens']
                Bowling2Runs = Total['bowling']['bowler'][1]['runs']
                Bowling2Wickets = Total['bowling']['bowler'][1]['wickets']

                varbowlingteam = "Bowling Side: " + Total['bowling']['team']
                Label(root, text=varbowlingteam).grid(row=4, column=0, sticky=E)
                var4 = Bowler1 + " : " + Bowling1Overs + "-" + Bowling1Maiden + "-" + Bowling1Runs + "-" + Bowling1Wickets
                Label(root, text=var4).grid(row=5, column=0, sticky=E)

                var5 = Bowler2 + " : " + Bowling2Overs + "-" + Bowling2Maiden + "-" + Bowling2Runs + "-" + Bowling2Wickets
                Label(root, text=var5).grid(row=6, column=0, sticky=E)
                
              
            Label(root, text=MatchTitle, relief=RAISED).grid(row=0)
            Label(root, text=numm, relief=RAISED).grid(row=0, column=1)
            
            # print (MatchTitle)

            var1 = BattingTeam + ": " + Runs + " /" + Wickets + ' in ' + overs
            Label(root, text=var1).grid(row=1, column=0, sticky=W)
            print(BattingTeam + ": " + Runs + " /" + Wickets + ' in ' + overs)

            var2 = Batsman1 + " " + Batsman1Runs + " (" + Batsman1Balls + ") "
            var21 = "4 X " + Batsman1Fours + " | " + " 6 X " + Batsman1Six
            Label(root, text=var2).grid(row=2, column=0, sticky=W)
            Label(root, text=var21).grid(row=2, column=1, sticky=W)

            if Check:
                var3 = Batsman2 + " " + Batsman2Runs + " (" + Batsman2Balls + ") "
                var31 = "4 X " + Batsman2Fours + " | " + " 6 X " + Batsman2Six
                Label(root, text=var3).grid(row=3, column=0, sticky=W)
                Label(root, text=var31).grid(row=3, column=1, sticky=W)
            else:
                print("---------")

            var6 = "Result: " + Status
            Label(root, text=var6).grid(row=7, column=0)
            

            time.sleep(1)
            
            #root.mainloop()
            
            root.update()
        except TypeError:
            print("Enter a Valid match ID.")
        except NameError as err:
            print("NameError",err)
        except IndexError:
            Check = False
        except KeyError:
            print("Match is yet to start")
    
        
            



 






