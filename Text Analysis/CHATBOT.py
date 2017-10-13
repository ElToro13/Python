from textblob import TextBlob
from FSC import Userdata

while True:
    test = input("Talk to Me! \n")
    output = Userdata()
    test = test.lower()
    print(test)
    output3 = output.FilterData(test)
    output2 = output.SensorWords(output3)
    output4 = output.FilterOut(output3)
    print(output2)
    print(output4)
    wiki = TextBlob(output4)
    print(wiki.polarity)


