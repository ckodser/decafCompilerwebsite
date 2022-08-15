from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    print('8')
    return render(request, "home.html",{"text": "", "options": [""]*5, "search": "boolean"})

def favicon(request):
    image_data = open("static/favicon.ico", "rb").read()
    return HttpResponse(image_data, content_type="image/x-icon")