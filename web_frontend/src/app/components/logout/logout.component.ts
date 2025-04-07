import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import {CommonModule} from '@angular/common';
import {environment} from '../../../environments/environment';
import { HttpClient } from '@angular/common/http';
import { AuthService } from '../../services/auth.service';

@Component({
  selector: 'app-event-detail',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './logout.component.html'
})
export class LogoutComponent implements OnInit {
  event: any = null;
  env = environment;
  
  constructor(private http: HttpClient, private router: Router, private authService: AuthService) {
  }

  ngOnInit(): void {
    this.authService.logout();
    this.router.navigate(['/']);
  }
}
