import requests
import json
import datetime
import smtplib
## Bitcoin
'''
r = requests.get("https://www.zebapi.com/api/v1/market/ticker/btc/inr")

data = json.loads(r.content)

print(data["buy"])
print(data["sell"])
B = int(data["buy"])
S = int(data["sell"])
if B>S:
    print("Difference: " + str(B-S))
'''

## Train Details
'''
r = requests.get("https://api.railwayapi.com/v2/live/train/12010/date/14-09-2017/apikey/dx8s8oak/")
data = json.loads(r.content)
if r.status_code == 200:
    print("Total number of Stations: " + str(len(data["route"])))
    for x in range(len(data["route"])):        
        print(data["route"][x]["station"]["name"])

else:
    print("Error fetching data")
'''

# Time
'''
#Time =  datetime.datetime.now().time()
Time =  datetime.datetime.now().time().hour
minute =  datetime.datetime.now().time().minute
time = int(Time) - 12
if time < 12:    
    print(str(time) + ":" + str(minute) + " pm")
else:
    print(str(time) + ":" + str(minute) + " am")
'''    
# Email

sender = 'yashsoni2017@gmail.com'
receivers = ['yashsoni2017@gmail.com']

message = "From"

try:
   smtpObj = smtplib.SMTP('localhost')
   smtpObj.sendmail(sender, receivers, message)         
   print "Successfully sent email"
except NameError:
    print "ohh.. didnt work."




