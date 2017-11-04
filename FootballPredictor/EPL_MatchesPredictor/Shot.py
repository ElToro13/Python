import pandas as pd
import math

df = pd.read_csv('C:\\Users\\chinkasoni\\Desktop\\EPL.csv')

def TSS(TT=''):
    TS=0
    OT=0
    for i in range(0,len(df)):
        if(df['homeTeam'][i]==TT):
            TS+= df['homeShotsTotalFT'][i]
            OT+= df['homeShotsOnTargetFT'][i]
    return int(OT)/int(TS)

def SSS(TT=''):
    TS=0
    OT=0
    for i in range(0,len(df)):
        if(df['awayTeam'][i]==TT):
            TS+= df['awayShotsTotalFT'][i]
            OT+= df['awayShotsOnTargetFT'][i]
    return int(OT)/int(TS)



        
