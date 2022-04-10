import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import {FormsModule} from "@angular/forms";
import {Routes, RouterModule} from '@angular/router';

import { AppComponent } from './app.component';
import { HeaderComponent } from './header/header.component';
import { HomeComponent } from './home/home.component';
import { RegistrationComponent } from './registration/registration.component';
import { LoginComponent } from './login/login.component';
import { PreloaderComponent } from './preloader/preloader.component';
import { CardsComponent } from './cards/cards.component';
import { HttpClientModule }   from '@angular/common/http';
import { CardComponent } from './card/card.component';
import {CardTextPipe} from "./card-text.pipe";
import {ManaSymbolsPipe} from "./mana-symbols.pipe";

// определение маршрутов
const appRoutes: Routes =[
  { path: '', component: HomeComponent},
  { path: 'registration', component: RegistrationComponent},
  { path: 'login', component: LoginComponent},
  { path: 'cards', component: CardsComponent},
];


@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent,
    HomeComponent,
    RegistrationComponent,
    LoginComponent,
    PreloaderComponent,
    CardsComponent,
    CardComponent,
    CardTextPipe,
    ManaSymbolsPipe
  ],
  imports: [
    BrowserModule,
    FormsModule,
    RouterModule.forRoot(appRoutes),
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
