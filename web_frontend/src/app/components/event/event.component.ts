import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { EventService } from '../../services/event.service';
import {CommonModule} from '@angular/common';
import {environment} from '../../../environments/environment';

@Component({
  selector: 'app-event-detail',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './event.component.html',
  styleUrls: ['./event.component.css'],
})
export class EventDetailComponent implements OnInit {
  event: any = null; // Store event data
  env = environment;

  constructor(
    private route: ActivatedRoute,
    private eventService: EventService
  ) {}

  ngOnInit(): void {
    const eventId = this.route.snapshot.params['event_id']; // Get event ID from route
    this.eventService.getEventDetails(eventId).subscribe(
      (data) => {
        this.event = data; // Assign API response to the event object
      },
      (error) => {
        console.error('Error fetching event details:', error);
      }
    );
  }
}
