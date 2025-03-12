import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import {environment} from '../../environments/environment';

@Injectable({
  providedIn: 'root',
})
export class Company_List_Service {
  private baseUrl = environment.apiUrl + 'api/company';

  constructor(private http: HttpClient) {}

  getCompanies(): Observable<any> {
    return this.http.get(this.baseUrl);
  }
}
