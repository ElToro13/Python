from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from Class_Cricbuzz import *
from pycricbuzz import Cricbuzz
import time


def scoreb(i):
    root = Tk()
    sco = Cricbuzz()
    Total = sco.scorecard(i)
    ii = len(Total['scorecard'][0]['batcard'])
    Label(root, text="Batsman",bg="#F0B27A").grid(row=0, column=0, sticky=W)
    Label(root, text="Dismissal",bg="#F0B27A").grid(row=0, column=1, sticky=W)
    Label(root, text="Runs",bg="#F0B27A").grid(row=0, column=2, sticky=W)
    Label(root, text="Balls",bg="#F0B27A").grid(row=0, column=3, sticky=W)
    for k in range(1,ii+1):        
        name = Total['scorecard'][0]['batcard'][k-1]['name']
        diss = Total['scorecard'][0]['batcard'][k-1]['dismissal']
        run = Total['scorecard'][0]['batcard'][k-1]['runs']
        ball = Total['scorecard'][0]['batcard'][k-1]['balls']
        
        Label(root, text=name).grid(row=k, column=0, sticky=W)
        Label(root, text=diss).grid(row=k, column=1, sticky=W)
        Label(root, text=run).grid(row=k, column=2, sticky=W)
        Label(root, text=ball).grid(row=k, column=3, sticky=W)
    uu = len(Total['scorecard'][0]['bowlcard'])
    Label(root, text="Bowler",bg="#F0B27A").grid(row=ii+2, column=0, sticky=W)
    Label(root, text="O",bg="#F0B27A").grid(row=ii+2, column=2, sticky=W)
    Label(root, text="M",bg="#F0B27A").grid(row=ii+2, column=3, sticky=W)
    Label(root, text="R",bg="#F0B27A").grid(row=ii+2, column=4, sticky=W)
    Label(root, text="W",bg="#F0B27A").grid(row=ii+2, column=5, sticky=W)
    if(len(Total['scorecard'])==1):
        ddd = Total['scorecard'][1]['runs']
        wick = Total['scorecard'][1]['wickets']
        oo = Total['scorecard'][1]['overs']
        Label(root, text=ddd+" in "+oo+" for "+wick,bg="#F0B27A").grid(row=ii+1, column=0, sticky=W)
        
    else:
        ddd = Total['scorecard'][0]['runs']
        wick = Total['scorecard'][0]['wickets']
        oo = Total['scorecard'][0]['overs']
        Label(root, text=ddd+" in "+oo+" for "+wick,bg="#F0B27A").grid(row=ii+1, column=0, sticky=W)
        
        
        
        
    
    for e in range(11,uu+11):
        name = Total['scorecard'][0]['bowlcard'][e-11]['name']
        over = Total['scorecard'][0]['bowlcard'][e-11]['overs']
        maiden = Total['scorecard'][0]['bowlcard'][e-11]['maidens']
        runs = Total['scorecard'][0]['bowlcard'][e-11]['runs']
        wicket = Total['scorecard'][0]['bowlcard'][e-11]['wickets']

        Label(root, text=name).grid(row=e+11, column=0, sticky=W)
        Label(root, text=over).grid(row=e+11, column=2, sticky=W)
        Label(root, text=maiden).grid(row=e+11, column=3, sticky=W)
        Label(root, text=runs).grid(row=e+11, column=4, sticky=W)
        Label(root, text=wicket).grid(row=e+11, column=5, sticky=W)

        
       
    #time.sleep(1)
    root.mainloop()



def scoreb2(i):
    #try:
    root1 = Tk()
    sco = Cricbuzz()
    Total = sco.scorecard(i)
    ii = len(Total['scorecard'][1]['batcard'])
    Label(root1, text="Batsman",bg="#F0B27A").grid(row=0, column=0, sticky=W)
    Label(root1, text="Dismissal",bg="#F0B27A").grid(row=0, column=1, sticky=W)
    Label(root1, text="Runs",bg="#F0B27A").grid(row=0, column=2, sticky=W)
    Label(root1, text="Balls",bg="#F0B27A").grid(row=0, column=3, sticky=W)
    for k in range(1,ii+1):        
        name = Total['scorecard'][1]['batcard'][k-1]['name']
        diss = Total['scorecard'][1]['batcard'][k-1]['dismissal']
        run = Total['scorecard'][1]['batcard'][k-1]['runs']
        ball = Total['scorecard'][1]['batcard'][k-1]['balls']
        
        Label(root1, text=name).grid(row=k, column=0, sticky=W)
        Label(root1, text=diss).grid(row=k, column=1, sticky=W)
        Label(root1, text=run).grid(row=k, column=2, sticky=W)
        Label(root1, text=ball).grid(row=k, column=3, sticky=W)
    uu = len(Total['scorecard'][1]['bowlcard'])
    Label(root1, text="Bowler",bg="#F0B27A").grid(row=ii+2, column=0, sticky=W)
    Label(root1, text="O",bg="#F0B27A").grid(row=ii+2, column=2, sticky=W)
    Label(root1, text="M",bg="#F0B27A").grid(row=ii+2, column=3, sticky=W)
    Label(root1, text="R",bg="#F0B27A").grid(row=ii+2, column=4, sticky=W)
    Label(root1, text="W",bg="#F0B27A").grid(row=ii+2, column=5, sticky=W)

    ddd = Total['scorecard'][1]['runs']
    wick = Total['scorecard'][1]['wickets']
    oo = Total['scorecard'][1]['overs']
    Label(root1, text=ddd+" in "+oo+" for "+wick,bg="#F0B27A").grid(row=ii+1, column=0, sticky=W)
    
    for e in range(12,uu+12):
        name = Total['scorecard'][1]['bowlcard'][e-12]['name']
        over = Total['scorecard'][1]['bowlcard'][e-12]['overs']
        maiden = Total['scorecard'][1]['bowlcard'][e-12]['maidens']
        runs = Total['scorecard'][1]['bowlcard'][e-12]['runs']
        wicket = Total['scorecard'][1]['bowlcard'][e-12]['wickets']

        Label(root1, text=name).grid(row=e+11, column=0, sticky=W)
        Label(root1, text=over).grid(row=e+11, column=2, sticky=W)
        Label(root1, text=maiden).grid(row=e+11, column=3, sticky=W)
        Label(root1, text=runs).grid(row=e+11, column=4, sticky=W)
        Label(root1, text=wicket).grid(row=e+11, column=5, sticky=W)

   
       
    #time.sleep(1)                
    root1.mainloop()
    #except:
     #   print('Second Innings is yet to start')
    
    
