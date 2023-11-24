from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import JsonResponse
import json

from .forms import CustomUserCreationForm
from .models import *


def getjson_arrow(requests, path):
    data_arrow = {
        "type": "FeatureCollection",
        "features": [

        ]
    }
    f = open('arrow_1.geojson')
    data = json.load(f)
    data = data["features"]
    
    if path == 1:
        data_arrow["features"].append(data[14])
    elif path == 2:
        data_arrow["features"].append(data[15])
    elif path == 3:
        data_arrow["features"].append(data[16])
        data_arrow["features"].append(data[17])

    return JsonResponse(data_arrow)


def get_geojson(requests):
    data = {
        "type": "FeatureCollection",
        "features": []
    }
    items = MapRooms.objects.all()
    for item in items:
        data["features"].append({
              "type": "Feature",
              "id": str(item.id),
              "properties": {
                "@id": str(item.id)+"_id",
                "clothes": "children",
                "fill": "#3b86c9",
                "fill-opacity": "1",
                "indoor": "room",
                "level": str(item.level),
                "name": item.name,
                "stroke": "#000314",
                "stroke-opacity": "1",
                "stroke-width": "0.5",
                "id": str(item.id)
              },
              "geometry": {
                "type": "Polygon",
                "coordinates": [
                    item.coordinates_json
                ]
              }
            })


    return JsonResponse(data)

def get_geojson_icon(requests):
    items = MapIcons.objects.all()
    res = []
    for item in items:
        res.append(item.file_name)

    return JsonResponse({'img': res})

def get_geojson_point(requests):
    items = MapPoint.objects.all()
    data = {"data": []}

    for item in items:
        data["data"].append({
            "icon": item.icon.file_name,
            "id": str(item.id)+"_point_id",
            "source": {
                    'type': 'geojson',
                    'data': {
                        'type': 'FeatureCollection',
                        'features': [
                            {
                                'type': 'Feature',
                                'geometry': {
                                    'type': 'Point',
                                    'coordinates': item.coordinates_json
                                },
                                'properties': {
                                    'level': str(item.level),
                                    'name': item.name,
                                    'text': item.text
                                }
                            }
                        ]
                    }
                }
            })

    return JsonResponse(data)


@login_required(login_url='login')
def index(request):
    context = {
        'sensors': len(Sensor.objects.all()),
        'employs': len(CustomUser.objects.all()),
    }
    return render(request, 'KAMEN.html', context=context)


@login_required(login_url='login')
def zavod(request):
    context = {}
    num_path = request.GET.get("path")
    if num_path != None:
        context["num_path"] = num_path
        return render(request, 'zavod.html', context=context)
    return render(request, 'zavod_1.html', context=context)


@login_required(login_url='login')
def sensors(request):
    context = {
        'sensors': Sensor.objects.all(),
    }
    return render(request, 'Sensors.html', context=context)


@login_required(login_url='login')
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


@login_required(login_url='login')
def alitic(request):
    return render(request, 'alitic.html')


@login_required(login_url='login')
def employs(request):
    context = {
        'employs': CustomUser.objects.all(),
    }
    return render(request, 'Reestr.html', context=context)


@login_required(login_url='login')
def employ_view(request, pk):
    context = {
        'employ': CustomUser.objects.get(pk=pk),
    }
    return render(request, 'Sotrudnik.html', context=context)


@login_required(login_url='login')
def oborudovanie(request):
    context = {
        'oborudovanie': Equipment.objects.all(),
    }
    return render(request, 'Oborudovanie.html', context=context)


@login_required(login_url='login')
def ind(request):
    return redirect('zavod')


