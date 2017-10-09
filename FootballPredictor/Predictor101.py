#import matplotlib.pyplot as plt
import math

print("                   " + "FIFA World Cup 2018 Qualification - South America")
print("         " + "Standings - Week 17")

pa = [{'id':0}, {'name': 'Paraguay'}, {'points': 24}, {'form': 3},{'gd':-5},{'h2h':6},{'wins':6}, {'ash':0.36227}, {'asa':0.48923}]
Ve = [{'id':1}, {'name': 'Venezuela'}, {'points':9}, {'form': -3},{'gd':-17},{'h2h':6},{'wins':1}, {'ash':0.398507}, {'asa':0.38051}]
Br = [{'id':2}, {'name': 'Brazil'}, {'points': 38}, {'form': 15},{'gd':27},{'h2h':8},{'wins':11}, {'ash':0.83324}, {'asa':0.81539}]
Ch = [{'id':3}, {'name': 'Chile'}, {'points': 26}, {'form': -3},{'gd':2},{'h2h':5},{'wins':7}, {'ash':0.61587}, {'asa':0.48923}]
Ec = [{'id':4}, {'name': 'Ecuador'}, {'points': 20}, {'form': 3},{'gd':-1},{'h2h':5},{'wins':6}, {'ash':0.47096}, {'asa':0.65231}]
Ar = [{'id':5}, {'name': 'Argentina'}, {'points': 25}, {'form': 1},{'gd':1},{'h2h':8},{'wins':6}, {'ash':0.326051}, {'asa':0.380517}]
Pe = [{'id':6}, {'name': 'Peru'}, {'points': 25}, {'form': 9},{'gd':1},{'h2h':3},{'wins':7}, {'ash':0.50719}, {'asa':0.65231}]
Co = [{'id':7}, {'name': 'Colombia'}, {'points': 26}, {'form': 5},{'gd':2},{'h2h':9},{'wins':7}, {'ash':0.43473}, {'asa':0.43487}]
Ur = [{'id':8}, {'name': 'Uruguay'}, {'points': 28}, {'form': 9},{'gd':10},{'h2h':10},{'wins':8}, {'ash':0.61587}, {'asa':0.59795}]
Bo = [{'id':9}, {'name': 'Bolivia'}, {'points': 14}, {'form': -3},{'gd':-20},{'h2h':4},{'wins':4}, {'ash':0.43479}, {'asa':0.10871}]

paDS = [{'id':0}, {'name': 'Paraguay'}, {'points': 24}, {'form': 3},{'gd':1.11764},{'h2h':6},{'wins':6}, {'dsh':0.6523}, {'dsa':0.43473}]
VeDS = [{'id':1}, {'name': 'Venezuela'}, {'points':9}, {'form': 1},{'gd':1.05882},{'h2h':6},{'wins':1}, {'dsh':0.76103}, {'dsa':0.76078}]
BrDS = [{'id':2}, {'name': 'Brazil'}, {'points': 38}, {'form': 13},{'gd':2.23529},{'h2h':8},{'wins':11}, {'dsh':0.21743}, {'dsa':0.25359}]
ChDS = [{'id':3}, {'name': 'Chile'}, {'points': 26}, {'form': 3},{'gd':1.52941},{'h2h':5},{'wins':7}, {'dsh':0.54359}, {'dsa':0.507191}]
EcDS = [{'id':4}, {'name': 'Ecuador'}, {'points': 20}, {'form': -1},{'gd':1.47058},{'h2h':5},{'wins':6}, {'dsh':0.54359}, {'dsa':0.57964}]
ArDS = [{'id':5}, {'name': 'Argentina'}, {'points': 25}, {'form': 7},{'gd':0.94117},{'h2h':8},{'wins':6}, {'dsh':0.27179}, {'dsa':0.36227}]
PeDS = [{'id':6}, {'name': 'Peru'}, {'points': 25}, {'form': 9},{'gd':1.52941},{'h2h':3},{'wins':7}, {'dsh':0.70667}, {'dsa':0.43473}]
CoDS = [{'id':7}, {'name': 'Colombia'}, {'points': 26}, {'form': 7},{'gd':1.17947},{'h2h':9},{'wins':7}, {'dsh':0.38051}, {'dsa':0.398507}]
UrDS = [{'id':8}, {'name': 'Uruguay'}, {'points': 28}, {'form': 1},{'gd':1.64705},{'h2h':10},{'wins':8}, {'dsh':0.27179}, {'dsa':0.47096}]
BoDS = [{'id':9}, {'name': 'Bolivia'}, {'points': 14}, {'form': 7},{'gd':0.82352},{'h2h':4},{'wins':4}, {'dsh':0.65231}, {'dsa':0.79701}]



