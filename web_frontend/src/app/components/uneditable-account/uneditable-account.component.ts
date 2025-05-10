import { Component } from '@angular/core';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { ActivatedRoute } from '@angular/router'; // 🔥 ДОБАВЛЕНО для получения ID из URL
import { CommonModule } from '@angular/common'; // ДОБАВИТЬ импорт

@Component({
  selector: 'app-uneditable-account',
  standalone: true, // Сказать Angular, что компонент сам по себе
  imports: [CommonModule], // ПОДКЛЮЧИТЬ CommonModule
  templateUrl: './uneditable-account.component.html',
})
export class UneditableAccountComponent {
  user: any;
  universities: any[] = [];

  // 🔥 ДОБАВЛЕНО для загрузки резюме
  selectedFile: File | null = null;
  uploadSuccessMessage: string = '';
  uploadErrorMessage: string = '';

  constructor(private http: HttpClient, private route: ActivatedRoute) {
    // 🔥 ДОБАВЛЕНО: загрузка данных пользователя сразу в конструкторе
    const userId = this.route.snapshot.paramMap.get('id');
    if (userId) {
      this.http.get(`/api/account/${userId}/`).subscribe({
        next: (data: any) => {
          this.user = data;
          this.universities = data.universities || [];
        },
        error: (error: HttpErrorResponse) => {
          console.error('Ошибка при загрузке пользователя:', error);
        }
      });
    }
  }

  getStudentUniversity(universityId: number): any {
  return this.universities.find((u) => u.id === universityId) || null;
  }

  // 🔥 ДОБАВЛЕНО: метод для выбора файла
  onFileSelected(event: Event): void {
    const input = event.target as HTMLInputElement;
    if (input.files && input.files.length > 0) {
      this.selectedFile = input.files[0];
    }
  }

  // 🔥 ДОБАВЛЕНО: метод для отправки файла на сервер
  onResumeUpload(event: Event): void {
    event.preventDefault();

    this.uploadSuccessMessage = '';
    this.uploadErrorMessage = '';

    if (!this.selectedFile) {
      this.uploadErrorMessage = 'Файл не выбран.';
      return;
    }

    const formData = new FormData();
    formData.append('file', this.selectedFile);

    this.http.post<any>('/upload-resume/', formData).subscribe({
      next: (response) => {
        this.uploadSuccessMessage = response.message || 'Резюме успешно загружено!';
      },
      error: (error: HttpErrorResponse) => {
  if (error.status === 413) {
    this.uploadErrorMessage = 'Файл слишком большой. Пожалуйста, выберите файл меньшего размера.';
  } else if (error.status === 415) {
    this.uploadErrorMessage = 'Неподдерживаемый формат файла. Допустимы PDF, DOC или DOCX.';
  } else if (error.status === 400 && error.error?.error) {
    this.uploadErrorMessage = `Ошибка: ${error.error.error}`;
  } else {
    this.uploadErrorMessage = 'Произошла ошибка при загрузке резюме. Попробуйте снова позже.';
  }
  console.log(error);
      }
    });
  }
}
