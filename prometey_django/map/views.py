from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.http import JsonResponse
import json

from .forms import CustomUserCreationForm
from .models import *


def getjson_arrow(requests):
    data_arrow = {
        "type": "FeatureCollection",
        "features": [

        ]
    }
    f = open('arrow_1.geojson')
    data = json.load(f)
    data = data["features"]
    """
    #data_arrow["features"].append(data[0])
    data_arrow["features"].append(data[1])
    #data_arrow["features"].append(data[2])
    data_arrow["features"].append(data[3])
    #data_arrow["features"].append(data[4])
    #data_arrow["features"].append(data[5])
    #data_arrow["features"].append(data[6])
    #data_arrow["features"].append(data[7])
    data_arrow["features"].append(data[8])
    #data_arrow["features"].append(data[9])
    #data_arrow["features"].append(data[10])
    #data_arrow["features"].append(data[11])
    #data_arrow["features"].append(data[12])
    #data_arrow["features"].append(data[13])
    """
    return JsonResponse(data_arrow)


def index(request):
    context = {
        'sensors': len(Sensor.objects.all()),
        'employs': len(CustomUser.objects.all()),
    }
    return render(request, 'KAMEN.html', context=context)


def zavod(request):
    return render(request, 'zavod.html')


def sensors(request):
    context = {
        'sensors': Sensor.objects.all(),
    }
    return render(request, 'Sensors.html', context=context)


def department(request):
    context = {
        'departments': Department.objects.all(),
    }
    return render(request, 'department.html', context=context)


def log_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('zavod')  # Замените 'home' на URL вашей домашней страницы
        else:
            pass
    return render(request, 'index.html')


def register_view(request):
    if request.method == 'POST':
        if request.POST['password']:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('zavod')  # Замените 'home' на URL вашей домашней страницы
        else:
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                username = request.POST['username']
                password = request.POST['password1']
                user = authenticate(request, username=username, password=password)
                login(request, user)
                return redirect('zavod')
    else:
        form = CustomUserCreationForm()
    return render(request, 'index.html', {'form': form})


def alitic(request):
    return render(request, 'alitic.html')


def employs(request):
    context = {
        'employs': CustomUser.objects.all(),
    }
    return render(request, 'Reestr.html', context=context)


def employ_view(request, pk):
    context = {
        'employ': CustomUser.objects.get(pk=pk),
    }
    return render(request, 'Sotrudnik.html', context=context)


def oborudovanie(request):
    context = {
        'oborudovanie': Equipment.objects.all(),
    }
    return render(request, 'Oborudovanie.html', context=context)


def ind(request):
    return redirect('zavod')
