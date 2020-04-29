import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { CompaniesListComponent } from './pages/companies-list/companies-list.component';
import { VacanciesListComponent } from './pages/vacancies-list/vacancies-list.component';


const routes: Routes = [
  {path: '', redirectTo: '/companies-page', pathMatch: 'full'},
  {path: 'companies-page', component: CompaniesListComponent},
  {path: ':company_id', component: VacanciesListComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
