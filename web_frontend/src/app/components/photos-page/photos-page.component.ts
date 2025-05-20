import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ActivatedRoute, Router } from '@angular/router';
import { HttpClient } from '@angular/common/http';
import { environment } from '../../../environments/environment';
import { AuthService } from '../../services/auth.service';

interface FaceRect {
  x: number;
  y: number;
  width: number;
  height: number;
}

interface Photo {
  id: number;
  image: string;
  rect: FaceRect;
}

@Component({
  selector: 'app-photos-page',
  templateUrl: './photos-page.component.html',
  standalone: true,
  styleUrls: ['./photos-page.component.css']
})
export class PhotosPageComponent implements OnInit {
  photos: Photo[] = [];
  loading = true;
  unauthorized = false;

  constructor(
    private route: ActivatedRoute,
    private http: HttpClient,
    private auth: AuthService,
    private router: Router
  ) {}

  ngOnInit(): void {
    const requestedId = Number(this.route.snapshot.paramMap.get('id'));
    const currentId = this.auth.currentUserId();

    if (!this.auth.isAdmin() && requestedId !== currentId) {
      this.unauthorized = true;
      this.loading = false;
      console.error('Не лезь');
      return;
    }

    this.fetchPhotos(requestedId);
  }

  private fetchPhotos(userId: number): void {
    this.http.get<Photo[]>(`${environment.apiUrl}images/${userId}/`).subscribe({
      next: data => {
        this.photos = data;
        this.loading = false;
      },
      error: err => {
        console.error('Не удалось получить фотографии', err);
        this.loading = false;
      }
    });
  }

  trackById(_: number, photo: Photo) {
    return photo.id;
  }
}
