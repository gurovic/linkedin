import { ComponentFixture, TestBed } from '@angular/core/testing';
import { SignupComponent } from './sign-up.component';
import { ReactiveFormsModule } from '@angular/forms';
import { HttpClientTestingModule } from '@angular/common/http/testing';

describe('SignupComponent', () => {
    let component: SignupComponent;
    let fixture: ComponentFixture<SignupComponent>;

    beforeEach(async () => {
        await TestBed.configureTestingModule({
            imports: [SignupComponent, ReactiveFormsModule, HttpClientTestingModule]
        }).compileComponents();

        fixture = TestBed.createComponent(SignupComponent);
        component = fixture.componentInstance;
        fixture.detectChanges();
    });

    it('should create', () => {
        expect(component).toBeTruthy();
    });

    it('should invalidate the form when empty', () => {
        expect(component.entryForm.valid).toBeFalsy();
    });

    it('should validate form with correct data', () => {
        component.entryForm.setValue({
            surname: 'Ivanov',
            firstName: 'Ivan',
            middleName: 'Ivanovich',
            email: 'test@example.com',
            university: 'Test University',
            photo: new File([], 'photo.jpg')
        });
        expect(component.entryForm.valid).toBeTruthy();
    });
});
