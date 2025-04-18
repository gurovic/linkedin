import {Injectable} from '@angular/core';
import {
  HttpEvent,
  HttpHandler,
  HttpInterceptor,
  HttpRequest
} from '@angular/common/http';
import {Observable} from 'rxjs';
import {environment} from '../../environments/environment';

@Injectable()
export class AuthInterceptor implements HttpInterceptor {
  intercept(req: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
    if (req.url.includes('auth/login')) {
      return next.handle(req);
    }
    if (!req.url.includes(environment.apiUrl) && !req.url.includes(environment.mediaUrl)) {
      return next.handle(req);
    }
    const token = localStorage.getItem('authToken');
    if (token) {
      const cloned = req.clone({
        headers: req.headers.set('Authorization', 'Token ' + token)
      });
      return next.handle(cloned);
    } else {
      return next.handle(req);
    }
  }
}
