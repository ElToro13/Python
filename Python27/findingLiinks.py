##import urllib2
##import re
##
###connect to a URL
###http://www.thehindu.com/news/international/
###http://indianexpress.com/section/world/
###http://www.hindustantimes.com/world-news/  120-150 2 
###https://timesofindia.indiatimes.com/world
##website = urllib2.urlopen("http://www.thehindu.com/news/international/")
##
###read html code
##html = website.read()
###use re.findall to get all the links
##links = re.findall('"((http|ftp)s?://.*?)"', html)
###print len(links)
####for i in range(150,200):
####    print(links[i])
##for i in links:
##    print(i)
##
##
###'http://www.hindustantimes.com/world-news/

from suma import SaveInWord
import webhoseio
from random import *
while True:
    try:
        webhoseio.config(token="76009b9e-ef73-4a95-ae19-3f8a58138651")
        s = raw_input("Enter: ")
        query_params = {
            "q": s + " language:english  has_video:false site_type:news",
            "ts": "1511956744788",
            "sort": "crawled"
        }
        output = webhoseio.query("filterWebContent", query_params)
        try:
            for i in range(10,15):
                print output['posts'][i]['title']
                print output['posts'][i]['thread']['site']
                #print(output['posts'][i]['url'])
                SaveInWord(output['posts'][i]['url'], s+str(i+1))
                
                                         
        except Exception as e:
            print("No more news", e)
    except KeyboardInterrupt:
        break
                                 
            

