import { ComponentFixture, TestBed } from '@angular/core/testing';

import { VacancyGalleryComponent } from './vacancy-gallery.component';

describe('VacancyGalleryComponent', () => {
  let component: VacancyGalleryComponent;
  let fixture: ComponentFixture<VacancyGalleryComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [VacancyGalleryComponent]
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
