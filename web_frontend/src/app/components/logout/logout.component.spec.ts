import { ComponentFixture, TestBed } from '@angular/core/testing';

import { LogoutComponent } from './logout.component';
import { Router } from '@angular/router';
import { HttpClientTestingModule } from '@angular/common/http/testing';

describe('LogoutComponent', () => {
  let component: LogoutComponent;
  let fixture: ComponentFixture<LogoutComponent>;
  let router: Router;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [LogoutComponent, HttpClientTestingModule]
    })
    .compileComponents();

    fixture = TestBed.createComponent(LogoutComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
    router = TestBed.inject(Router);

    // Setting the token here
    localStorage.setItem("authToken", "toBeDeleted");
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  it('should delete the session token', () => {
    const navigateSpy = spyOn(router, 'navigate');

    component.ngOnInit();
    expect(navigateSpy).toHaveBeenCalledWith(['/']);
    expect(localStorage.getItem("authToken")).toBeNull();
  });
});
