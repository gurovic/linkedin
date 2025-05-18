import { Component } from '@angular/core';
import { NgIf, NgOptimizedImage, AsyncPipe } from '@angular/common';
import { takeUntilDestroyed } from '@angular/core/rxjs-interop';

import { AboutSiteComponent } from '../about-site/about-site.component';
import { ValuesComponent } from '../values/values.component';
import { LoginComponent } from '../login/login.component';
import { SignupComponent } from '../sign-up/sign-up.component';
import { MapComponent } from '../map/map.component';
import { AuthService } from '../../services/auth.service';

@Component({
  selector: 'app-main-page',
  standalone: true,
  imports: [
    NgIf,
    NgOptimizedImage,
    AsyncPipe,
    AboutSiteComponent,
    ValuesComponent,
    LoginComponent,
    SignupComponent,
    MapComponent
  ],
  templateUrl: './main-page.component.html',
  styleUrls: ['./main-page.component.css']
})
export class MainPageComponent {
  showSignup = false;
  showLogin  = false;
  isAuthenticated = false;

  constructor(private readonly authService: AuthService) {
    this.authService.isLoggedIn$
      .pipe(takeUntilDestroyed())
      .subscribe(v => this.isAuthenticated = v);
  }
}
