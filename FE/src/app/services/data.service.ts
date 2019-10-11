import {throwError as observableThrowError,  Observable } from 'rxjs';
import {Injectable, OnInit} from '@angular/core';
import {environment} from '../../environments/environment';
import {capitalizeField, sortByField, transformData} from '../shared/shared.functions';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import * as points from '../../assets/points.json';



@Injectable()
export class DataService implements OnInit {
  private baseUrl = `${environment.apiUrl}/charts`;
  radarData: any;
  spiderData: any;
  constructor(
    private http: HttpClient
  ) {
  }
  ngOnInit() {
  }

  loadPoints() {
    console.log(points)
    return points;
  }

  getRadarStatsForPlayer(player_instatid: number, season: string) {
    const headers = new HttpHeaders({ 'Content-Type': 'application/json' });
    const options = { headers: headers }
    return this.http.post(this.baseUrl + '/radar', JSON.stringify({ 'data': {player_instatid, season }}), options)
  }

  getChancesJSONForMatch(match_instatid: number) {
    return this.http.get(this.baseUrl + '/chances/match/' + match_instatid)
  }

  getShotsJSONForTeamLeagueAndSeason(team_instatid: number, league_instatid: number, season: string) {
    return this.http.get(this.baseUrl + '/shots/team/' + team_instatid + '/league/' + league_instatid + '/season/' + season)
  }


  getShotsForTeamLeagueAndSeason(team_instatid: number, league_instatid: number, season: string, callback) {
    this.getShotsJSONForTeamLeagueAndSeason(team_instatid, league_instatid, season).subscribe((t: any) => {
      if (t.data) {
        const data = this.extractShotsSeasonTeamFromJSON(t.data);
        callback(data);
      }
    })
  }

  extractShotsSeasonTeamFromJSON(data) {
    console.log(data)
    data['items'] = data['shots'].map(item => {
      return {
        player_instatid: item[0],
        player_name: item[1],
        result: item[2],
        type: item[3],
        x: item[4],
        y: item[5],
        xG: item[6],
        time: item[7]
      }
    });
    return data;
  }


  getHeatMap(type, match_instatid, team_instatid, callback) {
    callback({}, {})
  }
}
