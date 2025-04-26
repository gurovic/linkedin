import { ComponentFixture, TestBed } from '@angular/core/testing';

import { UniversityComponent } from './university.component';
import {RouterTestingModule} from '@angular/router/testing';
import {HttpClientTestingModule} from '@angular/common/http/testing';

describe('UniversityComponent', () => {
  let component: UniversityComponent;
  let fixture: ComponentFixture<UniversityComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [UniversityComponent, RouterTestingModule, HttpClientTestingModule]
    })
    .compileComponents();

    fixture = TestBed.createComponent(UniversityComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
