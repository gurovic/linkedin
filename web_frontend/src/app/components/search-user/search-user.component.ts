import { Component } from '@angular/core';
import { SearchUserService } from '../../services/search-user.service';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { FormsModule } from '@angular/forms';
import { UneditableAccountComponent } from '../uneditable-account/uneditable-account.component';

@Component({
  selector: 'app-search-user',
  standalone: true,
  imports: [
    CommonModule,
    FormsModule,
    RouterModule
  ],
  templateUrl: './search-user.component.html',
  styleUrl: './search-user.component.css',
  providers: [SearchUserService]
})
export class SearchUserComponent {
  query: string = '';
  school: string = '';
  university: string = '';
  skills: string = '';
  searchResults: any = null;
  isLoading: boolean = false;
  errorMessage: string = '';

  constructor(private searchUserService: SearchUserService) {}

  performSearch() {
    this.isLoading = true;
    this.errorMessage = '';

    const payload = {
      query: this.query,
      school: this.school,
      university: this.university,
      skills: this.skills.split(',').map(skill => skill.trim())
    };

    this.searchUserService.RequestUserSearch(payload).subscribe(
      (response) => {
        this.searchResults = response;
        this.isLoading = false;
      },
      (error) => {
        if (error.status === 400 && error.error.error) {
          this.errorMessage = error.error.error;
        } else {
          this.errorMessage = 'Error fetching search results. Please try again.';
        }
        console.error(error);
        this.isLoading = false;
      }
    );
  }
}
