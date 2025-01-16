import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class EventService {
  private baseUrl = 'http://127.0.0.1:8000/api/event/'; // API base URL

  constructor(private http: HttpClient) {}

  // Fetch event details by ID
  getEventDetails(eventId: number): Observable<any> {
    return this.http.get(`${this.baseUrl}${eventId}/`);
  }
}