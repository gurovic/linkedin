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
    signupForm: FormGroup;

    constructor(private fb: FormBuilder, private http: HttpClient) {
        this.signupForm = this.fb.group({
            email: ['', [Validators.required, Validators.email]],
            university: ['', Validators.required],
            photo: [null, Validators.required]
        });
    }

    onFileSelected(event: Event): void {
        const file = (event.target as HTMLInputElement)?.files?.[0];
        if (file) {
            this.signupForm.patchValue({ photo: file });
        }
    }

    onSubmit(): void {
        if (this.signupForm.invalid) return;

        const formData = new FormData();
        formData.append('email', this.signupForm.value.email);
        formData.append('university', this.signupForm.value.university);
        formData.append('photo', this.signupForm.value.photo);
        this.http.post(environment.apiUrl + `api/alumni-verification-request/`, formData).subscribe({
            next: () => alert('Заявка успешно отправлена!'),
            error: (err) => alert('Ошибка при отправке: ' + err.message)
        });
    }
}
