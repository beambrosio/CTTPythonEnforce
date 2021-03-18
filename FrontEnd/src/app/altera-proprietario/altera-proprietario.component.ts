import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { ApiService } from '../api.service';

@Component({
  selector: 'app-altera-proprietario',
  templateUrl: './altera-proprietario.component.html',
  styleUrls: ['./altera-proprietario.component.scss']
})
export class AlteraProprietarioComponent implements OnInit {
  proprietario:any
  constructor(private activatedRoute: ActivatedRoute, private apiService: ApiService) {
    this.activatedRoute.queryParams.subscribe(params => {
      //console.log(params['id'])
      this.carregaProprietario(Number(params['id']))
      });
    }
  ngOnInit(): void {
  }

  carregaProprietario(propid:number){
    console.log(propid);
    this.apiService.getProprietario(propid).subscribe(data => {
      this.proprietario = data;
    },
    error  => {
    console.log("Error", error);
    });
  }

  alteraProprietario( propid:number , nome_prop:string, data_nasc_prop:string, cpf_prop:string, rg_prop:number, est_civil_prop:string,tel_prop:string, formacao:string,
    temp_imovel:number){
      
    let proprietario = { "nome_prop": nome_prop, "data_nasc_prop":data_nasc_prop, "cpf_prop":cpf_prop,"rg_prop":rg_prop,"tel_prop":tel_prop, "est_civil_prop": est_civil_prop,"formacao":formacao,
      temp_imovel};
      return this.apiService.putProprietario(propid,  proprietario)
    .subscribe(data => {
      console.log(data)
    });
  }
}