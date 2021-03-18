import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { ApiService } from '../api.service';

@Component({
  selector: 'app-altera-cliente',
  templateUrl: './altera-cliente.component.html',
  styleUrls: ['./altera-cliente.component.scss']
})
export class AlteraClienteComponent implements OnInit {
  cliente:any
  constructor(private activatedRoute: ActivatedRoute, private apiService: ApiService) {
    this.activatedRoute.queryParams.subscribe(params => {
      //console.log(params['id'])
      this.carregaCliente(Number(params['id']))
      });
   }

  ngOnInit(): void {
  }

  carregaCliente(clienteid:number){
    console.log(clienteid);
    this.apiService.getCliente(clienteid).subscribe(data => {
      this.cliente = data;
    },
    error  => {
    console.log("Error", error);
    });
  }

  alteraCliente( clienteid: number, nome_cliente:string, data_nasc_cliente:string, cpf_cliente:string, rg_cliente:number, est_civil_cliente:string, tel_cliente:string,
    formacao_cliente:string, rua:string, num:string, andar:string, bloco:string, cidade:string, cep:string, estado:string){
      
    let cliente = { "nome_cliente":nome_cliente , "data_nasc_cliente":data_nasc_cliente, "cpf_cliente":cpf_cliente, "rg_cliente":rg_cliente, "est_civil_cliente":est_civil_cliente, "tel_cliente":tel_cliente, "formacao_cliente":formacao_cliente,
    "rua":rua, "num":num, "andar":andar, "bloco":bloco,"cep":cep, "cidade":cidade, "estado": estado };
      return this.apiService.putCliente(clienteid,  cliente)
    .subscribe(data => {
      console.log(data)
    });

  }
}

