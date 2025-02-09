import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import {environment} from '../../environments/environment';

@Injectable({
  providedIn: 'root',
})
export class Event_List_Service {
  private baseUrl = environment.apiUrl + 'api/event';

  constructor(private http: HttpClient) {}

  getEvents(): Observable<any> {
    return this.http.get(this.baseUrl);
  }
}
