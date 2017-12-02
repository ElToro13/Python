from textblob import TextBlob
import requests
import json
import urllib
import random
import urllib2




class datos:
    
    def __init__(self, link=""):
        self.link = link

    def UserInput(self):

        #s = "http://www.thehindu.com/todays-paper/tp-opinion/the-ai-battlefield/article20376166.ece"
        #s = "https://timesofindia.indiatimes.com/india/no-country-can-thrive-without-equal-opportunity-for-half-its-population/articleshow/61827809.cms"
        #s = "http://www.wionews.com/india-news/watch-india-an-inspiration-for-the-world-ivanka-trump-at-ges-2017-25369"
        #s = "http://www.wionews.com/world/london-police-closes-roads-to-gherkin-skyscraper-after-suspicious-vehicle-found-25370"
        #s = "https://timesofindia.indiatimes.com/city/hyderabad/made-in-india-bot-mitra-to-welcome-pm-narendra-modi-ivanka-trump-at-ges/articleshow/61827978.cms"
        #s = "http://www.wionews.com/sports/cricket-australia-crush-england-by-10-wickets-in-1st-test-25214"
        #s = "http://www.hindustantimes.com/business-news/india-gdp-can-grow-by-150bn-if-it-halves-gender-gap-ivanka-trump/story-ch3QRAcwZpCyGMSiZ3SPcO.html"
        #s = "http://www.hindustantimes.com/fashion-and-trends/manushi-chhillar-on-her-winning-moment-wish-i-had-given-a-more-lady-like-reaction/story-pCJlLA3yUeoz6QucVVZDPI.html?li_source=LI&li_medium=recommended-for-you"

        s =  urllib.quote_plus(str(self.link))
        f = "https://api.diffbot.com/v3/article?token=2aca4b94adb14d3c02619c02a3d22cac&url=" + s


        r = requests.get(f)
        data = json.loads(r.content.decode("UTF-8"))
        #print(data)
        dd = data['objects'][0]['text']
        return data['objects'][0]['title'], dd, data['objects'][0]['images'][0]['url']


    def Summarize(self, data):
        blob = TextBlob(data)
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
        return ll, dh







