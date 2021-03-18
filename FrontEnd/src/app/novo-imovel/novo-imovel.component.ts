import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api.service';

@Component({
  selector: 'app-novo-imovel',
  templateUrl: './novo-imovel.component.html',
  styleUrls: ['./novo-imovel.component.scss']
})
export class NovoImovelComponent implements OnInit {

  constructor(private apiService: ApiService) { }

  ngOnInit(): void {
  }

  insereNovoImovel(rua:string, num:string, andar:string, bloco:string, cidade:string, cep:string, estado:string,
    obs:string, id_prop:string, id_gastos:string){
    this.apiService.postImoveis({ "rua":rua,"num":num,"andar":andar,"bloco":bloco,"cidade":cidade,"cep":cep,"estado": estado, 
      "obs":obs, "id_prop":id_prop, "id_gastos":id_gastos}).subscribe(data => {
      console.log(data)
    },
    error  => {
    console.log("Error", error);
    });
  }
}
