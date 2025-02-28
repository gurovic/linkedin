import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { CompanyService } from '../../services/company.service';
import { CommonModule } from '@angular/common';

interface Worker {
  first_name: string;
  last_name: string;
}

@Component({
  selector: 'app-company',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './company.component.html',
  styleUrls: ['./company.component.css'],
  providers: [CompanyService]
})
export class CompanyComponent implements OnInit {
  company: any;
  companyId: string | null = null;

  constructor(private route: ActivatedRoute, private companyService: CompanyService) {}

  ngOnInit(): void {
    this.route.paramMap.subscribe(params => {
      this.companyId = params.get('id');
      if (this.companyId) {
        const id = Number(this.companyId); // Convert string to number
        if (!isNaN(id)) {
          this.getCompanyByID(id);
        } else {
          console.error('Invalid company ID:', this.companyId);
        }
      }
    });
  }

  getCompanyByID(id: number): void {
    this.companyService.getCompanyDetails(id).subscribe(
      (data) => {
        data.current_workers = data.current_workers.map((worker: Worker) => ({
          ...worker,
          full_name: `${worker.last_name} ${worker.first_name}`
        }));
        this.company = data;
      },
      (error) => {
        console.error('Error fetching company details:', error);
      }
    );
  }
}
