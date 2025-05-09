import { ComponentFixture, TestBed } from '@angular/core/testing';
import { FormResumeAutofillComponent } from './form-resume-autofill.component';
import { HttpClientTestingModule } from '@angular/common/http/testing';

describe('FormResumeAutofillComponent', () => {
  let component: FormResumeAutofillComponent;
  let fixture: ComponentFixture<FormResumeAutofillComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [FormResumeAutofillComponent, HttpClientTestingModule]
    })
    .compileComponents();

    fixture = TestBed.createComponent(FormResumeAutofillComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
