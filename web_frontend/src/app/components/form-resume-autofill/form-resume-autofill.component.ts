import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from '../../../environments/environment';
import * as bootstrap from 'bootstrap';

@Component({
  selector: 'app-form-resume-autofill',
  templateUrl: './form-resume-autofill.component.html',
  styleUrls: ['./form-resume-autofill.component.css']
})
export class FormResumeAutofillComponent {
  selectedFile: File | null = null;
  backendUrl = environment.apiUrl + '/cvautofill'; 

  constructor(private http: HttpClient) {}

  onFileSelected(event: any) {
    this.selectedFile = event.target.files[0];
  }

  uploadFile() {
    if (!this.selectedFile) return;

    const formData = new FormData();
    formData.append('file', this.selectedFile);

    this.http.post(this.backendUrl, formData).subscribe({
      next: () => this.showModal('successModal'),
      error: () => this.showModal('errorModal'),
    });
  }

  showModal(modalId: string) {
    const modalElement = document.getElementById(modalId);
    if (modalElement) {
      const modal = new bootstrap.Modal(modalElement);
      modal.show();
    }
  }
}
