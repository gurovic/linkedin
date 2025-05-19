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
  user: any = null;
  universities: any[] = [];
  studentUniversities: any[] = [];
  isOwn: boolean = false;

  selectedFile: File | null = null;
  uploadSuccessMessage: string = '';
  uploadErrorMessage: string = '';

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
          this.isOwn = true;
        },
        (error) => {
          console.error('Error fetching user details:', error);
        }
      );
      return;
    }
    const userId = this.route.snapshot.params['id'];
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

  onFileSelected(event: Event): void {
    const input = event.target as HTMLInputElement;
    if (input.files && input.files.length > 0) {
      this.selectedFile = input.files[0];
    }
  }

  onResumeUpload(event: Event): void {
    event.preventDefault();
    if (this.selectedFile) {
      this.userService.uploadResume(this.selectedFile).subscribe(
        (response) => {
          this.uploadSuccessMessage = 'Resume uploaded successfully!';
          this.uploadErrorMessage = '';
        },
        (error) => {
          this.uploadErrorMessage = 'Error uploading resume.';
          this.uploadSuccessMessage = '';
          console.error('Error uploading resume:', error);
        }
      );
    } else {
      this.uploadErrorMessage = 'Please select a file to upload.';
      this.uploadSuccessMessage = '';
    }
  }
}
