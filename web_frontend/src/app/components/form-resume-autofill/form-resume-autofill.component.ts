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
    const file = event.target.files[0];
    if (file && file.type === 'application/pdf') {
      this.selectedFile = file;
    } else {
      alert('Пожалуйста, выберите PDF файл.');
      this.selectedFile = null;
    }
  }

  uploadFile() {
    if (!this.selectedFile) return;

    const formData = new FormData();
    formData.append('file', this.selectedFile);

    this.http.post(this.backendUrl, formData).subscribe({
      next: () => this.showModal('successModal'),
      error: (error) => {
        console.error('Upload error:', error);
        let errorMessage = 'Ошибка загрузки файла. Попробуйте еще раз.';
        if (error.status === 413) {
          errorMessage = 'Файл слишком большой. Пожалуйста, загрузите файл меньшего размера.';
        } else if (error.status === 500) {
          errorMessage = 'Ошибка сервера при загрузке файла. Попробуйте позже.';
        }
        this.showModal('errorModal', errorMessage);
      },
    });
  }

  showModal(modalId: string, message?: string) {
    const modalElement = document.getElementById(modalId);
    if (modalElement) {
        const modal = new bootstrap.Modal(modalElement);
        if (message) {
            const modalBody = modalElement.querySelector('.modal-body');
            if (modalBody) {
                modalBody.textContent = message;
            }
        }
        modal.show();
    }
  }
}
