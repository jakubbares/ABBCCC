import {Component, OnInit, OnChanges, Input} from '@angular/core';
declare let L;
import '../../../node_modules/leaflet-routing-machine/dist/leaflet-routing-machine.js'
import '../../dist/leaflet-heat.js'



@Component({
	selector: 'map',
	template: `
    <div id="map"></div>`,
	styleUrls: ['./map.component.css']
})
export class MapComponent implements OnInit, OnChanges {

  @Input points: any[];
  map: any;
  heat: any;

	ngOnChanges() {
    console.log(this.points);
    const { CentrLatitude, CentrLongitude } = this.points[0];
    this.map.setView([CentrLatitude, CentrLongitude], 13);
  }

	ngOnInit() {
		this.map = L.map('map').setView([51.505, -0.09], 13);

		L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
			attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
		}).addTo(this.map);

    this.heat = L.heatLayer([
      [51.505, -0.09, 700], // lat, lng, intensity
      [51.505, -1.09, 250],
    ], {radius: 10}).addTo(this.map);

	}

}
