import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from '../../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class VacanciesService {
  private baseUrl = environment.apiUrl + 'api/vacancys';

  constructor(private http: HttpClient) { }

  getVacancies(): Observable<any> {
    return this.http.get(this.baseUrl);
  }
}
