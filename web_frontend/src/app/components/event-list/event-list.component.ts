import { Component, OnInit } from '@angular/core';
import { Event_List_Service } from '../../services/events_list.service';
import { CommonModule } from '@angular/common'; // Import CommonModule
import { environment } from '../../../environments/environment';

@Component({
  selector: 'app-event-list',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './event-list.component.html',
  styleUrls: ['./event-list.component.css'],
})
export class EventListComponent implements OnInit {
  events: any[] = []; // Store event data
  env = environment;

  constructor(private eventService: Event_List_Service) {}

  ngOnInit(): void {
    // Fetch events when component initializes
    this.eventService.getEvents().subscribe(
      (data) => {
        this.events = data;
      },
      (error) => {
        console.error('Error fetching events:', error);
      }
    );
  }
}