def Refresh(h):
    #root.destroy()
    ss = Match(h)
    sss = ss.Livescore()

class Match(Batsman, Bowler, Score):
    def __init__(self, id=1):
        Batsman.__init__(self, batsman1="", batsman2="", runs1="", runs2="", balls1="", balls2="", four1="", four2="", six1="", six2="")
        Bowler.__init__(self, bowler1="", bowler2="", over1="", over2="", runsconceded1="", runsconceded2="", maiden1="",
                 maiden2="", wicket1="", wicket2="")
        Score.__init__(self, score="", overs="", wickets="")
        self.ID = id
    
    
    def Livescore(self):
        root = Tk()
        
        try:
            while True:
                ODI = Cricbuzz()
                Total = ODI.livescore(self.ID)
                MatchTitle = Total['matchinfo']['srs']
                numm = Total['matchinfo']['mnum']
                Label(root, text=MatchTitle, bg="#BB8FCE").grid(row=0, column=0, sticky=W)
                Label(root, text=numm, relief=RAISED, bg="#BB8FCE").grid(row=0, column=2, sticky=E)
                
                cc = Score(Total['batting']['score'][0]['runs'],  Total['batting']['score'][0]['overs'], Total['batting']['score'][0]['wickets'])
                ccc = Total['batting']['team'] + " : " + cc.total()
                Label(root, text=ccc, relief=RAISED,bg="#3498DB", fg="#FDFEFE").grid(row=1, column=0, sticky=W)
                button = tk.Button(root, text='Scorecard', relief=RAISED,command=lambda: scoreb2(self.ID))
                button.grid(row=4, column=1)
                button = tk.Button(root, text='Refresh', relief=RAISED,command=lambda: Refresh(self.ID))
                button.grid(row=1, column=2)
                button = tk.Button(root, text='Scorecard', relief=RAISED,command=lambda: scoreb(self.ID))
                button.grid(row=1, column=1)

                if(len(Total['batting']['batsman'])==2):
                    
                    bb = Batsman(Total['batting']['batsman'][0]['name'], Total['batting']['batsman'][1]['name'], Total['batting']['batsman'][0]['runs'], Total['batting']['batsman'][1]['runs'], Total['batting']['batsman'][0]['balls'], Total['batting']['batsman'][1]['balls'], Total['batting']['batsman'][0]['fours'], Total['batting']['batsman'][1]['fours'], Total['batting']['batsman'][0]['six'], Total['batting']['batsman'][1]['six'])
                   
                    bbb1, bbb2= bb.TwoBatsmen()
                    Label(root, text=bbb1).grid(row=2, column=0, sticky=W)
                    Label(root, text=bbb2).grid(row=3, column=0, sticky=W)


                varbowlingteam = "Bowling Side: " + Total['bowling']['team']
                Label(root, text=varbowlingteam, relief = RAISED,  bg="#F1C40F").grid(row=4, column=0, sticky=W)
                   
                if(len(Total['bowling']['bowler'])==2):
                    ww =Bowler(Total['bowling']['bowler'][0]['name'], Total['bowling']['bowler'][1]['name'], Total['bowling']['bowler'][0]['overs'], Total['bowling']['bowler'][1]['overs'], Total['bowling']['bowler'][0]['runs'], Total['bowling']['bowler'][1]['runs'], Total['bowling']['bowler'][0]['maidens'], Total['bowling']['bowler'][1]['maidens'], Total['bowling']['bowler'][0]['wickets'], Total['bowling']['bowler'][1]['wickets'])
                    www1, www2 = ww.TwoBowler()
                    Label(root, text=www1).grid(row=5, column=0, sticky=W)
                    Label(root, text=www2).grid(row=6, column=0, sticky=W)

                var6 = "Result: " + Total['matchinfo']['status']
                Label(root, text=var6, bg="#FDFEFE").grid(row=7, column=0,sticky=W)

                scr = scrolledtext.ScrolledText(root, width=30, height=10, wrap=tk.WORD)
                scr.grid(row=8,column=0, sticky='WE', columnspan=3)
                
                

                
                   
                root.update()

                ty = Tk()
                cc = ODI.commentary(self.ID)
                dd = cc['commentary']
                for i in  range(len(dd)-1,1,-1):
                    scr.insert('1.0', dd[i]+"\n \n")
                ty.close()

                
                
            
        except ValueError:
            print("Value Error")
        except IndexError:
            print("Index Error")
        except KeyError:
            print("KeyError")
        except:
            print("Thank you for using Cricbuzz Widget- Powered by PyCricbuzz")
            
            

            

            
            


            
        
