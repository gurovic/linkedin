import { ComponentFixture, TestBed } from '@angular/core/testing';

import { GorodComponent } from './gorod.component';

describe('GorodComponent', () => {
  let component: GorodComponent;
  let fixture: ComponentFixture<GorodComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [GorodComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(GorodComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
