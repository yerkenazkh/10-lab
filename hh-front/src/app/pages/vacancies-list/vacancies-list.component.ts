import { Component, OnInit } from '@angular/core';
import { CompanyService } from 'src/app/services/company.service';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-vacancies-list',
  templateUrl: './vacancies-list.component.html',
  styleUrls: ['./vacancies-list.component.css']
})
export class VacanciesListComponent implements OnInit {
  public company
  public vacancies

  constructor(private companyService: CompanyService, private route: ActivatedRoute) { }
  public id = this.route.snapshot.paramMap.get('company_id')

  ngOnInit(): void {
    this.companyService.getCompany(this.id).subscribe(company => {
      this.company = company
    })

    this.companyService.getVacancies(this.id).subscribe(vacancies => {
      this.vacancies = vacancies
      console.log(vacancies)
    })
  }

}
