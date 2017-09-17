from pycricbuzz import Cricbuzz
import time
while True:
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
        print (Runs +" /" + Wickets + ' in ' + overs)
        print (Batsman1 + " " + Batsman1Runs)
        print (Batsman2 + " " + Batsman2Runs)
        print (Status)
        print ("-------------")
        time.sleep(5)
        
