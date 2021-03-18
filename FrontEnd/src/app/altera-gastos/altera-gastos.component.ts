import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { ApiService } from '../api.service';

@Component({
  selector: 'app-altera-gastos',
  templateUrl: './altera-gastos.component.html',
  styleUrls: ['./altera-gastos.component.scss']
})
export class AlteraGastosComponent implements OnInit {
  gasto:any
  constructor(private activatedRoute: ActivatedRoute,
    private apiService: ApiService) { 
      this.activatedRoute.queryParams.subscribe(params => {
        //console.log(params['id'])
        this.carregaGasto(Number(params['id']))
        });
  }
  ngOnInit(): void {
  }

  carregaGasto(gastoid:number){
    console.log(gastoid);
    this.apiService.getCompra(gastoid).subscribe(data => {
      this.gasto = data;
    },
    error  => {
    console.log("Error", error);
    });
  }

  alteraGasto(gastoid:number, luz:string, agua: string, condominio:string){
      
    let gasto = {"luz":luz, "agua": agua, "conodminio":condominio};
      return this.apiService.putCompras(gastoid,  gasto)
    .subscribe(data => {
      console.log(data)
    });
  }

}
