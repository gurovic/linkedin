import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { UneditableAccountComponent } from './components/uneditable-account/uneditable-account.component';

export const routes: Routes = [
  { path: 'account/:id', component: UneditableAccountComponent },
  { path: '', redirectTo: '/account/1', pathMatch: 'full' }, // Default route
];

@NgModule({
  imports: [RouterModule.forRoot(routes)], // Configure routes for the root module
  exports: [RouterModule], // Export RouterModule so it can be used in the AppModule
})
export class AppRoutingModule {}