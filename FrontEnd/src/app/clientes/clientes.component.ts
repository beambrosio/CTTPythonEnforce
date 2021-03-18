import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api.service';

@Component({
  selector: 'app-clientes',
  templateUrl: './clientes.component.html',
  styleUrls: ['./clientes.component.scss']
})
export class ClientesComponent implements OnInit {
  clientes:any;

  constructor(private apiService: ApiService,
            private httpClient : HttpClient) { }

  ngOnInit() {
    this.apiService.getClientes().subscribe((data)=>{
      console.log(data);
      this.clientes = data; //TODO: Verificar
      console.log(this.clientes[0])
    });

  }
}  
  