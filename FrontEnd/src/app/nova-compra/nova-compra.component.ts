import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api.service';

@Component({
  selector: 'app-nova-compra',
  templateUrl: './nova-compra.component.html',
  styleUrls: ['./nova-compra.component.scss']
})
export class NovaCompraComponent implements OnInit {

  constructor(private apiService: ApiService) { }

  ngOnInit(): void {
  }

  insereNovaCompra(tipo_compra:string, banco_finan:string, preco:string, id_cliente:string, id_imovel:string ){
    this.apiService.postCompras({ "tipo_compra":tipo_compra , "banco_finan":banco_finan, "preco": preco, "id_cliente":id_cliente,"id_imovel":id_imovel  }).subscribe(data => {
      console.log(data)
    },
    error  => {
    console.log("Error", error);
    });
  }
}
