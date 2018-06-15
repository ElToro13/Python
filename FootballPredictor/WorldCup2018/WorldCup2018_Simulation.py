import urllib2
from bs4 import BeautifulSoup
import requests
import pandas as pd
import random
import math
wct = ['Argentina', 'Australia', 'Belgium', 'Brazil', 'Colombia', 'Costa Rica', 'Croatia', 'Denmark', 'Egypt', 'England', 'France', 'Germany',
       'Iceland', 'Iran', 'Japan', 'Mexico', 'Morocco', 'Nigeria', 'Panama', 'Peru', 'Poland', 'Portugal', 'Russia', 'Saudi Arabia', 'Senegal',
       'Serbia', 'South Korea', 'Spain', 'Sweden', 'Switzerland', 'Tunisia', 'Uruguay']


df = pd.read_csv('WorldCup2018.csv')
#dates = [str(i)+'/'+str(j) if j>9 else str(i)+'/0'+str(j) for i in range(2016,2019) for j in range(1,13)]

#req = urllib2.Request('http://www.betexplorer.com/soccer/world/friendly-international/mutual-matches/?home=I9l9aqLq&away=f9OppQjp&where=0', None, headers)
def H2H():
    link1 = 'http://www.betexplorer.com/soccer/world/friendly-international/mutual-matches/?home='
    link2 = '&away='
    link3 = '&where=0'
    teamID = {'Russia': 'hrgrswHh', 'Saudi Arabia': 'biSY8ox4', 'Egypt':'bejDn7NN', 'Uruguay':'xMk44orG', 'Spain':'bLyo6mco', 'Portugal':'WvJrjFVN', 'Morocco': 'IDKYO3R8',
          'Iran': 'xrRx85iA', 'France':'QkGeVG1n', 'Australia':'xSrf6qMM', 'Peru':'Uend67D3','Denmark':'0KUdxQVi','Argentina':'f9OppQjp', 'Nigeria':'EBE2Xb3l','Croatia':'K8aznggo',
          'Iceland':'6TsAIrGN','Brazil':'I9l9aqLq','Switzerland':'rHJ2vy1B', 'Costa Rica':'C4ePE2kq', 'Serbia':'8Kl6iq0i', 'Germany':'ptQide1O', 'Mexico':'O6iHcNkd', 'Sweden': 'OQyqbHWB',
          'South Korea':'K6Gs7P6G', 'Belgium':'GbB957na', 'Panama':'OWKqbCfi', 'Tunisia': 'QqZVYk95', 'England':'j9N9ZNFA', 'Poland':'2HzmcynI','Senegal':'hOIsJLJr', 'Colombia':'G02s4PCS', 'Japan':'ULXPdOUj'}

    headers = { 'User-Agent' : 'Mozilla/5.0' }
    req = urllib2.Request('https://www.bbc.co.uk/sport/football/international-friendlies/scores-fixtures/2018-05', None, headers)
    page = urllib2.urlopen(req).read()
    #page = urllib2.urlopen(link1 + teamID['Germany'] + link2 + teamID['Brazil'])
    #page = urllib2.urlopen('https://stackoverflow.com/questions/44854334/no-handlers-could-be-found-for-logger-bs4-dammit')
    soup = BeautifulSoup(page, 'html.parser')
    scoH = soup.findAll('span',{'class':'sp-c-fixture__number sp-c-fixture__number--home sp-c-fixture__number--ft'})
    scoA = soup.findAll('span',{'class':'sp-c-fixture__number sp-c-fixture__number--away sp-c-fixture__number--ft'})
    print(len(scoH))
    print(len(scoA))
    Ht = soup.findAll('span',{'class':'gs-u-display-none gs-u-display-block@m qa-full-team-name sp-c-fixture__team-name-trunc'})
    del Ht[0]
    del Ht[0]
    print(len(Ht))
    for i in range(0,len(Ht),2):
        try:
            team1, team2 = Poisson(Ht[i].text, Ht[i+1].text)
            print(scoH[i].text, scoA[i].text)
            print(int(team1.index(max(team1))),int(team2.index(max(team2))))
        except:
            pass
        #print(Ht[-8].text.decode('UTF-8'), Ht[-6].text.decode('UTF-8'), Ht[-5].text.decode('UTF-8'),Ht[-4].text.decode('UTF-8'))
##        r = (float(Ht[-6].text))/float(Ht[-7].text)
##        return 1-r, r
        
        #print(Ht[-16].text.decode('UTF-8'), Ht[-14].text.decode('UTF-8'), Ht[-13].text.decode('UTF-8'),Ht[-12].text.decode('UTF-8'))
