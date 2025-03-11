import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import {environment} from '../../environments/environment';

@Injectable({
  providedIn: 'root',
})
export class EventService {
  private baseUrlEventDetails = environment.apiUrl + 'api/event/';
  private baseUrlEventList = environment.apiUrl + 'api/event_list_last/';

  constructor(private http: HttpClient) {}

  getEventDetails(eventId: number): Observable<any> {
    return this.http.get(`${this.baseUrlEventDetails}${eventId}/`);
  }

  getLastEvents(): Observable<any> {
    return this.http.get(this.baseUrlEventList);
  }
}
