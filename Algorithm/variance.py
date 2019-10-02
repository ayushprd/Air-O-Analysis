#Assuming indexing starts from 0

'''

Imagine a graph and you have points scattered all over. What this program does is it removes 
all the extreme points from the graph and gives us a cluster 
of points that fit our definition. Our definition in this case is the standard_Value. 
The above mentioned variable acts as a means of measurement 
as how precise we want our data to be or in terms of the graph how close our points should be. 
Now coming to our problem imagine the Air Quality Index(AQI) are 
points on a graph and the extreme values are values that we exclued and are deemed incorrect. 
The elimanation of these incorrect values is the main logic behind this algo.
We are considering values that have similar reading correct reading while discarding the values that deter away from these values. 
Why cause we believe in DEMOCRACY! 

In the code below first it finds the deviation as deviation gives us an estimate of how spread our data is
If the value is low that means our data is similar(clustered in terms of graph) and then we can use mean to calculate 
the best value. We use mean because in a cluster of data that have similar values mean gives us a best estimate 
to represent the data. And now after calculating the mean it check which value is closest to the mean and 
labels that as our most_Accurate_value

Below a part of code is labelled 2.
From that point on below what is does is it keeps eliminating the worst values one by one by finding the 
least deviation. E.g say we have sample=[10,60,70,500,68] obvioulsy 500 is the incorrect data thus what the program does is
checks deviation for each set like : [10.60,70,500] [10,60,70,68] [10,60,500,68] [60,70,500,68] and obviously the second
second set has the least deviation and thus our new sample = [10,60,70,68] now if the new sample has deviation less than 
our defintion then it stops and calculates and mean and finds the most_Accurate_value otherwise it continues the process of
elimination.

For better understanding copy paste the following test cases :
Data={"a":100,"B":200,"V":300,"F":400,"g":500} 
Data={"a":10,"B":60,"V":70,"F":500,"g":68} 
Data={"a":5,"B":7,"V":7,"F":8,"g":9} 
'''


import statistics

standard_Value=10; # this is our standard value lowering it means closer points to a graph and vice versa 
Data={"a":10,"B":60,"V":70,"F":500,"g":68} # Sample data you may input ur own data and check it
sample = [Data[key] for key in Data] #Converts the data into a array or list 
temp=[]
index=0
sample_new=sample
minimum_Deviation=0
length=len(sample)
mean= statistics.mean(sample) 
standard_Deviation=statistics.stdev(sample)
most_Accurate_Value=sample[0]
val=abs(sample[0]-mean)
print("Current Sample : ",sample)

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
        print("Data elimanated -",sample[index])        
        sample=sample_new 
        print("Current Sample : ",sample)
        if(len(sample)==2):
            print("We cant decrease our sample any more so we take the above sample and calculate mean")
            break  
        elif(standard_Deviation<=standard_Value):
            print("The given sample fits our definition so no need for further elimination ")
            break
    mean=statistics.mean(sample)
    length=len(sample)
    for i in range(length):
        if((abs(sample[i]-mean))<=most_Accurate_Value):
            val=abs(sample[i]-mean)
            most_Accurate_Value=sample[i]

print("Mean :",mean," Most Accurate Value :",most_Accurate_Value)

#The second part

    





