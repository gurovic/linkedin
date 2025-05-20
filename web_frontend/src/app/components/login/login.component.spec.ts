import { ComponentFixture, TestBed } from '@angular/core/testing';
import { LoginComponent } from './login.component';
import { provideHttpClientTesting, HttpTestingController } from '@angular/common/http/testing';
import { provideRouter } from '@angular/router';
import { AuthService } from '../../services/auth.service';
import { of } from 'rxjs';

describe('LoginComponent', () => {
  let component: LoginComponent;
  let fixture: ComponentFixture<LoginComponent>;
  let httpMock: HttpTestingController;
  let authServiceSpy: jasmine.SpyObj<AuthService>;
  let emitted = false;

  beforeEach(async () => {
    const authSpy = jasmine.createSpyObj('AuthService', ['login']);

    await TestBed.configureTestingModule({
      imports: [LoginComponent],
      providers: [
        provideHttpClientTesting(),
        provideRouter([]),
        { provide: AuthService, useValue: authSpy }
      ]
    }).compileComponents();

    fixture = TestBed.createComponent(LoginComponent);
    component = fixture.componentInstance;
    httpMock = TestBed.inject(HttpTestingController);
    authServiceSpy = TestBed.inject(AuthService) as jasmine.SpyObj<AuthService>;

    component.closeLoginPopup.subscribe(() => emitted = true);

    fixture.detectChanges();
  });

  afterEach(() => {
    httpMock.verify();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  it('should login successfully', () => {
    component.loginForm.setValue({ username: 'testuser', password: 'testpass' });

    component.onSubmit();

    const req = httpMock.expectOne(req =>
      req.method === 'POST' &&
      req.url.endsWith('/api/auth/login/')
    );
    expect(req.request.headers.get('Authorization')).toContain('Basic');
    req.flush({ token: 'fake-token', expiry: '2025-01-01T00:00:00Z' });

    expect(authServiceSpy.login).toHaveBeenCalledWith('fake-token');

    expect(emitted).toBeTrue();
  });
});
