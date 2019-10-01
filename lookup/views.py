from django.shortcuts import render
import json
import requests
# Create your views here.
def home(request):

    api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=25&API_KEY=80255E1C-5395-4191-8F32-BE148707DBE0")

    try:
        api = json.loads(api_request.content)
    except Exception as e:
        api = "Error"

    return render(request, 'home.html', {'api':api})

def about(request):
    return render(request, 'about.html', {})