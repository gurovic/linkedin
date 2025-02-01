import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from '../../environments/environment';

@Injectable({
  providedIn: 'root',
})
export class UserService {
  private baseUrl = environment.apiUrl + 'angular/account/';

  constructor(private http: HttpClient) {}

  // Fetch user details by user ID
  getUserDetails(userId: number): Observable<any> {
    return this.http.get(`${this.baseUrl}${userId}/`);
  }
}
