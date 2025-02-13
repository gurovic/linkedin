import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import {environment} from '../../environments/environment';

@Injectable({
  providedIn: 'root',
})
export class CompanyService {
  private baseUrl = environment.apiUrl + 'api/company/';

  constructor(private http: HttpClient) {}

  getCompanyDetails(companyId: number): Observable<any> {
    return this.http.get(`${this.baseUrl}${companyId}/`);
  }
}
