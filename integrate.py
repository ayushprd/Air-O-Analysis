#    request=requests.get('https://api.openaq.org/v1/measurements?city=Siliguri&limit=1')#
#(distance(cordinate_ground_data,location_entered))>50
import json 
import urllib.request 
import requests
import pprint
import csv
import sys
import pprint
import statistics
from geopy.geocoders import Nominatim
from haversine import haversine, Unit

def distance(cordinate1,cordinate2):
    return haversine(cordinate1, cordinate2)

def ground(link):
    request=requests.get(link)
    data = request.json()
    t1=json.dumps(data)
    t=json.loads(t1)
    data=t['results']
    return data
    #pprint.pprint(data)
    ''' i=0
    for i in range(5) :
        pprint.pprint(data[i])
    pprint.pprint(data[0]['date']['local'])
    pprint.pprint(data[len(data)-1]['date']['local'])
    pprint.pprint(data)  

    #print(request.text)'''

def satilite(fileName):
    row = ['Year', ' Month', ' Date' ,'Latitude','longitude','AOD1','AOD2','STD3']
    with open(fileName, 'r') as readFile:
        reader = csv.reader(readFile)
        lines = list(reader)
        lines[0] = row

    with open(fileName, 'w') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(lines)

    readFile.close()
    writeFile.close()
    reader = csv.DictReader(open(fileName, 'r'))
    dict_list = []
    for line in reader:
        dict_list.append(line)
    return dict_list

def sati_AOD(dict,coordinates):
    min=10000
    i=0
    index=0
    for i in range(len(dict)):
        c=(float)(dict[i]['Latitude'])
        a=(float)(dict[i]['longitude'])  
        co=(c,a)
        if(distance(co,coordinates)<=min):
            index=i
            min=distance(co,coordinates)
    val=((float)(dict[index]['AOD1'])+(float)(dict[index]['AOD2']))/2.0
    return val

def variance(sample):
    if(len(sample)==0):
        return -1
    standard_Value=10; # this is our standard value lowering it means closer points to a graph and vice versa 
    temp=[]
    index=0
    sample_new=sample
    minimum_Deviation=0
    length=len(sample)
    mean= statistics.mean(sample) 
    standard_Deviation=statistics.stdev(sample)
    most_Accurate_Value=sample[0]
    val=abs(sample[0]-mean)

    if(standard_Deviation<=standard_Value): # checking if the data given already fits our definition 
        #finding the value which is closet to mean 
        for i in range(length):
            if((abs(sample[i]-mean))<=val):
                val=abs(sample[i]-mean)
                most_Accurate_Value=sample[i]
    else :
        #2.
        for i in range(length):
            for j in range (len(sample)):
                temp=(sample[:j]+sample[j+1:])
                minimum_Deviation=statistics.stdev(temp)
                if(minimum_Deviation<standard_Deviation):
                    standard_Deviation=minimum_Deviation  
                    index=j  
                    sample_new=temp
            sample=sample_new 
            if(len(sample)==2):
                break  
            elif(standard_Deviation<=standard_Value):
                break
        mean=statistics.mean(sample)
        length=len(sample)
        for i in range(length):
            if((abs(sample[i]-mean))<=most_Accurate_Value):
                val=abs(sample[i]-mean)
                most_Accurate_Value=sample[i]
    return most_Accurate_Value

def ground_Aqi(ground_data,location_entered):
    dict =[]
    i=0
    while i<len(ground_data)-7:
        list1=[0,0,0,0,0,0,0] #[pm10,pm25,o3,no2,co,no3,so2]
        cordinate_ground_data=(ground_data[i]['coordinates']['latitude'],ground_data[i]['coordinates']['longitude'])
        if(True):
            for j in range(7):
                if((i+j)>=len(ground_data)):
                    break
                elif(ground_data[i+j]['parameter']=='pm10'and list1[0]==0):
                    list1[0]=(ground_data[i+j]['value'])
                elif(ground_data[i+j]['parameter']=='pm25'and list1[1]==0):
                    list1[1]=(ground_data[i+j]['value'])
                elif(ground_data[i+j]['parameter']=='o3'and list1[2]==0):
                    list1[2]=(ground_data[i+j]['value'])
                elif(ground_data[i+j]['parameter']=='no2'and list1[3]==0):
                    list1[3]=(ground_data[i+j]['value'])
                elif(ground_data[i+j]['parameter']=='co'and list1[4]==0):
                    list1[4]=0
                elif(ground_data[i+j]['parameter']=='no3'and list1[5]==0):
                    list1[5]=(ground_data[i+j]['value'])
                elif(ground_data[i+j]['parameter']=='so2'and list1[6]==0):
                    list1[6]=(ground_data[i+j]['value'])
                else :
                    i=i+j
                    dict.append(max(list1))
                    break 
    return variance(dict)        

def generator():
    geolocator = Nominatim(user_agent="Enter location")
    #need to make this automated
    location_entered='Delhi Chanakyapuri'
    actual_location= geolocator.geocode(location_entered)
    location_entered=(actual_location.latitude,actual_location.longitude)
    url = ('https://api.openaq.org/v1/measurements?city=Delhi')  
    ground_data=ground(url)
    sat=satilite('C:\cpp\Python\AOD_DATA\Finished.csv')
    sati_AOD
    dict={'ground':ground_Aqi(ground_data,location_entered),'satalite':sati_AOD(sat,location_entered),'Longitude':actual_location.longitude,'Latitude':actual_location.latitude}
    print(dict)
    print(dict['ground'])

generator()
    

        

    

