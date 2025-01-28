import { Component } from '@angular/core';
import { FooterComponent } from '../footer/footer.component';
import { ValuesComponent } from '../values/values.component';
import { AboutSiteComponent } from '../about-site/about-site.component';

@Component({
  selector: 'app-main-page',
  standalone: true,
  imports: [FooterComponent, AboutSiteComponent, ValuesComponent],
  templateUrl: './main-page.component.html',
  styleUrl: './main-page.component.css'
})
export class MainPageComponent {

}
