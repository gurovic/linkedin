import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders  } from '@angular/common/http';
import { Observable } from 'rxjs';
import {environment} from '../../environments/environment';

@Injectable({
  providedIn: 'root'
})

export class SearchUserService {
  private baseUrl = environment.apiUrl + 'api/user_search';

  constructor(private http: HttpClient) { }

  RequestUserSearch(payload: any): Observable<any>{
    const headers = new HttpHeaders({
      'Content-Type': 'application/json'
    });
    
    return this.http.post<any>(this.baseUrl, payload, { headers });
  }
}
