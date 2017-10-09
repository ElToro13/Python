import pandas as pd


df = pd.read_csv('C:\\Users\\chinkasoni\\Desktop\\FootballEurope.csv')

hometeamgol = df.homeGoalFT
awayteamgol = df.awayGoalFT

hometeamname = df.homeTeam
awayteamname = df.awayTeam

division = df.division

#Selector = ('Real Madrid', 'Barcelona', 'Atletico', 'Man Utd', 'Liverpool', 'Borussia Dortmund', 'Man City', 'Chelsea', 'Tottenham', 'Arsenal', 'leicester', 'Bayern', 'PSG')
# EPL 2922(H)  2252(A)
#Bundesliga 2493 (H) 1953(A)
#La Liga 3091(H) 2214(A)
#Ligue 1 2760(H) 2034 (A) 
class MatchDetails:
    
    def __init__(self, TeamName=""):
        self.TN = TeamName
    def hgs(self):
        data = []
        THGS = 0

        for i in range(0,len(hometeamname)):
            if(hometeamname[i]==self.TN):
                data.append(i)
        for j in range(0,len(data)):
            THGS+=hometeamgol[data[j]]
        del data
        return int(THGS)

    def ags(self):
        data = []
        TAGS = 0
        for i in range(0,len(awayteamname)):
            if(awayteamname[i]==self.TN):
                data.append(i)
        for j in range(0,len(data)):
            TAGS+=awayteamgol[data[j]]
        del data
        return int(TAGS)

    def hgc(self):
        data = []
        THGC = 0
        for i in range(0,len(hometeamname)):
            if(hometeamname[i]==self.TN):
                data.append(i)
        for j in range(0,len(data)):
            THGC+=awayteamgol[data[j]]
        del data
        return int(THGC)

    def agc(self):
        data = []
        TAGC = 0
        for i in range(0,len(awayteamname)):
            if(awayteamname[i]==self.TN):
                data.append(i)
        for j in range(0,len(data)):
            TAGC+=hometeamgol[data[j]]
        del data
        return int(TAGC)

    def ohg(self):
        data = []
        for i in range(0,len(division)):
            if(hometeamname[i]==self.TN):
                data.append(division[i])
                break
        if(data[0] == 'EPL'):
            return int(2922)
        elif(data[0] == 'Bundesliga'):
            return int(2493)
        elif(data[0] == 'La_Liga'):
            return int(3091)
        else:
            return int(2760)

    def oag(self):
        dat = []
        for i in range(0,len(division)):
            if(awayteamname[i]==self.TN):
                dat.append(division[i])
                break
        if(dat[0] == 'EPL'):
            return int(2252)
        elif(dat[0] == 'Bundesliga'):
            return int(1953)
        elif(dat[0] == 'La_Liga'):
            return int(2214)
        else:
            return int(2034)
        
        
        
        
        
        
                
                
