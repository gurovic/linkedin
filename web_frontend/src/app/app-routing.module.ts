import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { UneditableAccountComponent } from './components/uneditable-account/uneditable-account.component';
import { BlankComponent } from './components/blank.component';
import { EventDetailComponent } from './components/event/event.component';
import { EventListComponent } from './components/event-list/event-list.component';

export const routes: Routes = [
  { path: 'account/:id', component: UneditableAccountComponent },
  { path: 'event/:event_id', component: EventDetailComponent },
  { path: 'events', component: EventListComponent },
  { path: '**', component: BlankComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)], // Configure routes for the root module
  exports: [RouterModule], // Export RouterModule so it can be used in the AppModule
})
export class AppRoutingModule {}
