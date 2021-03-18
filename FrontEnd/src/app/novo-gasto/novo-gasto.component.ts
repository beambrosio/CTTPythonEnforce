import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api.service';

@Component({
  selector: 'app-novo-gasto',
  templateUrl: './novo-gasto.component.html',
  styleUrls: ['./novo-gasto.component.scss']
})
export class NovoGastoComponent implements OnInit {

  constructor(private apiService: ApiService) { }

  ngOnInit(): void {
  }
  insereNovoGasto(luz:string, agua:string, condominio:string){
    this.apiService.postGastos({ "luz":luz , "agua":agua, "condominio": condominio}).subscribe(data => {
      console.log(data)
    },
    error  => {
    console.log("Error", error);
    });
  }

}
