import {Component, OnInit, OnChanges} from '@angular/core';
declare let L;
import '../../node_modules/leaflet-routing-machine/dist/leaflet-routing-machine.js'
import '../dist/leaflet-heat.js'
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";


@Component({
	selector: 'app-root',
	template: `<map points="points"></map>`
})
export class AppComponent implements OnInit {

  points: any[] = [];
	constructor(private http: HttpClient) {
	}

	ngOnInit() {
    this.getJSON().subscribe(data => {
      this.points = data;
    });
  }

  public getJSON(): Observable<any> {
    return this.http.get("assets/points.json");
  }

}
