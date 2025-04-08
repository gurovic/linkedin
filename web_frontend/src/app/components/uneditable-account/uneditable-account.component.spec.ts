import { ComponentFixture, TestBed } from '@angular/core/testing';

import { UneditableAccountComponent } from './uneditable-account.component';
import {RouterTestingModule} from '@angular/router/testing';
import {HttpClientTestingModule} from '@angular/common/http/testing';

describe('UneditableAccountComponent', () => {
  let component: UneditableAccountComponent;
  let fixture: ComponentFixture<UneditableAccountComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [UneditableAccountComponent, RouterTestingModule, HttpClientTestingModule]
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
