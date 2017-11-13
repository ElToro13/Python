from textblob import TextBlob
import requests
import json
import urllib
import os

file_1 = open("PATH of the text version of the book ","r")
dd =  file_1.read()
dd = dd.decode("UTF-8")
blob = TextBlob(dd)
#print(blob)
dh = blob.split(".")
print(len(dh))
#print(dh)
ll = []
fr = 0
qq = []
for lines in dh:
	blob = TextBlob(lines)
	qq = blob.tags
	for i in range(0,len(qq)):
		if (qq[i][1] == 'RB' or qq[i][1] == 'RBR' or qq[i][1] == 'RBS' or qq[i][1] == 'JJ' or qq[i][1] == 'JJS' or qq[i][1] == 'JJR' or qq[i][1] == 'NNP' or qq[i][1] == 'NNS'):
			fr+=1
	ll.append(fr)
	fr=0

#print(data['objects'][0]['title'])
file_write = open("testfile4.txt","w")
print("--------------")
for i in range(0,len(ll)):
	if(ll[i]>8):
		file_write.write(dh[i].encode("UTF-8"))

file_write.close()
if(os.stat("testfile4.txt").st_size == 0):
        print("Nothing Happened")
else:
        print("Summarizing completed succesfully.")
