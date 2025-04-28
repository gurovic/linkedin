import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from '../../environments/environment';

@Injectable({
  providedIn: 'root',
})
export class UniversityService {
  private baseUrl = environment.apiUrl + 'api/university/';

  constructor(private http: HttpClient) {}

  getUniversityDetails(university_id: number): Observable<any> {
    return this.http.get(`${this.baseUrl}${university_id}`);
  }
}
