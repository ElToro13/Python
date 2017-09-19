from pycricbuzz import Cricbuzz
import time

    
def Cric(iD):
    Check = True
    while True:
        try:
            c = Cricbuzz()
            matches = c.matches()
            Total = c.livescore(iD) #16855
            Runs = Total['batting']['score'][0]['runs']
            Wickets = Total['batting']['score'][0]['wickets']
            overs = Total['batting']['score'][0]['overs']
            Batsman1 = Total['batting']['batsman'][0]['name']
            Batsman1Runs = Total['batting']['batsman'][0]['runs']
            Batsman1Balls = Total['batting']['batsman'][0]['balls']
            Batsman1Fours = Total['batting']['batsman'][0]['fours']
            Batsman1Six = Total['batting']['batsman'][0]['six']
            
            if(Check):
                Batsman2 = Total['batting']['batsman'][1]['name']
                Batsman2Runs = Total['batting']['batsman'][1]['runs']
                Batsman2Balls = Total['batting']['batsman'][1]['balls']
                Batsman2Fours = Total['batting']['batsman'][1]['fours']
                Batsman2Six = Total['batting']['batsman'][1]['six']
           
            
            Status = Total['matchinfo']['status']
            MatchTitle = Total['matchinfo']['srs']
            BattingTeam = Total['batting']['team']
            
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
            
            print ("-------------")
            print (MatchTitle)
            print (BattingTeam + ": " + Runs +" /" + Wickets + ' in ' + overs)
            
            print (Batsman1 + " " + Batsman1Runs + " (" + Batsman1Balls + ") "  + "4 X " + Batsman1Fours + " | " + " 6 X " + Batsman1Six)
            
            if(Check):
                print (Batsman2 + " " + Batsman2Runs + " (" + Batsman2Balls + ") "  + "4 X " + Batsman2Fours +  " | " + " 6 X " + Batsman2Six)
            else:
                print ("---------")
            
            print (" ****")
            print (Bowler1 + " : " + Bowling1Overs + "-" + Bowling1Maiden + "-" + Bowling1Runs + "-" + Bowling1Wickets)
            print (Bowler2 + " : " + Bowling2Overs + "-" + Bowling2Maiden + "-" + Bowling2Runs + "-" + Bowling2Wickets)
            
            print()
            print ("Result: " + Status)
            
            time.sleep(5)
            
        except TypeError:
            print ("Enter a Valid match ID.")
        except NameError as err:
            print ("NameError",err)
        except IndexError as err:
            print ("Resolving Issues, please wait..")
            Check = False
            #print ("Index Error", err)
        except KeyError as err:
            #print ("KeyError", err)
            print ("Match is yet to start")
            
        except:
            print ("Unknown Error..")
     
      

     
       

        
