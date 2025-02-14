import { Component } from '@angular/core';
import { NgIf } from '@angular/common';
import { ValuesComponent } from '../values/values.component';
import { AboutSiteComponent } from '../about-site/about-site.component';
import { LoginComponent } from '../login/login.component';
import {MapComponent} from '../map/map.component';
import {FooterComponent} from '../footer/footer.component';

@Component({
  selector: 'app-main-page',
  standalone: true,
  imports: [FooterComponent, AboutSiteComponent, ValuesComponent, LoginComponent, NgIf, MapComponent],
  templateUrl: './main-page.component.html',
  styleUrl: './main-page.component.css'
})
export class MainPageComponent {
  showLogin = false;
}
