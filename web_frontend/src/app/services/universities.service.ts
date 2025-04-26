import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from '../../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class UniversitiesService {
  private baseUrl = environment.apiUrl + 'api/universities/';

  constructor(private http: HttpClient) { }

  getUniversities(): Observable<any> {
    return this.http.get(this.baseUrl);
  }
}
