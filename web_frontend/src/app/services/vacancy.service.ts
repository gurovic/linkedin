import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import {environment} from '../../environments/environment';

@Injectable({
  providedIn: 'root',
})
export class VacancyService {
  private baseUrl = environment.apiUrl + 'api/vacancy/';

  constructor(private http: HttpClient) {}

  getVacancyDetails(vacancy_id: number): Observable<any> {
    return this.http.get(`${this.baseUrl}${vacancy_id}/`);
  }
}
