import math
import pandas as pd
from H2H import H2H_Cal
from form_EPL import Form_Cal
from Shot import TSS, SSS


df = pd.read_csv('C:\\Users\\chinkasoni\\Desktop\\EPL.csv')
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
            return int(3091)
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
            return int(2214)
        else:
            return int(2034)

    
        
data =[]

class odds(MatchDetails):

    def __init__(self, Hometeam="", Awayteam=""):
        self.h = Hometeam
        self.a = Awayteam

        foo = MatchDetails(self.h, self.a)

        one = foo.hgs()
        two = foo.agc()
        three = foo.ohg()

        four = foo.hgc()
        five = foo.ags()
        six = foo.oag()
        

        H,A,T=H2H_Cal(self.h,self.a)
        FH,FA = Form_Cal(self.h,self.a)
        
        HSS = TSS(self.h)
        AS = SSS(self.a)
        
        
        HTS = (((one/38)*(two/38))/(three/760))+ FH/15 + H/T + HSS
        ATS =  (((four/38)*(four/38))/(three/760)) + FA/15 + A/T + AS
        

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
        FTS = str(HomeScore) + " - " + str(AwayScore)
        print(FTS)
        '''
        try:
            fi1 = open("C:\\Users\\chinkasoni\\AppData\\Local\\Programs\\Python\\Python36\\prediction.txt","r")
            fi2 = fi1.read()
            
        except:
            fi = fi = open("prediction.txt","w")
        fi = fi = open("prediction.txt","w")
        fi2 = fi2 + "\n" + FTS
        fi.write(fi2)
        
        '''
        

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
        
        
            
        




        
        
        
        
        
        
        
                
                

        
            
            
        




        
        
        
        
        
        
        
                
                