##    except IndexError:
##        #print('This two team have never played against each other')
##        return 0.0, 0.0
##    except KeyError as e:
##        print('Name of {} does not match in our Database'.format(e))


def Cal():
    group = {'A':'Russia,Egypt,Saudi Arabia,Uruguay', 'B':'Spain,Portugal,Morocco,Iran','C':'France,Australia,Peru,Denmark', 'D':'Argentina,Iceland,Croatia,Nigeria',
             'E':'Brazil,Switzerland,Costa Rica,Serbia','F':'Germany,Mexico,Sweden,South Korea','G':'Belgium,Panama,Tunisia,England', 'H':'Poland,Senegal,Colombia,Japan'}
##    group = {'A':'Brazil,Croatia,Cameroon,Mexico', 'B':'Spain,Netherlands,Chile,Australia','C':'Colombia,Greece,Ivory Coast,Japan', 'D':'Uruguay,Costa Rica,England,Italy',
##             'E':'Switzerland,France,Ecuador,Honduras','F':'Argentina,Nigeria,Bosnian-Herzegovina,Iran','G':'Germany,Portugal,Ghana,USA', 'H':'Belgium,Russia,Algeria,South Korea'}
##    group = {'A':'South Africa,Mexico,Uruguay,France', 'B':'Argentina,Nigeria,South Korea,Greece','C':'England,USA,Algeria,Slovenia', 'D':'Germany,Australia,Serbia,Ghana',
##             'E':'Netherlands,Denmark,Japan,Cameroon','F':'Italy,Paraguay,New Zealand,Slovakia','G':'Brazil,Portugal,North Korea,Ivory Coast', 'H':'Spain,Switzerland,Honduras,Chile'}
    
    final= {}
    for letter in ['A','B','C','D','E','F','G','H']:
        names = group[letter].split(',')
        points = {}
        gd = {}
        for n in names:
            points[n]=0
            gd[n]=0
        n=0
        for name in names:
            n+=1
            v = names[n:]
            for oppo in v:
                    team1, team2 = Poisson(name,oppo)
                    print(int(team1.index(max(team1))),int(team2.index(max(team2))))
                    gd[name]+= int(team1.index(max(team1))) - int(team2.index(max(team2)))
                    gd[oppo]+= int(team2.index(max(team2))) - int(team1.index(max(team1)))
                    if int(team1.index(max(team1))) > int(team2.index(max(team2))):
                            points[name] +=3
                            #points[oppo]-=1
                    elif int(team1.index(max(team1))) < int(team2.index(max(team2))):
                            points[oppo] +=3
                            #points[name]-=1
                    else:
                            points[oppo] -=float(df[oppo][12])
                            points[name] -=float(df[name][12])
        print points
        point = {}
        po =[]
        for team in names:
            point[points[team] + gd[team]] = team
            po.append(points[team] + gd[team])
        po = sorted(po, reverse=True)
        final[letter+'1'] = point[po[0]]
        final[letter+'2'] = point[po[1]]

    return final
        
        
#{'F1': 'Mexico', 'F2': 'Germany', 'G2': 'England', 'G1': 'Belgium', 'H2': 'Senegal',
#'E1': 'Brazil', 'H1': 'Colombia', 'A1': 'Uruguay', 'A2': 'Russia', 'B1': 'Spain',
#'B2': 'Portugal', 'C2': 'Peru', 'C1': 'France', 'E2': 'Serbia', 'D2': 'Croatia', 'D1': 'Argentina'}  
def R16(teams={}):
    r16 = {}
    print(teams)
    groupList = [A+B for A in ['A','B','C','D','E','F','G','H'] for B in ['1','2']]
    qL = [a+str(b) for a in ['Q'] for b in range(1,9)]
    for n in range(0,16,4):
        print(n)
        team1, team2 = Poisson(teams[groupList[n]], teams[groupList[n+3]])
        if team1.index(max(team1)) > team2.index(max(team2)):
            r16[qL[n/2]] = teams[groupList[n]]
        elif team1.index(max(team1)) < team2.index(max(team2)):
            r16[qL[n/2]] = teams[groupList[n+3]]
        else:
            if float(df[teams[groupList[n]]][12])< float(df[teams[groupList[n+3]]][12]):
                r16[qL[n/2]] = teams[groupList[n+3]]
            else:
                r16[qL[n/2]] = teams[groupList[n]]
                
        team1, team2 = Poisson(teams[groupList[n+1]], teams[groupList[n+2]])
        if team1.index(max(team1)) > team2.index(max(team2)):
            r16[qL[n/2+1]] = teams[groupList[n+1]]
        elif team1.index(max(team1)) < team2.index(max(team2)):
            r16[qL[n/2+1]] = teams[groupList[n+2]]
        else:
            if float(df[teams[groupList[n+1]]][12])< float(df[teams[groupList[n+2]]][12]):
                r16[qL[n/2+1]] = teams[groupList[n+2]]
            else:
                r16[qL[n/2+1]] = teams[groupList[n+1]]
    print(r16)
    return r16
    

