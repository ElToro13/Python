import math
import pandas as pd
from H2H_LaLiga import H2H_Cal
from form_LaLiga import Form_Cal


df = pd.read_csv('C:\\Users\\chinkasoni\\Desktop\\LaLiga.csv')
hometeamgol = df.homeGoalFT
awayteamgol = df.awayGoalFT
hometeamname = df.homeTeam
awayteamname = df.awayTeam
division = df.division
#Selector = ('Real Madrid', 'Barcelona', 'Atletico', 'Man Utd', 'Liverpool', 'Borussia Dortmund', 'Man City', 'Chelsea', 'Tottenham', 'Arsenal', 'leicester', 'Bayern', 'PSG')
# EPL 2922(H)  2252(A) 1173 916
#Bundesliga 2493 (H) 1953(A)
#La Liga 3091(H) 2214(A) 1247 914
#Ligue 1 2760(H) 2034 (A)
            
class MatchDetails:
    
    
    def __init__(self, HomeTeam="", AwayTeam=""):
        self.HT = HomeTeam
        self.AT = AwayTeam

        
    def hgs(self):
        data = []
        THGS = 0

        for i in range(0,len(hometeamname)):
            if(hometeamname[i]==self.HT):
                data.append(i)
        for j in range(0,len(data)):
            THGS+=hometeamgol[data[j]]
        del data
        return int(THGS)

    def ags(self):
        data = []
        TAGS = 0
        for i in range(0,len(awayteamname)):
            if(awayteamname[i]==self.AT):
                data.append(i)
        for j in range(0,len(data)):
            TAGS+=awayteamgol[data[j]]
        del data
        return int(TAGS)

    def hgc(self):
        data = []
        THGC = 0
        for i in range(0,len(hometeamname)):
            if(hometeamname[i]==self.HT):
                data.append(i)
        for j in range(0,len(data)):
            THGC+=awayteamgol[data[j]]
        del data
        return int(THGC)

    def agc(self):
        data = []
        TAGC = 0
        for i in range(0,len(awayteamname)):
            if(awayteamname[i]==self.AT):
                data.append(i)
        for j in range(0,len(data)):
            TAGC+=hometeamgol[data[j]]
        del data
        return int(TAGC)

    def ohg(self):
        return int(1247)

    def oag(self):
        return int(914)
        

class odds(MatchDetails):

    def __init__(self, Hometeam="", Awayteam=""):
        self.h = Hometeam
        self.a = Awayteam

        foo = MatchDetails(self.h, self.a)
        print(self.h)
        print(self.a)
        one = foo.hgs()
        two = foo.agc()
        three = foo.ohg()

        four = foo.hgc()
        five = foo.ags()
        six = foo.oag()

        H,A,T=H2H_Cal(self.h,self.a)
        FH,FA = Form_Cal(self.h,self.a)
        
        if(T == 0):
            HTS = ((one/38)*(two/38))/(three/760)+ FH/15 
            ATS =  (((four/38)*(five/38))/(six/760)) + FA/15 

        else:
            HTS = ((one/38)*(two/38))/(three/760)+ FH/15 + H/T
            ATS =  ((four/38)*(five/38))/(six/760) + FA/15 + A/T


        dato = []
        poi = 0
        for i in range(0,6):
            poi = ((math.exp(-HTS))*(math.pow(HTS,i)))/(math.factorial(i)) 
            dato.append(round(poi,4))

        daty = []
        poy = 0
        for j in range(0,6):
            poy = ((math.exp(-ATS))*(math.pow(ATS,j)))/(math.factorial(j))
            daty.append(round(poy,4))

        
        HomeScore = dato.index(max(dato))
        AwayScore = daty.index(max(daty))
        FTS = str(HomeScore) + " - " + str(AwayScore)
        fff = open("Predictor_Week.txt", "a") 
        fff.write(self.h+" "+FTS+" "+self.a+"\n")
        fff.close()
        print(str(HomeScore) + " - " + str(AwayScore)+" **")
        
        HTS =  ((one/38)*(two/38))/(three/760)
        ATS =  ((four/38)*(five/38))/(six/760)

        dato = []
        poi = 0
        for i in range(0,6):
            poi = ((math.exp(-HTS))*(math.pow(HTS,i)))/(math.factorial(i)) 
            dato.append(round(poi,4))

        daty = []
        poy = 0
        for j in range(0,6):
            poy = ((math.exp(-ATS))*(math.pow(ATS,j)))/(math.factorial(j))
            daty.append(round(poy,4))

        #print(dato)
        #print(daty)

        HomeScore = dato.index(max(dato))
        AwayScore = daty.index(max(daty))
        print(str(HomeScore) + " - " + str(AwayScore))

        
            
            
        




        
        
        
        
        
        
        
                
                

        
            
            
        




        
        
        
        
        
        
        
                
                
