from textblob import TextBlob
from FSC import Userdata
import random

np = ('Ohh! go on..', 'Aww! Cheer up. Its not that bad.', 'You can get over this. May be you need good memes')
pp = ('Tell me about it!', 'I am all ears', 'Good to hear', 'Hmm')
ppp= ('Thats sounds great!', 'Someone had a great day, Huh!!')

print("Talk to Me! \n")
Ap=0
while True:
    test = input()
    output = Userdata()
    test = test.lower()
    #print(test)
    output3 = output.FilterData(test)
    output2 = output.SensorWords(output3)
    output4 = output.FilterOut(output3)
    #print(output2)
    #print(output4)
    wiki = TextBlob(output3)
    print(round(wiki.polarity,3))
    prP = wiki.polarity
    Ap = prP+Ap
    if(0.3>Ap>0):
        print(pp[random.randint(0, 3)])
    elif(Ap>0.3):
        print(ppp[random.randint(0, 1)])
    else:
        print(np[random.randint(0, 2)])



