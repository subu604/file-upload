import { Component } from '@angular/core';
import { AuthService } from '../../auth.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css'],
})
export class LoginComponent {
  username: any;
  password: any;

  constructor(private authService: AuthService, private router: Router) {}

  login(): void {
    this.authService
      .login(this.username, this.password)
      .subscribe((response) => {
        this.authService.setToken(response.access_token);
        this.router.navigate(['/files']);
      });
  }
}
