import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { UserService } from '../../services/uneditable-account.service';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-uneditable-account',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './uneditable-account.component.html',
  styleUrls: ['./uneditable-account.component.css']
})
export class UneditableAccountComponent implements OnInit {
  user: any = null; // Store user data
  universities: any[] = [];
  studentUniversities: any[] = [];

  constructor(
    private route: ActivatedRoute,
    private userService: UserService
  ) {}

  getStudentUniversity(universityId: number): any {
    return this.studentUniversities.find(su => su.university === universityId);
  }

  ngOnInit(): void {
    if (!this.route.snapshot.params['id']) {
      this.userService.getOwnDetails().subscribe(
        (data) => {
          this.user = data;
          this.universities = data.university || [];
          this.studentUniversities = data.university_student || [];
        },
        (error) => {
          console.error('Error fetching user details:', error);
        }
      );
      return;
    }
    const userId = this.route.snapshot.params['id']; // Get user ID from route
    this.userService.getUserDetails(userId).subscribe(
      (data) => {
        this.user = data;
        this.universities = data.university || [];
        this.studentUniversities = data.university_student || [];
      },
      (error) => {
        console.error('Error fetching user details:', error);
      }
    );
  }
}
