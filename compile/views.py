from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.contrib import auth
from compiler.main import run


@csrf_exempt
def index(request):
    if request.method == "POST":
        code = request.POST['code']
        mipscode = run(code, "completemips" in request.POST)

        return render(request, 'mipscode.html', {"mipscode": mipscode, "decafcode": code})
