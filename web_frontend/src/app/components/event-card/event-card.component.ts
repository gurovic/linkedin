import { Component, Input } from '@angular/core';
import { CommonModule } from '@angular/common';
import { environment } from '../../../environments/environment';
import { DatePipe } from '@angular/common';
import { Router } from '@angular/router';


@Component({
  selector: 'app-event-card',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './event-card.component.html',
  styleUrls: ['./event-card.component.css'],
  providers: [DatePipe]
})
export class EventCardComponent {
  @Input() event: any;
  env = environment;

  constructor(private datePipe: DatePipe, private router: Router) {}

  formatDate(dateString: string): string {
    const date = new Date(dateString);
    const formattedDate = this.datePipe.transform(date, 'dd.MM.yyyy HH:mm'); 
    return formattedDate || dateString; 
  }

  goToEventDetails(): void {
    this.router.navigate(['/event', this.event.id]);
  }
}
