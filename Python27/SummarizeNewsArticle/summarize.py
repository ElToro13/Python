from textblob import TextBlob
import requests
import json
import urllib

f = "https://api.diffbot.com/v3/article?token=f885465fe124b43884c0081bbaf19ab8&url=https://timesofindia.indiatimes.com/world/us/i-would-never-call-kim-jong-un-short-and-fat-tweets-us-president-donald-trump/articleshow/61613369.cms"
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
		if (qq[i][1] == 'RB' or qq[i][1] == 'RBR' or qq[i][1] == 'RBS' or qq[i][1] == 'JJ' or qq[i][1] == 'JJS' or qq[i][1] == 'JJR' or qq[i][1] == 'NNP'):
			fr+=1
	ll.append(fr)
	fr=0

print(data['objects'][0]['title'])
print("--------------")
for i in range(0,len(ll)):
	if(ll[i]>8):
		print(dh[i])
