import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CompanyCardComponent } from './company-card.component';

describe('СompanyCardComponent', () => {
  let component: CompanyCardComponent;
  let fixture: ComponentFixture<CompanyCardComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [CompanyCardComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(CompanyCardComponent);
    component = fixture.componentInstance;
    component.company = { name: 'Test Company', description: 'This is a test company.', country: 'DE'};
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
