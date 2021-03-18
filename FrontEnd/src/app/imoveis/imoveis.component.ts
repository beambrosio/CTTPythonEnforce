import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api.service';



@Component({
  selector: 'app-imoveis',
  templateUrl: './imoveis.component.html',
  styleUrls: ['./imoveis.component.scss']
})
export class ImoveisComponent implements OnInit {
  imoveis:any;
  constructor(private apiService: ApiService,
    private httpClient : HttpClient) { }


  ngOnInit() {
    this.apiService.getImoveis().subscribe((data)=>{
      console.log(data);
      this.imoveis = data; //TODO: Verificar
      console.log(this.imoveis[0])
    });
  }

}
