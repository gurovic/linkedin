import {Component} from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import {Router} from '@angular/router';
import {
  FormControl,
  FormGroup,
  FormsModule,
  ReactiveFormsModule
} from '@angular/forms';
import {CommonModule} from '@angular/common';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule, FormsModule],
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
  loginForm = new FormGroup({
    username: new FormControl(''),
    password: new FormControl('')
  });
  loginError: string | null = null;

  constructor(private http: HttpClient, private router: Router) {
  }

  onSubmit() {
    const username = this.loginForm.value.username;
    const password = this.loginForm.value.password;
    console.log(username, password)

    const headers = new HttpHeaders({
      'Authorization': 'Basic ' + btoa(username + ':' + password)
    });

    this.http.post(`http://localhost:8000/api/auth/login/`, JSON.stringify({}), {headers: headers}).subscribe(
      response => {
        console.log('Login successful', response);
        this.loginError = null;
        this.router.navigate(['/']);
      },
      error => {
        this.loginError = 'Invalid username or password';
        console.error('Login failed', error);
      }
    );
  }
}
