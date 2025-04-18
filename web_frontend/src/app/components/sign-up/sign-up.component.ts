import { Component } from '@angular/core';
import { FormBuilder, FormGroup, Validators, ReactiveFormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { HttpClient, HttpClientModule } from '@angular/common/http';
import {environment} from '../../../environments/environment';

@Component({
    selector: 'app-sign-up',
    standalone: true,
    imports: [CommonModule, ReactiveFormsModule, HttpClientModule],
    templateUrl: './sign-up.component.html'
})
export class SignupComponent {
  entryForm: FormGroup;

  constructor(private fb: FormBuilder, private http: HttpClient) {
    this.entryForm = this.fb.group({
      surname: ['', Validators.required],
      firstName: ['', Validators.required],
      middleName: [''],
      email: ['', [Validators.required, Validators.email]],
      institution: ['', Validators.required],
      photo: [null, Validators.required]
    });
  }

  onFileSelected(event: Event): void {
    const file = (event.target as HTMLInputElement)?.files?.[0];
    if (file) {
      this.entryForm.patchValue({ photo: file });
    }
  }

  onSubmit(): void {
    if (this.entryForm.invalid) return;

    const fd = new FormData();
    fd.append('surname', this.entryForm.value.surname);
    fd.append('firstName', this.entryForm.value.firstName);
    fd.append('middleName', this.entryForm.value.middleName);
    fd.append('email', this.entryForm.value.email);
    fd.append('university', this.entryForm.value.institution);
    fd.append('photo', this.entryForm.value.photo);

    this.http.post(environment.apiUrl + `api/alumni-verification-request/`, fd).subscribe({
      next: () => alert('Анкета отправлена!'),
      error: (err) => alert('Ошибка: ' + err.message)
    });
  }
}
