from django.shortcuts import render
from django.http import JsonResponse
import json
import networkx as nx

# Opening JSON file

# Create your views here.
def getjson_arrow(requests):
	data_arrow = {
		"type": "FeatureCollection", 
		"features": [

		]
	}
	f = open('arrow_1.geojson')
	data = json.load(f)
	data = data["features"]
	data_arrow["features"].append(data[0])
	data_arrow["features"].append(data[1])
	data_arrow["features"].append(data[2])
	data_arrow["features"].append(data[3])
	#data_arrow["features"].append(data[4])
	return JsonResponse(data_arrow)