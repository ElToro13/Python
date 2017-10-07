#import matplotlib.pyplot as plt

print("FIFA World Cup 2018 Qualification - South America")
print("Standings - Week 17")
pa = [{'id':0}, {'name': 'Paraguay'}, {'points': 24}, {'form': 7},{'gd':1.11764},{'h2h':6}]
Ve = [{'id':1}, {'name': 'Venezuela'}, {'points':9}, {'form': 3},{'gd':1.05882},{'h2h':6}]
Br = [{'id':2}, {'name': 'Brazil'}, {'points': 38}, {'form': 11},{'gd':2.23529},{'h2h':8}]
Ch = [{'id':3}, {'name': 'Chile'}, {'points': 26}, {'form': 3},{'gd':1.52941},{'h2h':5}]
Ec = [{'id':4}, {'name': 'Ecuador'}, {'points': 20}, {'form': -5},{'gd':1.47058},{'h2h':5}]
Ar = [{'id':5}, {'name': 'Argentina'}, {'points': 25}, {'form': 5},{'gd':0.94117},{'h2h':8}]
Pe = [{'id':6}, {'name': 'Peru'}, {'points': 25}, {'form': 11},{'gd':1.52941},{'h2h':3}]
Co = [{'id':7}, {'name': 'Colombia'}, {'points': 26}, {'form': 7},{'gd':1.17947},{'h2h':9}]
Ur = [{'id':8}, {'name': 'Uruguay'}, {'points': 28}, {'form': 3},{'gd':1.64705},{'h2h':10}]
Bo = [{'id':9}, {'name': 'Bolivia'}, {'points': 14}, {'form': 5},{'gd':0.82352},{'h2h':4}]

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
    print(str(int(f)+1) + g + " " + d + " " + h + " " + j) 

print("------------------------")


paSt = (pa[2]['points']/51) + (pa[3]['form']/15) + (pa[5]['h2h']) + (pa[4]['gd'] + 0.2) # Last numeric is added for home advantage based on recent form of the team
VeSt = (Ve[2]['points']/51) + (Ve[3]['form']/15) + (Ve[5]['h2h']) + (Ve[4]['gd']  - 0.2)
BrSt = (Br[2]['points']/51) + (Br[3]['form']/15) + (Br[5]['h2h']) + (Br[4]['gd'] + 1)
ChSt = (Ch[2]['points']/51) + (Ch[3]['form']/15) + (Ch[5]['h2h']) + (Ch[4]['gd'] - 0.2)
EcSt = (Ec[2]['points']/51) + (Ec[3]['form']/15) + (Ec[5]['h2h']) + (Ec[4]['gd'] + 0.2)
ArSt = (Ar[2]['points']/51) + (Ar[3]['form']/15) + (Ar[5]['h2h']) + (Ar[4]['gd'] + 0.0666)
PeSt = (Pe[2]['points']/51) + (Pe[3]['form']/15) + (Pe[5]['h2h']) + (Pe[4]['gd'] + 0.6)
CoSt = (Co[2]['points']/51) + (Co[3]['form']/15) + (Co[5]['h2h']) + (Co[4]['gd'] + 0.333)
UrSt = (Ur[2]['points']/51) + (Ur[3]['form']/15) + (Ur[5]['h2h']) + (Ur[4]['gd'] + 0.6)
BoSt = (Bo[2]['points']/51) + (Bo[3]['form']/15) + (Bo[5]['h2h']) + (Bo[4]['gd'] -0.2)
'''
paSt = (pa[2]['points']/255) + (pa[3]['form']/15) + (pa[5]['h2h']) + (pa[4]['gd']/5 + 1.2)
VeSt = (Ve[2]['points']/255) + (Ve[3]['form']/15) + (Ve[5]['h2h']) + (Ve[4]['gd']/5)
BrSt = (Br[2]['points']/255) + (Br[3]['form']/15) + (Br[5]['h2h']) + (Br[4]['gd']/5 + 1.2)
ChSt = (Ch[2]['points']/255) + (Ch[3]['form']/15) + (Ch[5]['h2h']) + (Ch[4]['gd']/5)
EcSt = (Ec[2]['points']/255) + (Ec[3]['form']/15) + (Ec[5]['h2h']) + (Ec[4]['gd']/5 + 1.2)
ArSt = (Ar[2]['points']/255) + (Ar[3]['form']/15) + (Ar[5]['h2h']) + (Ar[4]['gd']/5)
PeSt = (Pe[2]['points']/255) + (Pe[3]['form']/15) + (Pe[5]['h2h']) + (Pe[4]['gd']/5 + 1.2)
CoSt = (Co[2]['points']/255) + (Co[3]['form']/15) + (Co[5]['h2h']) + (Co[4]['gd']/5)
UrSt = (Ur[2]['points']/255) + (Ur[3]['form']/15) + (Ur[5]['h2h']) + (Ur[4]['gd']/5 + 1.2)
BoSt = (Bo[2]['points']/255) + (Bo[3]['form']/15) + (Bo[5]['h2h']) + (Bo[4]['gd']/5)
'''

