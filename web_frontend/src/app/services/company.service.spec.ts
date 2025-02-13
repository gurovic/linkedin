import { TestBed } from '@angular/core/testing';

import {
  HttpTestingController,
  provideHttpClientTesting
} from '@angular/common/http/testing';
import { CompanyService } from './company.service';
import {provideHttpClient} from '@angular/common/http';

describe('CompanyService', () => {
  let service: CompanyService;
  let httpMock: HttpTestingController;

  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [],
      providers: [CompanyService, provideHttpClient(), provideHttpClientTesting()]
    });
    service = TestBed.inject(CompanyService);
    httpMock = TestBed.inject(HttpTestingController);
  });

  afterEach(() => {
    httpMock.verify();
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });

  it('should have getCompanyDetails function', () => {
    const service: CompanyService = TestBed.get(CompanyService);
    expect(service.getCompanyDetails).toBeTruthy();
  });

  it('should fetch company details', () => {
    const dummyCompanyDetails = { id: 1, name: 'Test Company' };

    service.getCompanyDetails(1).subscribe(details => {
      expect(details).toEqual(dummyCompanyDetails);
    });

    const req = httpMock.expectOne('http://localhost:8000/api/company/1/');
    expect(req.request.method).toBe('GET');
    req.flush(dummyCompanyDetails);
  });
});
