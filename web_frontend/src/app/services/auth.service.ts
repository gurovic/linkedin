import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';
import { HttpClient } from '@angular/common/http';
import { environment } from '../../environments/environment';

export interface UserInfo {
  id: number;
  username: string;
  first_name: string;
  last_name: string;
  is_staff: boolean;
}

@Injectable({ providedIn: 'root' })
export class AuthService {
  private loggedIn$ = new BehaviorSubject<boolean>(this.hasToken());
  private userInfo$ = new BehaviorSubject<UserInfo | null>(null);

  constructor(private http: HttpClient) {
    if (this.hasToken()) {
      this.fetchUserInfo();
    }
  }

  get isLoggedIn$() {
    return this.loggedIn$.asObservable();
  }

  get currentUser$() {
    return this.userInfo$.asObservable();
  }

  currentUserId(): number | null {
    return this.userInfo$.value?.id ?? null;
  }

  isLoggedInSync(): boolean {
    return this.loggedIn$.value;
  }

  isAdmin(): boolean {
    return this.userInfo$.value?.is_staff ?? false;
  }

  getToken(): string | null {
    return localStorage.getItem('authToken');
  }

  login(token: string): void {
    localStorage.setItem('authToken', token);
    this.loggedIn$.next(true);
    this.fetchUserInfo();
  }

  logout(): void {
    localStorage.removeItem('authToken');
    this.loggedIn$.next(false);
    this.userInfo$.next(null);
  }

  private hasToken(): boolean {
    return !!localStorage.getItem('authToken');
  }

  private fetchUserInfo(): void {
    this.http
      .get<UserInfo>(`${environment.apiUrl}api/auth/check/`)
      .subscribe({
        next: user => {
          this.userInfo$.next(user);
          this.loggedIn$.next(true);
        },
        error: err => {
          if (err.status === 401 || err.status === 403) {
            this.logout();
          } else {
            console.error('auth/check failed:', err);
          }
        }
      });
  }
}
