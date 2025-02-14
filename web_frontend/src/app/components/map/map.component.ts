import {AfterViewInit, Component} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import * as L from 'leaflet';
import 'leaflet.markercluster';
import {forkJoin, Observable} from 'rxjs';

// Interfaces for type safety
interface UniversityStudent {
  id: number;
  student: number;
  university: number;
  leave_reason: string | null;
  start_year: number;
  end_year: number | null;
}

interface University {
  id: number;
  name: string;
  description: string;
  majors_availible: string[];
  lat: number;
  lon: number;
  country: string;
}

interface User {
  id: number;
  first_name: string;
  last_name: string;
  university: University[];
}

@Component({
  selector: 'app-map',
  templateUrl: './map.component.html',
  styleUrls: ['./map.component.css']
})
export class MapComponent implements AfterViewInit {
  private map!: L.Map;
  private markerClusterGroup = L.markerClusterGroup();

  constructor(private http: HttpClient) {
    delete (L.Icon.Default.prototype as any)._getIconUrl;
    L.Icon.Default.mergeOptions({
      iconRetinaUrl: 'assets/marker-icon-2x.png',
      iconUrl: 'assets/marker-icon.png',
      shadowUrl: 'assets/marker-shadow.png'
    });
  }

  ngAfterViewInit(): void {
    this.initMap();
  }

  private initMap(): void {
    this.map = L.map('mapid').setView([51.505, -0.09], 13);

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: '&copy; OpenStreetMap contributors'
    }).addTo(this.map);

    this.fetchUserMarkers();
  }

  private fetchUserMarkers(): void {
    const currentStudentsUrl = 'http://localhost:8000/api/universitystudent/current';

    this.http.get<UniversityStudent[]>(currentStudentsUrl).subscribe(
      (students: UniversityStudent[]) => {
        const userRequests: Observable<User>[] = students.map(student =>
          this.http.get<User>(`http://localhost:8000/api/user/${student.student}/`)
        );

        forkJoin(userRequests).subscribe(
          (users: User[]) => {
            users.forEach(user => {
              if (user.university && user.university.length > 0) {
                const uni = user.university[0];
                const lat = Number(uni.lat);
                const lon = Number(uni.lon);

                if (!isNaN(lat) && !isNaN(lon)) {
                  console.log(`Adding marker for ${user.first_name} ${user.last_name} at [${lat}, ${lon}]`);
                  const marker = L.marker([lat, lon], {
                    icon: L.icon({
                      iconRetinaUrl: 'assets/marker-icon-2x.png',
                      iconUrl: 'assets/marker-icon.png',
                      shadowUrl: 'assets/marker-shadow.png',
                      iconSize: [25, 41],
                    })
                  }).bindPopup(
                    `<strong>${user.first_name} ${user.last_name}</strong><br>${uni.name}`
                  );
                  this.map.addLayer(marker);
                  console.log('Adding marker to cluster group:', marker);

                  this.markerClusterGroup.addLayer(marker);
                } else {
                  console.warn(`Invalid coordinates for ${user.first_name} ${user.last_name}: [${lat}, ${lon}]`);
                }
              }
            });
            console.log('Total markers in cluster group:', this.markerClusterGroup.getLayers().length);

            if (!this.map.hasLayer(this.markerClusterGroup)) {
              this.map.addLayer(this.markerClusterGroup);
            }

            if (this.markerClusterGroup.getLayers().length > 0) {
              this.map.fitBounds(this.markerClusterGroup.getBounds());
            }
          },
          error => {
            console.error('Error fetching user data:', error);
          }
        );
      },
      error => {
        console.error('Error fetching current student data:', error);
      }
    );
  }
}
