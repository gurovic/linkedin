import {Component, OnInit} from '@angular/core';
import {ActivatedRoute, RouterModule} from '@angular/router';
import {UniversityService} from '../../services/university.service';
import {CommonModule} from '@angular/common';

@Component({
  selector: 'app-university',
  standalone: true,
  imports: [CommonModule, RouterModule],
  templateUrl: './university.component.html',
  styleUrl: './university.component.css',
  providers: [UniversityService]
})
export class UniversityComponent implements OnInit {
  university: any = null;
  university_id: number | null = null;
  isLoading: boolean = true;
  errorMessage: string | null = null;

  constructor(private route: ActivatedRoute, private universityService: UniversityService) {
  }

  ngOnInit(): void {
    const universityIdParam = this.route.snapshot.params['id'];
    console.log(universityIdParam)
    if (universityIdParam) {
      this.university_id = Number(universityIdParam);
      if (!isNaN(this.university_id)) {
        this.getUniversityByID(this.university_id);
      } else {
        this.errorMessage = 'Invalid University ID';
      }
    }
  }

  getUniversityByID(id: number): void {
    this.universityService.getUniversityDetails(id).subscribe(
      (data) => {
        this.university = {
          ...data,
          UniversityName: data.name,
          UniversityDescription: data.description,
          UniversityLan: data.lat,
          UniversityLot: data.lon,
          UniversityPhoto: data.photo,
        };
        this.isLoading = false;
      },
      (error) => {
        console.error('Error fetching university details:', error);
        this.errorMessage = 'Failed to load university details.';
        this.isLoading = false;
      }
    );
  }
}
