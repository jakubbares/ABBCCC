
import {throwError as observableThrowError,  Observable } from 'rxjs';
import { Injectable } from '@angular/core';
import {Http, Headers, Response, RequestOptions} from '@angular/http';

import * as _ from 'lodash';

import {environment} from '../../environments/environment';

import {HttpClient, HttpHeaders} from '@angular/common/http';


@Injectable()
export class AuthenticationService {
  private baseUrl = `${environment.apiUrl}/auth`;
  constructor(
    private http: HttpClient) {
  }

  public isLoggedIn() {
    return !!localStorage.getItem('currentUser');
  }

  getUsers(): Observable<any> {
    return this.http.get(this.baseUrl + '/users')
  }


  login(email: string, password: string) {
    const body = JSON.stringify({
      'data': {
        email: email,
        password: password
      }
    });
    const headers = new HttpHeaders({'Content-Type': 'application/json'});
    const options = {headers: headers};
    return this.http.post(this.baseUrl, body, options);
  }

  postUser(user: any): Observable<any> {
    const headers = new HttpHeaders({ 'Content-Type': 'application/json' });
    const options = { headers: headers };
    return this.http.post(this.baseUrl + '/user', JSON.stringify({ 'data': {"type": "data", "attributes": { user }}}), options)
  }

  patchUser(user: any, id: number): Observable<any> {
    const headers = new HttpHeaders({ 'Content-Type': 'application/json' });
    const options = { headers: headers };
    return this.http.patch(this.baseUrl + '/user/' + id, JSON.stringify({ 'data': {"type": "data", "attributes": { user }}}), options)
  }

  checkEmailExists(email: string) {
    return this.http.get(this.baseUrl + '/check/' + email)
  }

  logout() {
    // remove user from API storage to log user out
    localStorage.removeItem('currentUser');
  }

}
