import { Component } from '@angular/core';
import { NgIf, NgFor } from '@angular/common';
import { ValuesComponent } from '../values/values.component';
import { AboutSiteComponent } from '../about-site/about-site.component';
import { LoginComponent } from '../login/login.component';
import { MapComponent } from '../map/map.component';
import {FooterComponent} from '../footer/footer.component';


@Component({
  selector: 'app-main-page',
  standalone: true,
  imports: [AboutSiteComponent, ValuesComponent, LoginComponent, NgIf, NgFor, MapComponent, FooterComponent],
  templateUrl: './main-page.component.html',
  styleUrl: './main-page.component.css'
})
export class MainPageComponent {
  showLogin = false;
  isAuthenticated = false;
  //Моки
  users = [
    { username: 'Екатерина' },
    { username: 'Павел' },
    { username: 'Виктория' }
  ];

  // Пример списка компаний
  companies = [
    {
      name: 'Летово.Джуниор',
      description: 'Образовательная компания',
      country: 'Россия',
      vacancies: [
        { name: 'Разработчик', specialization: 'Frontend', description: 'Работа с Angular' }
      ],
      workers: [{ username: 'Павел' }]
    },
    {
      name: 'Русагро',
      description: 'Агрохолдинг',
      country: 'Россия',
      vacancies: [],
      workers: [{ username: 'Виктория' }]
    }
  ];
}

