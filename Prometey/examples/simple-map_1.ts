import { Map as MapboxMap, Popup } from 'mapbox-gl';

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

const mapLoadedPr = new Promise(resolve => map.on('load', resolve));
/**
 * Indoor specific
 */

addIndoorTo(map);

// Retrieve the geojson from the path and add the map
const geojson = await (await fetch('http://31.129.105.164:3030/get_geojson/')).json();

map.indoor.addMap(IndoorMap.fromGeojson(geojson));
//map.indoor.addMap(IndoorMap.fromGeojson(geojson, { layers }));
// Add the specific control
map.addControl(new IndoorControl());

await mapLoadedPr;


const geojson_icon = await (await fetch('http://31.129.105.164:3030/get_geojson_icon/')).json();

for (let i = 0; i < geojson_icon["img"].length; i++) {
  let img = geojson_icon["img"][i];
  let image: ImageData = await new Promise(resolve => map.loadImage(
    './img/'+img, (_: string, image: ImageData) => resolve(image)));
  map.addImage(img, image);

}


const geojson_point = await (await fetch('http://31.129.105.164:3030/get_geojson_point/')).json();
for (let i = 0; i < geojson_point["data"].length; i++) {
    let point = geojson_point["data"][i];
    map.addSource(point.id, point.source);

    map.indoor.addLayerForFiltering({
        'id': point.id,
        'type': 'symbol',
        'source': point.id,

        'layout': {
            'icon-image': point.icon,
            'text-field': ['get', 'text'],
            'text-offset': [0, 1.25],

        }
    });

    map.on('click', point.id, (e) => {

        const { geometry, properties } = e.features![0];
        const coordinates = (geometry as Point).coordinates.slice();
        const description = properties?.name + ' (level: ' + properties?.level + ')';
        //let elem = document.querySelector<HTMLDivElement>('.panarams')!
        
        //elem.style.display = 'block';

        //console.log(elem);
        new Popup()
            .setLngLat(coordinates as [number, number])
            .setHTML(description)
            .addTo(map);

        
    });

    map.on('mouseenter', point.id, () => {
        map.getCanvas().style.cursor = 'pointer';
    });

    map.on('mouseleave', point.id, () => {
        map.getCanvas().style.cursor = '';
    });



}




