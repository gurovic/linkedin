import { TestBed } from '@angular/core/testing';
import { HttpClientTestingModule, HttpTestingController } from '@angular/common/http/testing';
import { VacancyService } from './vacancy.service';
import {environment} from '../../environments/environment';
import {RouterTestingModule} from '@angular/router/testing';

describe('VacancyService', () => {
  let service: VacancyService;
  let httpMock: HttpTestingController;
  const apiUrl = environment.apiUrl + 'api/vacancy/';

  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [HttpClientTestingModule, RouterTestingModule],
      providers: [VacancyService]
    });

    service = TestBed.inject(VacancyService);
    httpMock = TestBed.inject(HttpTestingController);
  });

  afterEach(() => {
    httpMock.verify(); // Проверяет, что нет незакрытых HTTP-запросов
  });

  it('должен быть создан', () => {
    expect(service).toBeTruthy();
  });

  it('должен получать вакансию по ID', () => {
    const mockVacancy = {
      id: 1,
      name: 'Frontend Developer',
      description: 'Требуется Angular-разработчик',
      required_majors: [1, 2],
      company: 5,
      expiration_date: '2025-06-01',
      required_language: [3],
      contacts: 'contact@example.com'
    };

    service.getVacancyDetails(1).subscribe(vacancy => {
      expect(vacancy).toEqual(mockVacancy);
    });

    const req = httpMock.expectOne(`${apiUrl}1`);
    expect(req.request.method).toBe('GET');
    req.flush(mockVacancy); // Отправляем мок-ответ
  });

  it('должен корректно обрабатывать ошибку 404', () => {
    service.getVacancyDetails(999).subscribe(
      () => fail('Ожидалась ошибка, но сервис вернул успешный ответ'),
      (error) => {
        expect(error.status).toBe(404);
      }
    );

    const req = httpMock.expectOne(`${apiUrl}999`);
    req.flush('Вакансия не найдена', { status: 404, statusText: 'Not Found' });
  });
});
