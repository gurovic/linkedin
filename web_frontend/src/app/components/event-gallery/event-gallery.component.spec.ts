import { ComponentFixture, TestBed } from '@angular/core/testing';

import { EventGalleryComponent } from './event-gallery.component';
import {HttpClientTestingModule} from '@angular/common/http/testing';

describe('EventGalleryComponent', () => {
  let component: EventGalleryComponent;
  let fixture: ComponentFixture<EventGalleryComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [EventGalleryComponent, HttpClientTestingModule]
    })
    .compileComponents();

    fixture = TestBed.createComponent(EventGalleryComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
