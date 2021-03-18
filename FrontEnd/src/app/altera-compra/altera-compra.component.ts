import { stringify } from '@angular/compiler/src/util';
import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { ApiService } from '../api.service';

@Component({
  selector: 'app-altera-compra',
  templateUrl: './altera-compra.component.html',
  styleUrls: ['./altera-compra.component.scss']
})
export class AlteraCompraComponent implements OnInit {
  compra: any
  constructor(private activatedRoute: ActivatedRoute,
    private apiService: ApiService) { 
      this.activatedRoute.queryParams.subscribe(params => {
        //console.log(params['id'])
        this.carregaCompra(Number(params['id']))
        });

    }

  ngOnInit(): void {
  }

  carregaCompra(compraid:number){
    console.log(compraid);
    this.apiService.getCompra(compraid).subscribe(data => {
      this.compra = data;
    },
    error  => {
    console.log("Error", error);
    });
  }

  alteraCompra(compraid: number, tipo_compra:string, banco_finan: string, preco:string, id_cliente:string , id_imovel:string ){
      
    let compra = {"tipo_compra":tipo_compra, "banco_finan": banco_finan, "preco":preco, "id_cliente":id_cliente, "id_imovel":id_imovel};
      return this.apiService.putCompras(compraid,  compra)
    .subscribe(data => {
      console.log(data)
    });
  }


}
