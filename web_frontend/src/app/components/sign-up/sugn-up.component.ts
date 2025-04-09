import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-sign-up',
  templateUrl: './sign-up.component.html',
  styleUrls: ['./sign-up.component.css']
})
export class SignUpComponent {
  showForm = false;
  formData = {
    fullName: '',
    email: '',
    university: ''
  };
  selectedFile: File | null = null;

  constructor(private http: HttpClient) {}

  toggleForm() {
    this.showForm = !this.showForm;
  }

  onFileSelected(event: any) {
    this.selectedFile = event.target.files[0];
  }

  onSubmit() {
    const form = new FormData();
    form.append('full_name', this.formData.fullName);
    form.append('email', this.formData.email);
    form.append('university', this.formData.university);
    if (this.selectedFile) {
      form.append('photo', this.selectedFile);
    }

    this.http.post('http://localhost:8000/api/verify-description', form).subscribe({
      next: () => {
        alert('Данные успешно отправлены!');
        this.showForm = false;
      },
      error: (error) => {
        alert('Ошибка отправки данных.');
        console.error(error);
      }
    });
  }
}
