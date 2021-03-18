import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { ApiService } from '../api.service';

@Component({
  selector: 'app-altera-imovel',
  templateUrl: './altera-imovel.component.html',
  styleUrls: ['./altera-imovel.component.scss']
})
export class AlteraImovelComponent implements OnInit {
  imovel:any

  constructor(private activatedRoute: ActivatedRoute,
               private apiService: ApiService) { 
    this.activatedRoute.queryParams.subscribe(params => {
      //console.log(params['id'])
      this.carregaImoveis(Number(params['id']))
      });
  }

  ngOnInit(): void {
  }

  carregaImoveis(imovelid:number){
    console.log(imovelid);
    this.apiService.getImovel(imovelid).subscribe(data => {
      this.imovel = data;
    },
    error  => {
    console.log("Error", error);
    });
  }

  alteraImovel( imovelid: number, rua:string, num:string, andar:string, bloco:number, cidade:string, cep:string,
      estado:string, obs: string, id_prop: string, id_gastos: string){
      
    let imovel = {"rua":rua, "num":num, "andar":andar, "bloco":bloco,"cep":cep, "cidade":cidade, "estado": estado,
      "obs":obs, "id_prop":id_prop, "id_gastos":id_gastos };
      return this.apiService.putImoveis(imovelid,  imovel)
    .subscribe(data => {
      console.log(data)
    });
  }
}
