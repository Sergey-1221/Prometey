import { Map as MapboxMap } from 'mapbox-gl';

import accessToken from './mapbox-access-token';
import { addIndoorTo, IndoorControl, IndoorMap, MapboxMapWithIndoor } from '../src/index';

import 'mapbox-gl/dist/mapbox-gl.css';
import './style.css';

const app = document.querySelector<HTMLDivElement>('#app')!

const map = new MapboxMap({
    container: app,
    zoom: 18,
    center: [37.6365144, 55.7209155],
    style: 'mapbox://styles/mapbox/streets-v10',
    accessToken,
    hash: true
}) as MapboxMapWithIndoor;

/**
 * Indoor specific
 */
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
            "fill-opacity": 1,
            "symbol": "1123"
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

addIndoorTo(map);

// Retrieve the geojson from the path and add the map
const geojson = await (await fetch('maps/zvd.geojson')).json();

map.indoor.addMap(IndoorMap.fromGeojson(geojson));
//map.indoor.addMap(IndoorMap.fromGeojson(geojson, { layers }));
// Add the specific control
map.addControl(new IndoorControl());
