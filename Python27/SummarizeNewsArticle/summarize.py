from textblob import TextBlob
import requests
import json
import urllib


s = "http://www.thehindu.com/todays-paper/tp-opinion/the-ai-battlefield/article20376166.ece"  # Enter the URL of the news article here.
s =  urllib.quote_plus(s) # encoding the URL
f = "https://api.diffbot.com/v3/article?token="Your API Token"&url=" + s  # Here I have used diffbot API to scrap text only from the webite page. Get your API Key from thier official website https://www.diffbot.com/

r = requests.get(f)
data = json.loads(r.content.decode("UTF-8"))
dd = data['objects'][0]['text']
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


