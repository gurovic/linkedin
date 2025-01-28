import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import {environment} from '../../environments/environment';

@Injectable({
  providedIn: 'root',
})
export class Event_List_Service {
  private baseUrl = environment.apiUrl + 'api/event_list'; // API base URL

  constructor(private http: HttpClient) {}

  // Fetch the list of events
  getEvents(): Observable<any> {
    return this.http.get(this.baseUrl);
  }
}
