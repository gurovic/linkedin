import { Component, OnInit } from '@angular/core';
import { Event_List_Service } from '../../services/events_list.service';
import { CommonModule } from '@angular/common';
import { environment } from '../../../environments/environment';
import { EventCardComponent } from '../event-card/event-card.component';

@Component({
  selector: 'app-event-gallery',
  standalone: true,
  imports: [CommonModule, EventCardComponent],
  templateUrl: './event-gallery.component.html',
  styleUrls: ['./event-gallery.component.css'],
})
export class EventGalleryComponent implements OnInit {
  events: any[] = [];
  env = environment;

  constructor(private eventService: Event_List_Service) {}

  ngOnInit(): void {
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
