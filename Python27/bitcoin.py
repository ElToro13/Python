import requests
import json

def Bitcoin():
    r = requests.get("https://www.zebapi.com/api/v1/market/ticker/btc/inr")

    data = json.loads(r.content)

    print(data["buy"])
    print(data["sell"])
    B = int(data["buy"])
    S = int(data["sell"])
    if B>S:
        print("Difference: " + str(B-S))
        



'''
listo = []
ID = []
for i in range(0,len(team2)):
    listo.append(team2[i]['team_id'])
    
for j in range(0,len(listo)):
    try:
        URL = "http://api.football-api.com/2.0/matches?comp_id=1204&team_id=" + listo[j] + "&match_date=2017-09-30&Authorization=565ec012251f932ea4000001fa542ae9d994470e73fdb314a8a56d76"
        fix_init = requests.get(URL)
        fix = json.loads(fix_init.content)
        match_id = fix[0]['id']
        if match_id not in ID:
            ID.append(match_id)
            local = fix[0]['localteam_name']
            away = fix[0]['visitorteam_name']
            print(local + " V/s " +  away) 
    except KeyError:
        print()
        
'''    
            
Bitcoin()
