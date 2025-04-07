import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CompanyGalleryComponent } from './company-gallery.component';
import {HttpClientTestingModule} from '@angular/common/http/testing';

describe('CompanyGalleryComponent', () => {
  let component: CompanyGalleryComponent;
  let fixture: ComponentFixture<CompanyGalleryComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [CompanyGalleryComponent, HttpClientTestingModule]
    })
    .compileComponents();

    fixture = TestBed.createComponent(CompanyGalleryComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
