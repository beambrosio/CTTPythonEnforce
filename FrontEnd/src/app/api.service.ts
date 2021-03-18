import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { FormsModule, NgForm } from '@angular/forms';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  //public baseUrl='http://127.0.0.1:5000/';

  constructor(private httpClient: HttpClient) { }


  //metodos de Cliente
  public getClientes(){
    return this.httpClient.get(`http://127.0.0.1:5000/Cliente/getcli`);
  }
  public getCliente(idcliente:any){
    return this.httpClient.get(`http://127.0.0.1:5000/Cliente/getid/${idcliente}`);
  }
  public postCliente(cliente:any){
    return this.httpClient.post(`http://127.0.0.1:5000/Cliente/postcli`, cliente);
  }

  public putCliente(idcliente: number, cliente: any){
    return this.httpClient.put(`http://127.0.0.1:5000/Cliente/put/${idcliente}`, cliente);
  }


  //metodos de Proprietarios
  public getProprietarios(){
    return this.httpClient.get(`http://127.0.0.1:5000/Proprietarios/getprop`);
  }
  
  public getProprietario(idprop:any){
    return this.httpClient.get(`http://127.0.0.1:5000/Proprietarios/getid/${idprop}`);
  }
  
  public postProprietario(proprietario:any){
    return this.httpClient.post(`http://127.0.0.1:5000/Proprietarios/postprop`, proprietario);
  }

  public putProprietario(idprop: number, proprietario: any){
    return this.httpClient.put(`http://127.0.0.1:5000/Proprietarios/put/${idprop}`, proprietario);
  }

  //metodos de Imoveis
  public getImoveis(){
    return this.httpClient.get(`http://127.0.0.1:5000/Imoveis/getimov`);
  }
  public getImovel(idimov:any){
    return this.httpClient.get(`http://127.0.0.1:5000/Imoveis/getid/${idimov}`);
  }

  public postImoveis(imovel:any){
    return this.httpClient.post(`http://127.0.0.1:5000/Imoveis/postimov`, imovel);
  }

  public putImoveis(idimov: number, imovel: any){
    return this.httpClient.put(`http://127.0.0.1:5000/Imoveis/put/${idimov}`, imovel);
  }

  //metodos de Compras
  public getCompras(){
    return this.httpClient.get(`http://127.0.0.1:5000/Compra/getcompra`);
  }
  public getCompra(idcompra:any){
    return this.httpClient.get(`http://127.0.0.1:5000/Compra/getid/${idcompra}`);
  }

  public postCompras(compra:any){
    return this.httpClient.post(`http://127.0.0.1:5000/Compra/postcompra`, compra);
  }

  public putCompras(idcompra: number, compra: any){
    return this.httpClient.put(`http://127.0.0.1:5000/Compra/put/${idcompra}`, compra);
  }

  //metodos de Gastos
  public getGastos(){
    return this.httpClient.get(`http://127.0.0.1:5000/Gastos/get`);
  }
  public getGasto(idgasto:any){
    return this.httpClient.get(`http://127.0.0.1:5000/Gastos/getid/${idgasto}`);
  }

  public postGastos(gasto:any){
    return this.httpClient.post(`http://127.0.0.1:5000/Gastos/post`, gasto);
  }

  public putGastos(idgasto: number, gasto: any){
    return this.httpClient.put(`http://127.0.0.1:5000/Gastos/put/${idgasto}`, gasto);
  }

}
