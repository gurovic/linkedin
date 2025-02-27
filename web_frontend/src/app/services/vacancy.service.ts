import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class VacancyService {
  private apiUrl = 'http://localhost:8000/api/vacancy/'; // URL API

  constructor(private http: HttpClient) {}

  // Получение одной вакансии по ID
  getVacancy(id: number): Observable<any> {
    return this.http.get(`${this.apiUrl}${id}/`);
  }
}
