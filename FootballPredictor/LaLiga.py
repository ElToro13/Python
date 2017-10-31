import math
import pandas as pd

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
        data = []
        for i in range(0,len(division)):
            if(hometeamname[i]==self.HT):
                data.append(division[i])
                break
        if(data[0] == 'EPL'):
            return int(1173)
        elif(data[0] == 'Bundesliga'):
            return int(2493)
        elif(data[0] == 'La_Liga'):
            return int(1247)
        else:
            return int(2760)

    def oag(self):
        dat = []
        for i in range(0,len(division)):
            if(awayteamname[i]==self.AT):
                dat.append(division[i])
                break
        if(dat[0] == 'EPL'):
            return int(916)
        elif(dat[0] == 'Bundesliga'):
            return int(1953)
        elif(dat[0] == 'La_Liga'):
            return int(914)
        else:
            return int(2034)

    
        


class odds(MatchDetails):

    def __init__(self, Hometeam="", Awayteam="", ffH = 0, ffA =0, h2hH=0, h2hA=0,gsH=0,gcH=0,gsA=0,gcA=0):
        self.h = Hometeam
        self.a = Awayteam
        self.ffH = ffH
        self.ffA = ffA
        self.h2hH = h2hH
        self.h2hA = h2hA
        self.gsH = gsH
        self.gcH = gcH
        self.gsA = gsA
        self.gcA = gcA

        foo = MatchDetails(self.h, self.a)

        one = foo.hgs()
        two = foo.agc()
        three = foo.ohg()

        four = foo.hgc()
        five = foo.ags()
        six = foo.oag()

        '''

        if(self.h == 'Leicester City'):
            zero = one/57
            zero1 = four/57
        elif(self.h == 'Bournemouth' or self.h == 'Burnley'):
            zero = one/38
            zero1 = four/38
        else:
            zero = one/95
            zero1 = four/95

        if(self.a == 'Leicester City'):
            beta = two/57
            beta1 = five/57
        elif(self.a == 'Bournemouth' or self.a == 'Burnley'):
            beta = two/38
            beta1 = five/38
        else:
            beta = two/95
            beta1 = five/95
        '''
    
        HTS = (((one/38)*(two/38))/(three/760))+ self.ffH/15 + self.h2hH/15
        ATS =  (((four/38)*(four/38))/(three/760)) + self.ffA/15 + self.h2hA/15

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
        


        HTS =  (((one/38)*(two/38))/(three/760))
        ATS =  ((four/38)*(four/38))/(three/760)



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
        
            
            
        




        
        
        
        
        
        
        
                
                
