import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class AccountService {

  // Replace with the actual API URL of your Django backend
  private apiUrl = 'http://your-backend-url.com/api/account/';

  constructor(private http: HttpClient) { }

  // Method to fetch the account details of a user
  getAccountDetails(userId: number): Observable<any> {
    return this.http.get(`${this.apiUrl}${userId}/`);
  }
}