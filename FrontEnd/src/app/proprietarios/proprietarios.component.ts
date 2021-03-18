import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api.service'; 

@Component({
  selector: 'app-proprietarios',
  templateUrl: './proprietarios.component.html',
  styleUrls: ['./proprietarios.component.scss']
})
export class ProprietariosComponent implements OnInit {
  proprietarios:any;

  constructor(private apiService: ApiService,
    private httpClient : HttpClient) { }

  ngOnInit() {
    this.apiService.getProprietarios().subscribe((data)=>{
      console.log(data);
      this.proprietarios = data; //TODO: Verificar
      console.log(this.proprietarios[0])
    });

  }


}
