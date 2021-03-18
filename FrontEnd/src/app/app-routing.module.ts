import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import {ClientesComponent} from './clientes/clientes.component'
import { NovoClienteComponent } from './novo-cliente/novo-cliente.component'
import { AlteraClienteComponent} from './altera-cliente/altera-cliente.component'
import { HomeComponent } from './home/home.component';
import { ProprietariosComponent } from './proprietarios/proprietarios.component';
import { NovoProprietarioComponent } from './novo-proprietario/novo-proprietario.component';
import { AlteraProprietarioComponent } from './altera-proprietario/altera-proprietario.component';
import { ImoveisComponent } from './imoveis/imoveis.component';
import { NovoImovelComponent } from './novo-imovel/novo-imovel.component';
import { AlteraImovelComponent } from './altera-imovel/altera-imovel.component';
import { ComprasComponent } from './compras/compras.component';
import { NovaCompraComponent } from './nova-compra/nova-compra.component';
import { AlteraCompraComponent } from './altera-compra/altera-compra.component';
import { componentFactoryName } from '@angular/compiler';
import { GastosComponent } from './gastos/gastos.component';
import { NovoGastoComponent } from './novo-gasto/novo-gasto.component';
import { AlteraGastosComponent } from './altera-gastos/altera-gastos.component';

const routes: Routes = [
  
  {path: 'clientes', component: ClientesComponent },
  {path: 'novo-cliente', component: NovoClienteComponent},
  {path: 'altera-cliente', component: AlteraClienteComponent},
  
  {path: 'proprietarios', component: ProprietariosComponent },
  {path: 'novo-proprietario', component: NovoProprietarioComponent},
  {path: 'altera-proprietario', component: AlteraProprietarioComponent},

  {path: 'imoveis', component: ImoveisComponent },
  {path: 'novo-imovel', component: NovoImovelComponent},
  {path: 'altera-imovel', component: AlteraImovelComponent},

  {path: 'compras', component: ComprasComponent},
  {path: 'nova-compra', component: NovaCompraComponent},
  {path: 'altera-compra', component: AlteraCompraComponent},
  
  {path: 'gastos', component: GastosComponent},
  {path: 'novo-gasto', component: NovoGastoComponent},
  {path: 'altera-gastos', component: AlteraGastosComponent},

  {path: '**', redirectTo:'home', pathMatch: 'full'},
  {path: 'home', component: HomeComponent},

];
@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
