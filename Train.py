import requests
import json

def Live():
    r = requests.get("https://api.railwayapi.com/v2/live/train/12010/date/14-09-2017/apikey/dx8s8oak/")
    data = json.loads(r.content)
    if r.status_code == 200:
        print("Total number of Stations: " + str(len(data["route"])))
        for x in range(len(data["route"])):        
            print(data["route"][x]["station"]["name"])

    else:
        print("Error fetching data")
