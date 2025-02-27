import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { VacancyService } from '../../services/vacancy.service';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';

@Component({
  selector: 'app-vacancy',
  standalone: true,
  imports: [CommonModule, RouterModule],
  templateUrl: './vacancy.component.html',
  styleUrl: './vacancy.component.css', 
  providers: [VacancyService]
})
export class VacancyComponent implements OnInit {
  vacancy: any = null;
  vacancy_id: number | null = null;
  isLoading: boolean = true;
  errorMessage: string | null = null;

  constructor(private route: ActivatedRoute, private vacancyService: VacancyService) {}

  ngOnInit(): void {
    this.route.paramMap.subscribe(params => {
      const vacancyIdParam = params.get('vacancy_id');
      if (vacancyIdParam) {
        this.vacancy_id = Number(vacancyIdParam);
        if (!isNaN(this.vacancy_id)) {
          this.getVacancyByID(this.vacancy_id);
        } else {
          this.errorMessage = 'Invalid Vacancy ID';
        }
      }
    });
  }

  getVacancyByID(id: number): void {
    this.vacancyService.getVacancyDetails(id).subscribe(
      (data) => {
        this.vacancy = {
          ...data,
          companyName: data.company.name, 
          requiredMajors: data.required_majors || [],
          requiredLanguages: data.required_language || [],
        };
        this.isLoading = false;
      },
      (error) => {
        console.error('Error fetching vacancy details:', error);
        this.errorMessage = 'Failed to load vacancy details.';
        this.isLoading = false;
      }
    );
  }
}
