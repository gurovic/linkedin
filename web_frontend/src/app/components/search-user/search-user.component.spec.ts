import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SearchUserComponent } from './search-user.component';
import {HttpClientTestingModule} from '@angular/common/http/testing';

describe('SearchUserComponent', () => {
  let component: SearchUserComponent;
  let fixture: ComponentFixture<SearchUserComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [SearchUserComponent, HttpClientTestingModule]
    })
    .compileComponents();

    fixture = TestBed.createComponent(SearchUserComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
