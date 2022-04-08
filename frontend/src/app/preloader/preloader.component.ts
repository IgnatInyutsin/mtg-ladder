import { HostListener, Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-preloader',
  templateUrl: './preloader.component.html',
  styleUrls: ['./preloader.component.css']
})
export class PreloaderComponent implements OnInit {

  loaded = false;

  constructor() { }

  ngOnInit(): void {
  }

  @HostListener('window:load',['$event'])
  onPageLoad(event: Event) {
    this.loaded = true;
  }

}
