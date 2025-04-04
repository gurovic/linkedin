import { Component, Input } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Router } from '@angular/router';

@Component({
  selector: 'app-company-card',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './company-card.component.html',
  styleUrl: './company-card.component.css'
})
export class CompanyCardComponent {
  @Input() company: any;

  constructor(private router: Router) {}

  navigateToCompany(): void {
    this.router.navigate(['/company', this.company.id]);
  }
}
