from django.shortcuts import render
import json
import requests
# Create your views here.
def home(request):

    if request.method == "POST":
        zipcode = request.POST['zipcode']
        api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zipcode + "&distance=5&API_KEY=96A38DFD-5C56-4740-AD99-E38C0C855A1B")

        try:
            api = json.loads(api_request.content)
        except Exception as e:
             api = "Error"
    

        return render(request, 'home.html', {'api':api})

    else:
        api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=96A38DFD-5C56-4740-AD99-E38C0C855A1B")


        try:
            api = json.loads(api_request.content)
        except Exception as e:
             api = "Error"
        return render(request, 'home.html', {'api':api})

    


def about(request):
    return render(request, 'about.html', {})

import random

def about(request):
    num= random.randint(1,100)
    context= {
        'num': num,
        }
    return render(request, 'about.html', context)