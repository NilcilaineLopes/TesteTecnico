import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ClientCadastroComponent } from './components/client-cadastro/client-cadastro.component';
import { ClientFormComponent } from './components/client-form/client-form.component';
import { ClientListComponent } from './components/client-list/client-list.component';

const routes: Routes = [
  {path: '', component: ClientListComponent },
  {path: 'pessoa', component: ClientFormComponent },
  {path: 'pessoa/cadastrar', component: ClientCadastroComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
