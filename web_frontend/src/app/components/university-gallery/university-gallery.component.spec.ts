import { ComponentFixture, TestBed } from '@angular/core/testing';

import { UniversityGalleryComponent } from './university-gallery.component';
import {HttpClientTestingModule} from '@angular/common/http/testing';

describe('UniversityGalleryComponent', () => {
  let component: UniversityGalleryComponent;
  let fixture: ComponentFixture<UniversityGalleryComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [UniversityGalleryComponent, HttpClientTestingModule]
    })
    .compileComponents();

    fixture = TestBed.createComponent(UniversityGalleryComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
