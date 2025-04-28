import { Component, Input } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Router } from '@angular/router';

@Component({
  selector: 'app-university-card',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './university-card.component.html',
  styleUrl: './university-card.component.css'
})
export class UniversityCardComponent {
  @Input() university: any;

  constructor(private router: Router) {}

  navigateToUniversity(): void {
    this.router.navigate(['/university', this.university.id]);
  }
}
