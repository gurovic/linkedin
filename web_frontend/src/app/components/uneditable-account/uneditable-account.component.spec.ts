import { ComponentFixture, TestBed } from '@angular/core/testing';

import { UneditableAccountComponent } from './uneditable-account.component';

describe('UneditableAccountComponent', () => {
  let component: UneditableAccountComponent;
  let fixture: ComponentFixture<UneditableAccountComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [UneditableAccountComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(UneditableAccountComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
