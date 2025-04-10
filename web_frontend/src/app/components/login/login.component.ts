import {
  Component,
  EventEmitter,
  Output,
  ViewContainerRef
} from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import {Router} from '@angular/router';
import {
  FormControl,
  FormGroup,
  FormsModule,
  ReactiveFormsModule
} from '@angular/forms';
import {CommonModule} from '@angular/common';
import {environment} from '../../../environments/environment';
import { AuthService } from '../../services/auth.service';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule, FormsModule],
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
  @Output() closeLoginPopup = new EventEmitter<void>();

  loginForm = new FormGroup({
    username: new FormControl(''),
    password: new FormControl('')
  });
  loginError: string | null = null;

  constructor(
    private http: HttpClient,
    private router: Router,
    private viewContainerRef: ViewContainerRef,
    private authService: AuthService
  ) {
  }

  onSubmit() {
    const username = this.loginForm.value.username;
    const password = this.loginForm.value.password;
    console.log(username, password)

    const headers = new HttpHeaders({
      'Authorization': 'Basic ' + btoa(username + ':' + password)
    });

    this.http.post(environment.apiUrl + `api/auth/login/`, JSON.stringify({}), {headers: headers}).subscribe(
      (response: any) => {
        console.log('Login successful', response);
        this.authService.login(response.token);
        this.loginError = null;
        localStorage.setItem('authToken', response.token);
        this.closeLoginPopup.emit();
        this.router.navigate(['/']).then(r => null);
      },
      error => {
        this.loginError = 'Invalid username or password';
        console.error('Login failed', error);
      }
    );
  }
}
