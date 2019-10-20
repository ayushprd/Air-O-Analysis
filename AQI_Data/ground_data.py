import requests
import urllib.request

location = 'Delhi' #the first letter of the location has to be capitalised

url = ('https://api.openaq.org/v1/measurements?city={0}'.format(location))

urllib.request.urlretrieve(url, 'C:\cpp\Python\Create.csv') #the system path where the csv would be saved
