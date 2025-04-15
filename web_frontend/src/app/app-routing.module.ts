import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { UneditableAccountComponent } from './components/uneditable-account/uneditable-account.component';
import { BlankComponent } from './components/blank.component';
import { EventDetailComponent } from './components/event/event.component';
import { EventGalleryComponent } from './components/event-gallery/event-gallery.component';
import { MainPageComponent } from './components/main-page/main-page.component';
import { LogoutComponent } from './components/logout/logout.component';
import { SearchUserComponent } from './components/search-user/search-user.component';
import { CompanyComponent } from './components/company/company.component';
import { VacancyComponent } from './components/vacancy/vacancy.component';
import { VacancyGalleryComponent } from './components/vacancy-gallery/vacancy-gallery.component';
import { GorodComponent } from './components/gorod/gorod.component';
import { CompanyGalleryComponent} from './components/company-gallery/company-gallery.component';
import { AuthGuard } from './guards/auth.guard';

export const routes: Routes = [
  { path: 'account/:id', component: UneditableAccountComponent },
  { path: 'account', component: UneditableAccountComponent },
  { path: 'event/:event_id', component: EventDetailComponent },
  { path: 'events', component: EventGalleryComponent },
  { path: '', component: MainPageComponent },
  { path: 'logout', component: LogoutComponent },
  { path: 'search', component: SearchUserComponent},
  { path: 'company/:id', component: CompanyComponent},
  { path: 'vacancy/:vacancy_id', component: VacancyComponent},
  { path: 'vacancies', component: VacancyGalleryComponent},
  {
    path: 'gorod',
    component: GorodComponent,
    canActivate: [AuthGuard]
  },
  { path: 'companies', component: CompanyGalleryComponent},
  { path: '**', component: BlankComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
