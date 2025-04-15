import { ComponentFixture, TestBed } from '@angular/core/testing';

import { UniversityCardComponent } from './university-card.component';

describe('UniversityCardComponent', () => {
  let component: UniversityCardComponent;
  let fixture: ComponentFixture<UniversityCardComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [UniversityCardComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(UniversityCardComponent);
    component = fixture.componentInstance;
    component.university = { name: 'Test University', description: 'This is a test university.', lat: 1, lon: 1};
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