'''
pa = [{'id':0}, {'name': 'Paraguay'}, {'points': 57+28+30+12}, {'form': 9},{'gd':3+4+6-14},{'h2h':6}]
Ve = [{'id':1}, {'name': 'Venezuela'}, {'points': 31+18+16+20}, {'form': 4},{'gd':-23-8-26-6},{'h2h':6}]
Br = [{'id':2}, {'name': 'Brazil'}, {'points': 38+34+34+30+34}, {'form': 11},{'gd':27+22+18+14+20},{'h2h':8}]
Ch = [{'id':3}, {'name': 'Chile'}, {'points': 26+33+22+12+28}, {'form': 6},{'gd':2+10-4-12+4},{'h2h':5}]
Ec = [{'id':4}, {'name': 'Ecuador'}, {'points': 20+23+28+31+25}, {'form': 0},{'gd':-1-4+4+3+4},{'h2h':5}]
Ar = [{'id':5}, {'name': 'Argentina'}, {'points': 25+28+34+43+32}, {'form': 6},{'gd':1+3+12+27+20},{'h2h':8}]
Pe = [{'id':6}, {'name': 'Peru'}, {'points': 25+13+18+16+15}, {'form': 13},{'gd':1-23-8-11-9},{'h2h':3}]
Co = [{'id':7}, {'name': 'Colombia'}, {'points': 26+23+24+27+30}, {'form': 5},{'gd':2-4+8+5+14},{'h2h':9}]
Ur = [{'id':8}, {'name': 'Uruguay'}, {'points': 28+24+25+27+25}, {'form': 5},{'gd':10+8-8+6},{'h2h':10}]
Bo = [{'id':9}, {'name': 'Bolivia'}, {'points': 14+15+14+18+12}, {'form': 7},{'gd':-20-14-17-12-13},{'h2h':4}]
'''

teams = [pa, Ve, Br, Ch, Ec, Ar, Pe, Co, Ur, Bo]
away = [VeDS,paDS, ChDS, BrDS, ArDS, EcDS, CoDS, PeDS, BoDS, UrDS]

pos = 9
data1 =[]
for k in range(0,10):
    for j in range(0,10):
        if(teams[k][0]['id']!=teams[j][0]['id']):
            if(teams[k][2]['points'] > teams[j][2]['points']):
                pos = pos - 1
            elif(teams[k][2]['points'] == teams[j][2]['points']):
                if(teams[k][3]['form'] > teams[j][3]['form']):
                    pos = pos - 1
                    
    data1.append(str(pos)+ " . " + teams[k][1]['name'] + " - " + str(teams[k][2]['points']))
    pos = 9

data1 = sorted(data1)
for h in range(0,10):
    f,g,d,h,j = data1[h].split()
    print("           "+ str(int(f)+1) + g + " " + d + " " + h + " " + j)


print("           " + "------------------------------------------------------------------")

