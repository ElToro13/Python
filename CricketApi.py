from pycricbuzz import Cricbuzz
import time
while True:
    try:
         
        c = Cricbuzz()
        matches = c.matches()
        Total = c.livescore(3)
        Runs = Total['batting']['score'][0]['runs']
        Wickets = Total['batting']['score'][0]['wickets']
        overs = Total['batting']['score'][0]['overs']
        Batsman1 = Total['batting']['batsman'][0]['name']
        Batsman1Runs = Total['batting']['batsman'][0]['runs']

        Batsman2 = Total['batting']['batsman'][1]['name']
        Batsman2Runs = Total['batting']['batsman'][1]['runs']
        
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
        
        print (Batsman1 + " " + Batsman1Runs)
        print (Batsman2 + " " + Batsman2Runs)
        print (" ****")
        print (Bowler1 + " : " + Bowling1Overs + "-" + Bowling1Maiden + "-" + Bowling1Runs + "-" + Bowling1Wickets)
        print (Bowler2 + " : " + Bowling2Overs + "-" + Bowling2Maiden + "-" + Bowling2Runs + "-" + Bowling2Wickets)
        print()
        print ("Result: " + Status)        
        time.sleep(5)
    except TypeError:
        print ("Enter a Valid match ID.")
    except NameError:
        print ("NameError")
    #except IndexError:
        #print ("Index Error")
    #except KeyError:
        #print ("KeyError")
        
