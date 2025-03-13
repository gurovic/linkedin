import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { environment } from '../../../environments/environment';
import { Company_List_Service } from '../../services/company_list.service';
import { CompanyCardComponent } from '../company-card/company-card.component';

@Component({
  selector: 'app-company-gallery',
  standalone: true,
  imports: [CompanyCardComponent, CommonModule],
  templateUrl: './company-gallery.component.html',
  styleUrl: './company-gallery.component.css'
})
export class CompanyGalleryComponent implements OnInit{
  companies: any[] = [];
  env = environment;

  constructor(private CompaniesService: Company_List_Service) {}

  ngOnInit(): void {
    this.CompaniesService.getCompanies().subscribe(
      (data) => {
        this.companies = data;
      },
      (error) => {
        console.error('Error fetching events:', error);
      }
    );
  }
}
