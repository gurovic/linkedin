import { Component, Input } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Router } from '@angular/router';

@Component({
  selector: 'app-vacancy-card',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './vacancy-card.component.html',
  styleUrl: './vacancy-card.component.css'
})
export class VacancyCardComponent {
  @Input() vacancy: any;

  constructor(private router: Router) {}

  navigateToVacancy(): void {
    this.router.navigate(['/vacancy', this.vacancy.id]);
  }
}
