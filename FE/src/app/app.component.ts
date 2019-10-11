import {Component, HostListener} from '@angular/core';
import {Router} from "@angular/router";
import {AuthenticationService} from "./services/authentication.service";



@Component({
  selector: 'app-root',
  templateUrl: './app.component.html'
})
export class AppComponent {
  print = false;

  @HostListener('document:keydown.escape', ['$event'])
  onKeydownHandler(event: KeyboardEvent) {
    this.print = !this.print;
  }

  constructor(private router: Router,
              public authService: AuthenticationService) {
  }
}
