import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LoginComponent } from './login/login.component';
import { UploadComponent } from './upload/upload.component';
import { FilesComponent } from './files/files.component';

const routes: Routes = [
  { path: 'login', component: LoginComponent },
  { path: 'upload', component: UploadComponent },
  { path: 'files', component: FilesComponent },
  { path: '', redirectTo: '/login', pathMatch: 'full' },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
