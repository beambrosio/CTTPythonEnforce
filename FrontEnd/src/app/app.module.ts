import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http'
import { FormsModule } from '@angular/forms';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';

import { ProprietariosComponent } from './proprietarios/proprietarios.component';
import { ImoveisComponent } from './imoveis/imoveis.component';
import { ComprasComponent } from './compras/compras.component';
import { GastosComponent } from './gastos/gastos.component';

import { ClientesComponent } from './clientes/clientes.component';
import { NovoClienteComponent } from './novo-cliente/novo-cliente.component';
import { AlteraClienteComponent } from './altera-cliente/altera-cliente.component';
import { HomeComponent } from './home/home.component';
import { NovoProprietarioComponent } from './novo-proprietario/novo-proprietario.component';
import { AlteraProprietarioComponent } from './altera-proprietario/altera-proprietario.component';
import { NovoImovelComponent } from './novo-imovel/novo-imovel.component';
import { AlteraImovelComponent } from './altera-imovel/altera-imovel.component';
import { NovaCompraComponent } from './nova-compra/nova-compra.component';
import { AlteraCompraComponent } from './altera-compra/altera-compra.component';
import { AlteraGastosComponent } from './altera-gastos/altera-gastos.component';
import { NovoGastoComponent } from './novo-gasto/novo-gasto.component';




@NgModule({
  declarations: [
    AppComponent,
    ClientesComponent,
    ProprietariosComponent,
    ImoveisComponent,
    ComprasComponent,
    GastosComponent,
    NovoClienteComponent,
    AlteraClienteComponent,
    HomeComponent,
    NovoProprietarioComponent,
    AlteraProprietarioComponent,
    NovoImovelComponent,
    AlteraImovelComponent,
    NovaCompraComponent,
    AlteraCompraComponent,
    AlteraGastosComponent,
    NovoGastoComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule, 
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
