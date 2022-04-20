import { HostListener, Component, OnInit, Input, Directive, TemplateRef, ViewContainerRef } from '@angular/core';
import { CardsComponent } from '../cards/cards.component'
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
  onPageLoad(event: any) {
    document.body.style.overflow = "auto"
    this.loaded = true;
  }
}
