import { ComponentFixture, TestBed } from '@angular/core/testing';

import { VacancyCardComponent } from './vacancy-card.component';

describe('VacancyCardComponent', () => {
  let component: VacancyCardComponent;
  let fixture: ComponentFixture<VacancyCardComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [VacancyCardComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(VacancyCardComponent);
    component = fixture.componentInstance;
    component.vacancy = { name: 'Test Vacancy', description: 'This is a test vacancy.', company: 1};
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
