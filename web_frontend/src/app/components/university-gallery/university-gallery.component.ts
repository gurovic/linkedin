import { Component, OnInit } from '@angular/core';
import { UniversityCardComponent } from '../university-card/university-card.component';
import { CommonModule } from '@angular/common';
import { environment } from '../../../environments/environment';
import { UniversitiesService } from '../../services/universities.service';

@Component({
  selector: 'app-university-gallery',
  standalone: true,
  imports: [UniversityCardComponent, CommonModule],
  templateUrl: './university-gallery.component.html',
  styleUrl: './university-gallery.component.css'
})
export class UniversityGalleryComponent implements OnInit{
  universities: any[] = [];
  env = environment;

  constructor(private UniversitiesService: UniversitiesService) {}

  ngOnInit(): void {
    this.UniversitiesService.getUniversities().subscribe(
      (data) => {
        this.universities = data;
      },
      (error) => {
        console.error('Error fetching universities:', error);
      }
    );
  }
}
