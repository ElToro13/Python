from tkinter import *
from oopstester import *
from pycricbuzz import Cricbuzz
import time


class Match(Batsman, Bowler, Score):
    def __init__(self, id=1):
        self.ID = id


    def Livescore(self):
        root = Tk()
        while True:
            
            ODI = Cricbuzz()
            Total = ODI.livescore(self.ID)
            MatchTitle = Total['matchinfo']['srs']
            numm = Total['matchinfo']['mnum']
            Label(root, text=MatchTitle, bg="#E74C3C").grid(row=0, column=0)
            Label(root, text=numm, relief=RAISED, bg="#E74C3C").grid(row=0, column=1)
            
            cc = Score(Total['batting']['score'][0]['runs'],  Total['batting']['score'][0]['overs'], Total['batting']['score'][0]['wickets'])
            ccc = Total['batting']['team'] + " : " + cc.total()
            Label(root, text=ccc, relief=RAISED, bg="#F1C40F").grid(row=1, column=0, sticky=W)

            if(len(Total['batting']['batsman'])==2):
                
                bb = Batsman(Total['batting']['batsman'][0]['name'], Total['batting']['batsman'][1]['name'], Total['batting']['batsman'][0]['runs'], Total['batting']['batsman'][1]['runs'], Total['batting']['batsman'][0]['balls'], Total['batting']['batsman'][1]['balls'], Total['batting']['batsman'][0]['fours'], Total['batting']['batsman'][1]['fours'], Total['batting']['batsman'][0]['six'], Total['batting']['batsman'][1]['six'])
               
                bbb1, bbb2= bb.TwoBatsmen()
                Label(root, text=bbb1).grid(row=2, column=0, sticky=W)
                Label(root, text=bbb2).grid(row=3, column=0, sticky=W)

            varbowlingteam = "Bowling Side: " + Total['bowling']['team']
            Label(root, text=varbowlingteam, relief = RAISED, bg="#3498DB").grid(row=4, column=0, sticky=W)
               
            if(len(Total['bowling']['bowler'])==2):
                ww =Bowler(Total['bowling']['bowler'][0]['name'], Total['bowling']['bowler'][1]['name'], Total['bowling']['bowler'][0]['overs'], Total['bowling']['bowler'][1]['overs'], Total['bowling']['bowler'][0]['runs'], Total['bowling']['bowler'][1]['runs'], Total['bowling']['bowler'][0]['maidens'], Total['bowling']['bowler'][1]['maidens'], Total['bowling']['bowler'][0]['wickets'], Total['bowling']['bowler'][1]['wickets'])
                www1, www2 = ww.TwoBowler()
                Label(root, text=www1).grid(row=5, column=0, sticky=W)
                Label(root, text=www2).grid(row=6, column=0, sticky=W)

            var6 = "Result: " + Total['matchinfo']['status']
            Label(root, text=var6, bg="#FDFEFE").grid(row=7, column=0, sticky=W)
            
            time.sleep(1)
                
            #root.mainloop()
                
            root.update()
        root.destroy()

            
        
