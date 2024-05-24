from datetime import datetime 
import requests
import json

def ri3valeurhhh(L):
  L1=[]
  for i in range(0,len(L),3):
      L1.append(L[i])
  return L1

dateLyouma=datetime.today().strftime("%Y-%m-%d")
dateLyouma2=datetime.today().strftime("%d-%m-%Y")
lyoumaName=datetime.today().strftime("%A")
jours={'Monday':'Lundi','Tuesday':'Mardi', 'Wednesday':'Mercredi', 'Thursday':'jeudi', 'Friday':'Vendredi', 'Saturday':'samedi','Sunday':'Dimanche'}
Lyouma=jours[lyoumaName]
url="https://api.open-meteo.com/v1/forecast?"
url=url+"latitude=31,51&longitude=-9,77"
url=url+"&hourly=temperature_2m"
url=url+"&hourly=windspeed_10m"
url=url+"&hourly=cloud_cover"
url=url+"&hourly=precipitation"
url=url+"&daily=sunrise"
url=url+"&daily=sunset"
url=url+"&start_date="+dateLyouma
url=url+"&end_date="+dateLyouma

response=requests.get(url)
response=requests.get(url).content.decode('utf-8')
Data = json.loads(response)
daytemperature=Data[0]['hourly']['temperature_2m']
windsliste=Data[0]['hourly']['windspeed_10m']
cloudcover=Data[0]['hourly']['cloud_cover']
precipitation=Data[0]['hourly']['precipitation']
sunrise=Data[0]['daily']['sunrise']
sunset=Data[0]['daily']['sunset']

listetemperature=ri3valeurhhh(daytemperature)
listewind=ri3valeurhhh(windsliste)
listcloud=ri3valeurhhh(cloudcover)
listprecipitation=ri3valeurhhh(precipitation)
def Data1():
    dataMeteo=[ { "temps":"","temperature":"","wind":"","precipitation":"","image":"" } for i in range(8) ]
    for i in range(8):
        dataMeteo[i]["temps"]=int(i*3)
        dataMeteo[i]["temperature"]=listetemperature[i]
        dataMeteo[i]["precipitation"]=listprecipitation[i]
        dataMeteo[i]["wind"]=listewind[i]   
    return dataMeteo    
dataMeteo= Data1()

sunr=sunrise[0][11:13]
suns=sunset[0][11:13]
for i in range(8):
    
    if i * 3 >= int(sunr) and i * 3 < int(suns):
        
        if cloudcover[i] < 50:
            dataMeteo[i]["image"] = "static/img/sunmorecloud.png"
        else:
            dataMeteo[i]["image"] = "static/img/sun.png"
        if dataMeteo[i]["precipitation"] > 5:
            dataMeteo[i]["image"] = "static/img/rain.png"
    else:
        if cloudcover[i] < 50:
            dataMeteo[i]["image"] = "static/img/mooncloud.png"
        else:
            dataMeteo[i]["image"] = "static/img/moon.png"
        if dataMeteo[i]["precipitation"] > 5:
            dataMeteo[i]["image"] = "static/img/rain.png"


def get_current_hour():
    now=datetime.now()
    return now.hour
def get_current_min():
    now=datetime.now()
    return now.minute
current_H=get_current_hour()
current_M=get_current_min()

#tttthhhhhhhhhh
Pm=0.2
Pb=0.5
