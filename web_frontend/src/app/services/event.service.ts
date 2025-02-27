import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import {environment} from '../../environments/environment';

@Injectable({
  providedIn: 'root',
})
export class EventService {
  private baseUrl = environment.apiUrl + 'api/event/';

  constructor(private http: HttpClient) {}

  getEventDetails(eventId: number): Observable<any> {
    return this.http.get(`${this.baseUrl}${eventId}/`);
  }
}
