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
  studentSchools: any[] = [];
  studentUniversities: any[] = [];

  constructor(
    private route: ActivatedRoute,
    private userService: UserService
  ) {}

  ngOnInit(): void {
    const userId = this.route.snapshot.params['id']; // Get user ID from route
    this.userService.getUserDetails(userId).subscribe(
      (data) => {
        this.user = data;
        this.studentSchools = data.school || [];
        this.studentUniversities = data.university || [];
      },
      (error) => {
        console.error('Error fetching user details:', error);
      }
    );
  }
}
