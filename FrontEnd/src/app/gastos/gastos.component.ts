import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { ApiService } from '../api.service';

@Component({
  selector: 'app-gastos',
  templateUrl: './gastos.component.html',
  styleUrls: ['./gastos.component.scss']
})
export class GastosComponent implements OnInit {
  gastos:any;

  constructor(private apiService: ApiService,
    private httpClient : HttpClient) { }

  ngOnInit(): void {
    this.apiService.getGastos().subscribe((data)=>{
      console.log(data);
      this.gastos = data; //TODO: Verificar
      console.log(this.gastos[0])
    });
  }

}
