from pycricbuzz import Cricbuzz
from CricketAPi import Cric
c = Cricbuzz()
data = []
length = c.matches()
size = len(length)
for i in range(0,size):
    iD = length[i]['id']
    src = length[i]['srs']
    mat = length[i]['mchdesc']
    data.append(iD)
    print(str(i+1) + ": " + iD + " -- " + src +  " " + mat)

print("Enter the index of tha match you would like to watch: ")
number = input()
number1 = int(number) - 1;
Cric(data[number1]) 





