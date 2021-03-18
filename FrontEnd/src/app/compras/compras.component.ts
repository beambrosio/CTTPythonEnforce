import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api.service';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-compras',
  templateUrl: './compras.component.html',
  styleUrls: ['./compras.component.scss']
})
export class ComprasComponent implements OnInit {
  compras:any;
  constructor(private apiService: ApiService,
    private httpClient : HttpClient) { }

  ngOnInit(): void {

    this.apiService.getCompras().subscribe((data)=>{
      console.log(data);
      this.compras = data; //TODO: Verificar
      console.log(this.compras[0])
    });

  }

}