for k in range(0,10,2):
    paSt = ((teams[k][7]['ash'])*(away[k][8]['dsa'])*(3.067)) + ((teams[k][3]['form']/15)+ (teams[k][5]['h2h'])/15)
    VeSt = ((away[k+1][8]['dsa'])*(teams[k+1][8]['asa'])*(2.044)) + ((teams[k+1][3]['form']/15) + (teams[k+1][5]['h2h'])/15)
    #print(paSt)
    #print(VeSt)
    ScoreHome=[]
    ScoreAway =[]
    for i in range(0,6):
        ScoreHome.append(round(((math.exp(-paSt))*(math.pow(paSt, i)))/(math.factorial(i)),4)) # Score prediction based on Poisson Distribution
    for j in range(0,6):
        ScoreAway.append(round(((math.exp(-VeSt))*(math.pow(VeSt, j)))/(math.factorial(j)),4)) # Score prediction based on Poisson Distribution
    #print(ScoreHome)
    #print(ScoreAway)
    confidence = (max(ScoreHome) * max(ScoreAway))*100
    DispHomeScore = ScoreHome.index(max(ScoreHome))
    DispAwayScore = ScoreAway.index(max(ScoreAway))
    gd = abs(DispHomeScore - DispAwayScore)
    #print(gd)
    if (abs((max(ScoreHome) - max(ScoreAway)))< 0.1):
        result = " Draw"
        teams[k][2]['points'] = teams[k][2]['points'] + 1
        teams[k+1][2]['points'] = teams[k+1][2]['points'] + 1
        DispHomeScore = 0
        DispAwayScore = 0
    else:        
        if(DispHomeScore > DispAwayScore):
            result = teams[k][1]['name']+ " Wins"
            teams[k][2]['points'] = teams[k][2]['points'] + 3
            teams[k][4]['gd'] = teams[k][4]['gd'] + gd
            teams[k+1][4]['gd'] = teams[k+1][4]['gd'] - gd
            teams[k][6]['wins'] = teams[k][6]['wins'] + 1
        elif(DispHomeScore < DispAwayScore):
            result = teams[k+1][1]['name'] + " Wins"
            teams[k+1][2]['points'] = teams[k+1][2]['points'] + 3
            teams[k+1][4]['gd'] = teams[k+1][4]['gd'] + gd
            teams[k][4]['gd'] = teams[k][4]['gd'] - gd
        else:
            result = " Draw"
            teams[k][2]['points'] = teams[k][2]['points'] + 1
            teams[k+1][2]['points'] = teams[k+1][2]['points'] + 1
        
    print("           " + teams[k][1]['name'] + "  " + str(DispHomeScore) + " - " + str(DispAwayScore) + "  " + teams[k+1][1]['name'] + "  //  " + result + " (With Confidence: " + str(round(confidence,2)) + "%)" )
    print()

pos = 9
data1=[]
for k in range(0,10):
    for j in range(0,10):
        if(teams[k][0]['id']!=teams[j][0]['id']):
            if(teams[k][2]['points'] > teams[j][2]['points']):
                pos = pos - 1
            elif(teams[k][2]['points'] == teams[j][2]['points']):
                if(teams[k][4]['gd'] > teams[j][4]['gd']):
                    pos = pos - 1
                elif(teams[k][4]['gd'] == teams[j][4]['gd']):
                    if(teams[k][6]['wins'] > teams[j][6]['wins']):
                        pos = pos - 1
                
                    
    data1.append(str(pos)+ " . " + teams[k][1]['name'] + "  -  " + str(teams[k][2]['points']))
    pos = 9
    
data1 = sorted(data1)
print("           ----------predictions as of 9th October 2017 - 02:28 pm----------")
print("                   FIFA World Cup 2018 Qualification - South America")
print("             Predicted Standings - Week 18 - (Form(Home Vs Away), H2H & Poisson)")
print()

print()

for h in range(0,10):
    if(h < 4):        
        f,g,d,q,j = data1[h].split()
        print("                           " + str(int(f)+1) + g + " " + d + " " + q + " " + j + "    **Qualified**")
    elif(h == 4):
        f,g,d,q,j = data1[h].split()
        print("                           " + str(int(f)+1) + g + " " + d + " " + q + " " + j + "    **PlayOff**")
    else:
        f,g,d,q,j = data1[h].split()
        print("                           " + str(int(f)+1) + g + " " + d + " " + q + " " + j + "    **Eliminated**")

'''
plt.axis([0, 16, 0, 40])      
x1 = [0,5,10]
y1 = [15,25,36.66]
plt.plot(x1, y1, label = "World Cup 2018")

x1 = [0,5,10]
y1 = [30,36.66,12.5]
plt.plot(x1, y1, label = "World Cup 2014")

x1 = [0,5,10]
y1 = [18.75,20.83,31.25]
plt.plot(x1, y1, label = "World Cup 2010")

x1 = [0,5,10]
y1 = [25,28.57,28.57]
plt.plot(x1, y1, label = "World Cup 2006")

x1 = [0,5,10]
y1 = [20,14.285,31.42]
plt.plot(x1, y1, label = "World Cup 2002")

x1 = [0,4,8,12,16]
y1 = [24.44,25,27.77,22.32,26.66]
plt.plot(x1, y1, 'r--', label = "Overall % of Draws 2002-2014")        

plt.legend()
plt.grid(True)
plt.show()
'''
