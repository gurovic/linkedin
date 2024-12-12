import { Component, OnInit } from '@angular/core';
import { AccountService } from '../services/account.service';

@Component({
  selector: 'app-account',
  templateUrl: './account.component.html',
  styleUrls: ['./account.component.css']
})
export class AccountComponent implements OnInit {
  user: any;
  studentSchools: any[] = [];
  studentUniversities: any[] = [];
  errorMessage: string = '';

  constructor(private accountService: AccountService) { }

  ngOnInit(): void {
    const userId = 1; // Replace with dynamic user ID or route param if needed
    this.accountService.getAccountDetails(userId).subscribe(
      data => {
        this.user = data.user;
        this.studentSchools = data.student_schools;
        this.studentUniversities = data.student_universities;
      },
      error => {
        this.errorMessage = 'Unable to load account details. Please try again later.';
      }
    );
  }
}
