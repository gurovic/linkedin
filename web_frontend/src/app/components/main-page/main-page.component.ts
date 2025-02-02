import { Component } from '@angular/core';
import { NgIf } from '@angular/common';
import { FooterComponent } from '../footer/footer.component';
import { ValuesComponent } from '../values/values.component';
import { AboutSiteComponent } from '../about-site/about-site.component';
import { LoginComponent } from '../login/login.component';

@Component({
  selector: 'app-main-page',
  standalone: true,
  imports: [FooterComponent, AboutSiteComponent, ValuesComponent, LoginComponent, NgIf],
  templateUrl: './main-page.component.html',
  styleUrl: './main-page.component.css'
})
export class MainPageComponent {
  showLogin = false;
}
