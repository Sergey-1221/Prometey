import { Map as MapboxMap, Popup } from 'mapbox-gl';

import accessToken from './mapbox-access-token';
import { addIndoorTo, IndoorControl, IndoorMap, MapboxMapWithIndoor } from '../src/index';

import 'mapbox-gl/dist/mapbox-gl.css';
import './style.css';
import { Point } from 'geojson';

const app = document.querySelector<HTMLDivElement>('#app')!

const map = new MapboxMap({
    container: app,
    zoom: 18,
    center: [37.747424, 55.742387],
    style: 'mapbox://styles/mapbox/streets-v10',
    accessToken,
    hash: true
}) as MapboxMapWithIndoor;

const mapLoadedPr = new Promise(resolve => map.on('load', resolve));

/**
 * Indoor specific
 */

addIndoorTo(map);
const layers = [
    {
        "filter": [
            "filter-==",
            "indoor",
            "room"
        ],
        "id": "indoor-rooms",
        "type": "fill",
        "source": "indoor",
        "paint": {
            "fill-color": "#6d6d6d",
            "fill-opacity": 0.9
        }
    },
    {
        "filter": [
            "filter-==",
            "indoor",
            "area"
        ],
        "id": "indoor-areas",
        "type": "fill",
        "source": "indoor",
        "paint": {
            "fill-color": "#FFFFFF",
            "fill-opacity": 0.5
        }
    },
    {
        "filter": [
            "filter-==",
            "indoor",
            "room-sp"
        ],
        "id": "indoor-room-sp",
        "type": "fill",
        "source": "indoor",
        "paint": {
            "fill-color": "#48ff00",
            "fill-opacity": 1
        }
    },
    {
        "filter": [
            "filter-==",
            "indoor",
            "arrow"
        ],
        "id": "indoor-arrows",
        "type": "line",
        "source": "indoor",
        "paint": {
            "line-color": "#ff0000",
            "line-width": 2

        }
    }
    
]

// Retrieve the geojson from the path and add the map
const geojson = await (await fetch('maps/zavod.geojson')).json();
const num_path = new URLSearchParams(window.location.search).get("path");
if (num_path != ""){
    const geojson_arrow = await (await fetch('http://127.0.0.1:3030/get_arrow/'+num_path)).json();
    geojson["features"] = geojson["features"].concat(geojson_arrow["features"])
}



map.indoor.addMap(IndoorMap.fromGeojson(geojson, { layers }));
// Add the specific control
map.addControl(new IndoorControl());

await mapLoadedPr;

const image: ImageData = await new Promise(resolve => map.loadImage(
    './img/red-marker.png', (_: string, image: ImageData) => resolve(image)));
map.addImage('poi', image);

map.addSource('pois', {
    type: 'geojson',
    data: {
        type: 'FeatureCollection',
        features: [
            {
                type: 'Feature',
                geometry: {
                    type: 'Point',
                    coordinates: [37.747424, 55.742387],
                },
                properties: {
                    level: '1',
                    name: 'Paul'
                }
            },
            {
                type: 'Feature',
                geometry: {
                    type: 'Point',
                    coordinates: [37.747424, 55.742387],
                },
                properties: {
                    level: '2',
                    name: 'Relay'
                }
            }
        ]
    }
});

map.indoor.addLayerForFiltering({
    'id': 'pois',
    'type': 'symbol',
    'source': 'pois',
    'layout': {
        'icon-image': 'poi'
    }
});

map.on('click', 'pois', (e) => {

    const { geometry, properties } = e.features![0];
    const coordinates = (geometry as Point).coordinates.slice();
    const description = properties?.name + ' (level: ' + properties?.level + ')<a onclick="clear_arrow()">Тык</a>';

    new Popup()
        .setLngLat(coordinates as [number, number])
        .setHTML(description)
        .addTo(map);

    clear_arrow();
});

map.on('mouseenter', 'pois', () => {
    map.getCanvas().style.cursor = 'pointer';
});

map.on('mouseleave', 'pois', () => {
    map.getCanvas().style.cursor = '';
});

function clear_arrow(){
    
    fetch('maps/arrow.geojson').then((response) => response.json())
    .then((data) => {
        //map.indoor.addMap(IndoorMap.fromGeojson(data, { layers }));
        map.on('load', () => map.addSource('arrow', data));
    });
    //
    
}

//function create_
/*
response => {
            
        }
*/