def R8(team={}):
    r8={}
    qL = [a+str(b) for a in ['Q'] for b in range(1,9)]
    sL = [a+str(b) for a in ['S'] for b in range(1,5)]
    for i in range(0,5,4):
        team1,team2= Poisson(team[qL[i]], team[qL[i+2]])
        if team1.index(max(team1)) > team2.index(max(team2)):
            r8[sL[i/2]] = team[qL[i]]
        elif team1.index(max(team1)) < team2.index(max(team2)):
            r8[sL[i/2]] = team[qL[i+2]]
        else:
            if float(df[team[qL[i]]][12])< float(df[team[qL[i+2]]][12]):
                r8[sL[i/2]] = team[qL[i+2]]
            else:
                r8[sL[i/2]] = team[qL[i]]
        team1,team2= Poisson(team[qL[i+1]], team[qL[i+3]])
        if team1.index(max(team1)) > team2.index(max(team2)):
            r8[sL[i/2+1]] = team[qL[i+1]]
        elif team1.index(max(team1)) < team2.index(max(team2)):
            r8[sL[i/2+1]] = team[qL[i+3]]
        else:
            if float(df[team[qL[i+1]]][12])< float(df[team[qL[i+3]]][12]):
                r8[sL[i/2+1]] = team[qL[i+3]]
            else:
                r8[sL[i/2+1]] = team[qL[i+1]]
    print(r8)
    return r8

def R4(team={}):
    r4={}
    i=0
    sL = [a+str(b) for a in ['S'] for b in range(1,5)]
    fL = [a+str(b) for a in ['F'] for b in range(1,3)]
    team1,team2= Poisson(team[sL[i]], team[sL[i+2]])
    if team1.index(max(team1)) > team2.index(max(team2)):
        r4[fL[i/2]] = team[sL[i]]
    elif team1.index(max(team1)) < team2.index(max(team2)):
        r4[fL[i/2]] = team[sL[i+2]]
    else:
        if float(df[team[sL[i]]][12])< float(df[team[sL[i+2]]][12]):
            r4[fL[i/2]] = team[sL[i+2]]
        else:
            r4[fL[i/2]] = team[sL[i]]
    team1,team2= Poisson(team[sL[i+1]], team[sL[i+3]])
    if team1.index(max(team1)) > team2.index(max(team2)):
        r4[fL[i/2+1]] = team[sL[i+1]]
    elif team1.index(max(team1)) < team2.index(max(team2)):
        r4[fL[i/2+1]] = team[sL[i+3]]
    else:
        if float(df[team[sL[i+1]]][12])< float(df[team[sL[i+3]]][12]):
            r4[fL[i/2+1]] = team[sL[i+3]]
        else:
            r4[fL[i/2+1]] = team[sL[i+1]]
    print(r4)
    return r4

def Finals(team={}):
    final={}
    team1,team2= Poisson(team['F1'], team['F2'])
    if team1.index(max(team1)) > team2.index(max(team2)):
        final['WinningTeam'] = team['F1']
    elif team1.index(max(team1)) < team2.index(max(team2)):
        final['WinningTeam'] = team['F2']
    else:
        if float(df[team['F1']][12])< float(df[team['F2']][12]):
            final['WinningTeam'] = team['F2']
        else:
            final['WinningTeam'] = team['F1']
    print(final)
    return('Made by: Yash Soni')


def Poisson(HT='',AT=''):
    print(HT,AT)
    HTS = 0
    ATS = 0
    #print h2h_H, h2h_A
    ATS = ((float(df[AT][12])+(float(df[AT][13])))*(float(df[AT][2])/(float(df[AT][0]))))+random.uniform(0.1,float(df[AT][13]))         
    HTS = ((float(df[HT][12])+(float(df[HT][13])))*(float(df[HT][2])/(float(df[HT][0]))))+random.uniform(0.1,float(df[HT][13]))

        
    print(HTS,ATS)
                                                   
    return [(((math.exp(-HTS))*(math.pow(HTS,i))))/(math.factorial(i)) for i in range(0,5)], [(((math.exp(-ATS))*(math.pow(ATS,i))))/(math.factorial(i)) for i in range(0,5)]
   
    
print(Finals(R4(R8(R16(Cal())))))
