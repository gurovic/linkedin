import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { UneditableAccountComponent } from './components/uneditable-account/uneditable-account.component';
import { BlankComponent } from './components/blank.component';
import { EventDetailComponent } from './components/event/event.component';
import { EventGalleryComponent } from './components/event-gallery/event-gallery.component';
import { MainPageComponent } from './components/main-page/main-page.component';
import { LogoutComponent } from './components/logout/logout.component';
import { SearchUserComponent } from './components/search-user/search-user.component';

export const routes: Routes = [
  { path: 'account/:id', component: UneditableAccountComponent },
  { path: 'event/:event_id', component: EventDetailComponent },
  { path: 'events', component: EventGalleryComponent },
  { path: '', component: MainPageComponent },
  { path: 'logout', component: LogoutComponent },
  { path: 'search', component: SearchUserComponent},
  { path: '**', component: BlankComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)], // Configure routes for the root module
  exports: [RouterModule], // Export RouterModule so it can be used in the AppModule
})
export class AppRoutingModule {}