results = [paSt, VeSt, BrSt, ChSt, EcSt, ArSt, PeSt, CoSt, UrSt, BoSt]
teams = [pa, Ve, Br, Ch, Ec, Ar, Pe, Co, Ur, Bo]
data = []


for i in range(0,10,2):
    print("abs value: " + str(abs((abs(results[i]) - abs(results[i+1]))/abs(results[i] + results[i+1]))))
    if(abs((abs(results[i]) - abs(results[i+1]))/(abs(results[i]) + (results[i+1]))) < 0.247058823):
        teams[i][2]['points'] = teams[i][2]['points'] + 1
        teams[i+1][2]['points'] = teams[i+1][2]['points'] + 1
        print(teams[i][1]['name'] + "(H)  -  (A)" + teams[i+1][1]['name'] + " // Draw")
        print(results[i])
        print(results[i+1])
        print()
    elif(results[i] > results[i+1]):
        teams[i][2]['points'] = teams[i][2]['points'] + 3
        print(teams[i][1]['name'] + "(H)  -  (A)" + teams[i+1][1]['name'] + " // " + teams[i][1]['name'] + " Wins!")
        print(results[i])
        print(results[i+1])
        print()
    else:
        teams[i+1][2]['points'] = teams[i+1][2]['points'] + 3
        print(teams[i][1]['name'] + "(H)  -  (A)" + teams[i+1][1]['name'] + " // " + teams[i+1][1]['name'] + " Wins!")
        print(results[i])
        print(results[i+1])
        print()
    
pos = 9
data1=[]
for k in range(0,10):
    for j in range(0,10):
        if(teams[k][0]['id']!=teams[j][0]['id']):
            if(teams[k][2]['points'] > teams[j][2]['points']):
                pos = pos - 1
            elif(teams[k][2]['points'] == teams[j][2]['points']):
                if(teams[k][3]['form'] > teams[j][3]['form']):
                    pos = pos - 1
                elif(teams[k][3]['form'] == teams[j][3]['form']):
                    if(teams[k][4]['gd'] > teams[j][4]['gd']):
                        pos = pos - 1
                
                    
    data1.append(str(pos)+ " . " + teams[k][1]['name'] + "  -  " + str(teams[k][2]['points']))
    pos = 9
    
data1 = sorted(data1)
print("FIFA World Cup 2018 Qualification - South America")
print("Predicted Standings - Week 18")
print()
print("----------predictions as of 6th October 2017 - 10:17 pm")
print()

for h in range(0,10):
    if(h < 4):        
        f,g,d,q,j = data1[h].split()
        print(str(int(f)+1) + g + " " + d + " " + q + " " + j + "    **Qualified**")
    elif(h == 4):
        f,g,d,q,j = data1[h].split()
        print(str(int(f)+1) + g + " " + d + " " + q + " " + j + "    **PlayOff**")
    else:
        f,g,d,q,j = data1[h].split()
        print(str(int(f)+1) + g + " " + d + " " + q + " " + j + "    **Did not Qualify**")

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
