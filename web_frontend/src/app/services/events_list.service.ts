import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class Event_List_Service {
  private baseUrl = 'http://127.0.0.1:8000/api/event_list/'; // API base URL

  constructor(private http: HttpClient) {}

  // Fetch the list of events
  getEvents(): Observable<any> {
    return this.http.get(this.baseUrl);
  }
}