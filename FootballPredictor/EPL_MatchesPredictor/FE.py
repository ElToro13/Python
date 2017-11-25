import requests
import json
import time
from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth

ff=0
LID = input('Enter the League ID: \n 1) EPL \n 2) La Liga: \n')
if(int(LID) == 1):
    ff = 1204
    from FootballEurope import *
    from FootballEurope_Two import *

    
elif(int(LID) == 2):
    ff = 1399
    from LaLiga import *
    from LaLiga_Two import *
else:
    print('Invalid Input')

print(ff)
team = requests.get("http://api.football-api.com/2.0/matches?comp_id="+str(ff)+"&from_date=2017-10-13&to_date=2018-06-01&Authorization=565ec012251f932ea4000001fa542ae9d994470e73fdb314a8a56d76")
data=[]
team2 = json.loads(team.content.decode('utf-8'))
#print(team2)
for i in range(0,len(team2)):
    local = team2[i]['localteam_name']
    away = team2[i]['visitorteam_name']
    week = team2[i]['week']
    if(int(week)<10):
        week = "0" + str(week)
        
    data.append(week+ "/" +local+ "/" +away)
    #print(local + ' - ' + away)
data = sorted(data)
'''
for j in range(0,len(data)):
    print(data[j])
'''
GameWeek = input("For which game week you like to predict? // 8-38 ")
GameWeek = int(GameWeek)-8
fff = open("Predictor_Week.txt", "a")
fff.write("\n GameWeek - "+ str(GameWeek)+"\n")
fff.close()
for j in range(GameWeek*10,GameWeek*10+10):
    print(data[j])
    details = data[j].split('/')
    home = details[1]
    if(home == "Málaga"):
        del home
        home="Malaga"
    elif(home == "Atlético Madrid"):
        del home
        home = "Atletico"
    elif(home == "Atl. Madrid"):
        del home
        home="Atletico"
    elif(home=="Deportivo La Coruña"):
        del home
        home="Deportivo"
    elif(home=='Dep. La Coruna'):
        del home
        home="Deportivo"
    elif(home=="Leganés"):
        del home
        home="Leganes"
    elif(home=="Deportivo Alavés"):
        del home
        home="Alaves"
    elif(home == "Celta de Vigo"):
        del home
        home = "Celta Vigo"
    elif(home == "Ath Bilbao"):
        del home
        home = "Athletic Club"
    elif(home == "Leicester"):
        home = "Leicester City"
    elif(home == "West Brom"):
        home = "West Bromwich Albion"
    elif(home == "West Ham"):
        home = "West Ham United"
    elif(home == 'Newcastle Utd'):
        home = 'Newcastle United'
    elif(home == "Tottenham"):
        home = "Tottenham Hotspur"
    
    
        
    #print(home)
    away = details[2]
    if(away == "Málaga"):
        del away
        away="Malaga"
    elif(away == "Atlético Madrid"):
        del away
        away="Atletico"
    elif(away == "Atl. Madrid"):
        del away
        away = "Atletico"
    elif(away=="Deportivo La Coruña"):
        del away
        away="Deportivo"
    elif(away=='Dep. La Coruna'):
        del away
        away="Deportivo"
    elif(away=="Leganés"):
        del away
        away="Leganes"
    elif(away=="Deportivo Alavés"):
        del away
        away="Alaves"
    elif(away == "Celta de Vigo"):
        del away
        away = "Celta Vigo"
    elif(away == "Ath Bilbao"):
        del away
        away = "Athletic Club"
    elif(away == "Leicester"):
        away = "Leicester City"
    elif(away == "West Brom"):
        away = "West Bromwich Albion"
    elif(away == "West Ham"):
        away = "West Ham United"
    elif(away =='Newcastle Utd'):
        away ='Newcastle United'
    elif(away =='Bournemouth'):
        away = "AFC Bournemouth"
    elif(away == "Tottenham"):
        away = "Tottenham Hotspur"
        
    

    
    #print(away)
    try:
        dd = odds(home,away)
        ff = odds_Two(home,away)
        print("------")
    except:
        print("Predictions Not Available")
    
gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

file1 = open("Predictor_Week.txt")
file = file1.read()
file2 = drive.CreateFile({'title': 'footballPredictions.txt'})  # Create GoogleDriveFile instance with title 'Hello.txt'.
file2.SetContentString(file) # Set content of the file from given string.
file2.Upload()

        
    

