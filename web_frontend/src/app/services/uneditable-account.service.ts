import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class UserService {
  private baseUrl = 'http://127.0.0.1:8000/angular/account/'; // API base URL

  constructor(private http: HttpClient) {}

  // Fetch user details by user ID
  getUserDetails(userId: number): Observable<any> {
    return this.http.get(`${this.baseUrl}${userId}/`);
  }
}