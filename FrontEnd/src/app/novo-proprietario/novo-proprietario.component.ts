import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api.service';

@Component({
  selector: 'app-novo-proprietario',
  templateUrl: './novo-proprietario.component.html',
  styleUrls: ['./novo-proprietario.component.scss']
})
export class NovoProprietarioComponent implements OnInit {

  constructor(private apiService: ApiService) { }

  ngOnInit(): void {
  }

  insereNovoProprietario(nome_prop:string, data_nasc_prop:string, cpf_prop:string, rg_prop:string, est_civil_prop:string, tel_prop:string, formacao:string, temp_imovel:string){
    this.apiService.postProprietario({ "nome_prop":nome_prop , "data_nasc_prop":data_nasc_prop, "cpf_prop": cpf_prop, "rg_prop": rg_prop,"est_civil_prop": est_civil_prop,"tel_prop":tel_prop,"formacao": formacao,
    "temp_imovel":temp_imovel}).subscribe(data => {
      console.log(data)
    },
    error  => {
    console.log("Error", error);
    });
  }
}
