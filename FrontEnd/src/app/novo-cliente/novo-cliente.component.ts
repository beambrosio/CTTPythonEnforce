import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api.service';

@Component({
  selector: 'app-novo-cliente',
  templateUrl: './novo-cliente.component.html',
  styleUrls: ['./novo-cliente.component.scss']
})
export class NovoClienteComponent implements OnInit {

  constructor(private apiService: ApiService) { }

  ngOnInit(): void {
  }

  insereNovoCliente(nome_cliente:string, data_nasc_cliente:string, cpf_cliente:string, rg_cliente:string, est_civil_cliente:string, tel_cliente:string, formacao_cliente:string, rua:string, num:string, andar:string, bloco:string, cidade:string, cep:string, estado:string ){
    this.apiService.postCliente({ "nome_cliente":nome_cliente , "data_nasc_cliente":data_nasc_cliente, "cpf_cliente": cpf_cliente, "rg_cliente": rg_cliente,"est_civil_cliente": est_civil_cliente,"tel_cliente":tel_cliente,"formacao_cliente": formacao_cliente,
    "rua":rua,"num":num,"andar":andar,"bloco":bloco,"cidade":cidade,"cep":cep,"estado": estado }).subscribe(data => {
      console.log(data)
    },
    error  => {
    console.log("Error", error);
    });
  }
}
