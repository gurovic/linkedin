import { Component, OnInit } from '@angular/core';
import { VacancyCardComponent } from '../vacancy-card/vacancy-card.component';
import { CommonModule } from '@angular/common';
import { environment } from '../../../environments/environment';
import { VacanciesService } from '../../services/vacancies.service';

@Component({
  selector: 'app-vacancy-gallery',
  standalone: true,
  imports: [VacancyCardComponent, CommonModule],
  templateUrl: './vacancy-gallery.component.html',
  styleUrl: './vacancy-gallery.component.css'
})
export class VacancyGalleryComponent implements OnInit{
  vacancies: any[] = [];
  env = environment;

  constructor(private VacanciesService: VacanciesService) {}

  ngOnInit(): void {
    this.VacanciesService.getVacancies().subscribe(
      (data) => {
        this.vacancies = data;
      },
      (error) => {
        console.error('Error fetching events:', error);
      }
    );
  }
}
