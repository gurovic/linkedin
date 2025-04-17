import { Component } from '@angular/core';
import { NgIf } from '@angular/common';
import { ValuesComponent } from '../values/values.component';
import { AboutSiteComponent } from '../about-site/about-site.component';
import { LoginComponent } from '../login/login.component';
import { MapComponent } from '../map/map.component';
import { SignupComponent } from '../sign-up/sign-up.component';
import { AuthService } from '../../services/auth.service';

@Component({
  selector: 'app-main-page',
  standalone: true,
  imports: [
    AboutSiteComponent,
    ValuesComponent,
    LoginComponent,
    NgIf,
    MapComponent,
    SignupComponent
  ],
  templateUrl: './main-page.component.html',
  styleUrl: './main-page.component.css'
})
export class MainPageComponent {
  showLogin = false;
  showSignup = false;
  isAuthenticated: boolean;

  constructor(private authService: AuthService) {
    this.isAuthenticated = this.authService.isLoggedIn();
  }
}