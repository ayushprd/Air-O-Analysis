import json 
import requests
import urllib.request, json 
import pprint

request=requests.get('https://api.openaq.org/v1/measurements?city=Siliguri&limit=1')
data = request.json()
t1=json.dumps(data)
t=json.loads(t1)
data=t['results']
#pprint.pprint(data)
i=0
'''for i in range(5) :
    pprint.pprint(data[i])
pprint.pprint(data[0]['date']['local'])
pprint.pprint(data[len(data)-1]['date']['local'])'''
pprint.pprint(data)  

#print(request.text)
