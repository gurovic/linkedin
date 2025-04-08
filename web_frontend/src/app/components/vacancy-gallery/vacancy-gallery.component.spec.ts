import { ComponentFixture, TestBed } from '@angular/core/testing';

import { VacancyGalleryComponent } from './vacancy-gallery.component';
import {HttpClientTestingModule} from '@angular/common/http/testing';

describe('VacancyGalleryComponent', () => {
  let component: VacancyGalleryComponent;
  let fixture: ComponentFixture<VacancyGalleryComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [VacancyGalleryComponent, HttpClientTestingModule]
    })
    .compileComponents();

    fixture = TestBed.createComponent(VacancyGalleryComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
