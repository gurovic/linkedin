import { ComponentFixture, TestBed } from '@angular/core/testing';
import { HttpClientTestingModule, HttpTestingController } from '@angular/common/http/testing';
import { RouterTestingModule } from '@angular/router/testing';
import { ReactiveFormsModule, FormsModule } from '@angular/forms';
import { LoginComponent } from './login.component';
import { Router } from '@angular/router';

describe('LoginComponent', () => {
  let component: LoginComponent;
  let fixture: ComponentFixture<LoginComponent>;
  let httpMock: HttpTestingController;
  let router: Router;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [
        HttpClientTestingModule,
        RouterTestingModule,
        ReactiveFormsModule,
        FormsModule,
        LoginComponent
      ],
      declarations: []
    }).compileComponents();

    fixture = TestBed.createComponent(LoginComponent);
    component = fixture.componentInstance;
    httpMock = TestBed.inject(HttpTestingController);
    router = TestBed.inject(Router);
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  it('should login successfully', () => {
    const navigateSpy = spyOn(router, 'navigate');
    component.loginForm.setValue({ username: 'testuser', password: 'testpass' });

    component.onSubmit();

    const req = httpMock.expectOne('http://localhost:8000/api/auth/login/');
    expect(req.request.method).toBe('POST');
    expect(req.request.headers.get('Authorization')).toBe('Basic ' + btoa('testuser:testpass'));

    req.flush({"expiry":"2025-02-04T00:20:12.791128+03:00","token":"token"});

    expect(component.loginError).toBeNull();

    expect(navigateSpy).toHaveBeenCalledWith(['/']);
  });

  it('should handle login failure', () => {
    spyOn(console, 'error');
    component.loginForm.setValue({ username: 'testuser', password: 'testpass' });

    component.onSubmit();

    const req = httpMock.expectOne('http://localhost:8000/api/auth/login/');
    req.flush('Login failed', { status: 401, statusText: 'Unauthorized' });

    expect(component.loginError).toBe('Invalid username or password');

    expect(console.error).toHaveBeenCalledWith('Login failed', jasmine.any(Object));
  });

  afterEach(() => {
    httpMock.verify();
  });
});
