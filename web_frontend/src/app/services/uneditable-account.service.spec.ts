import { TestBed } from '@angular/core/testing';

import { UneditableAccountService } from './uneditable-account.service';

describe('UneditableAccountService', () => {
  let service: UneditableAccountService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(UneditableAccountService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
