#Converts a CSV file to list of dictionaries 
#To access elements based on keys stored the list index and then 
# simply print with the key as show below 
#dict=dict_list[0]
#print(dict['Year'])

import csv
import sys
import pprint
 
row = ['Year', ' Month', ' Date' ,'Latitude','longitude','AOD1','AOD2','STD3']

with open('C:\cpp\Python\AOD_DATA\Second.csv', 'r') as readFile:
    reader = csv.reader(readFile)
    lines = list(reader)
    lines[0] = row

with open('C:\cpp\Python\AOD_DATA\Second.csv', 'w') as writeFile:
    writer = csv.writer(writeFile)
    writer.writerows(lines)

readFile.close()
writeFile.close()
reader = csv.DictReader(open('C:\cpp\Python\AOD_DATA\Second.csv', 'r'))
dict_list = []
for line in reader:
    dict_list.append(line)
