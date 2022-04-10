import {Component, OnInit} from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { RestApiConnector } from '../../assets/connectors/restapi';
import {PageResponseObject} from "../../assets/models/page_response";
import { map, catchError } from "rxjs/operators";

@Component({
  selector: 'app-cards',
  templateUrl: './cards.component.html',
  styleUrls: ['./cards.component.css']
})
export class CardsComponent implements OnInit {
  rest: RestApiConnector = new RestApiConnector();
  cardsPull: PageResponseObject = new PageResponseObject(0, "", "", []);
  actualPage: number = 1
  previousPage: boolean = false
  nextPage: boolean = true
  myPage: number = 1
  ERROR_MESSAGE_404: boolean = false

  constructor(private http: HttpClient) {
  }

  ngOnInit(): void {
    // при создании страницы делаем http запрос для сбора карт с первой страницы
    this.http.get(this.rest.restapiUrl + "cards/").subscribe((data:any) => {
      // сбор данных с scryfall api
      this.cardsPull = this.getImageAndPrices(data);
    });
  }

  getImageAndPrices(data : any) : any {
    // проверяем возможность перейти на страницу вперед/назад
    if (data.next != null) this.nextPage = true; else this.nextPage = false;
    if (data.previous != null) this.previousPage = true; else this.previousPage = false;

    // сбор данных с scryfall api
    for (let i=0; i<data.results.length; i++) {
      this.http.get("https://api.scryfall.com/cards/oracle/" + data.results[i].scryfall_id).subscribe( (response:any) => {
        // если карточка односторонняя
        if (response.data[0].card_faces == undefined) {
          data.results[i].manyFaces = false;
          data.results[i].imgUrl = response.data[0].image_uris.png;
        } else { // иначе добавляем второй текст и картинки
          data.results[i].manyFaces = true;
          data.results[i].imgUrl = response.data[0].card_faces[0].image_uris.png;
          data.results[i].secondImgUrl = response.data[0].card_faces[1].image_uris.png;
          data.results[i].secondText = response.data[0].card_faces[1].oracle_text;
        }
        // заполнение полей с ценами
        if (response.data[0].prices.usd != null) data.results[i].usdPrice = response.data[0].prices.usd;
        else data.results[i].usdPrice = "НЕИЗВЕСТНО";
        if (response.data[0].prices.eur != null) data.results[i].eurPrice = response.data[0].prices.eur;
        else data.results[i].eurPrice = "НЕИЗВЕСТНО";
        if (response.data[0].prices.tix != null) data.results[i].tixPrice = response.data[0].prices.tix;
        else data.results[i].tixPrice = "НЕИЗВЕСТНО";
      });
    }
    return data;
  }

  nextPageGo() : void {
    // перемещаем скролл в верх страницы
    window.scrollTo(0, 0);
    // страница +1
    this.actualPage += 1;
    // сбор карт с актуальной страницы
    this.http.get(this.rest.restapiUrl + "cards/", {params:
        {
          page: this.actualPage
        }
    }).subscribe((data:any) => {
      // отключаем сообщение с ошибкой
      this.ERROR_MESSAGE_404 = false;
      // сбор данных с scryfall api
      this.cardsPull = this.getImageAndPrices(data);
    });
  }

  previousPageGo() : void {
    // перемещаем скролл в верх страницы
    window.scrollTo(0, 0);
    // страница -1
    this.actualPage -= 1;
    // сбор карт с актуальной страницы
    this.http.get(this.rest.restapiUrl + "cards/", {
      params:
        {
          page: this.actualPage
        }
    }).subscribe((data:any) => {
      // отключаем сообщение с ошибкой
      this.ERROR_MESSAGE_404 = false;
      // сбор данных с scryfall api
      this.cardsPull = this.getImageAndPrices(data);
    });
  }

  choicePageGo() : void {
    // собираем данные из формы
    this.actualPage = this.myPage;
    window.scrollTo(0, 0);
    // сбор карт с актуальной страницы
    this.http.get(this.rest.restapiUrl + "cards/", {
      params:
        {
          page: this.actualPage
        }
    }).subscribe((data:any) => {
      // отключаем сообщение с ошибкой
      this.ERROR_MESSAGE_404 = false;
      // собираем данные со scryfallapi
      this.cardsPull = this.getImageAndPrices(data);
    }, error => { // обработка ошибок
      if (error.status == 404) { // если такой страницы нет - сообщение с ошибкой
        this.cardsPull.results = []
        this.ERROR_MESSAGE_404 = true;
        this.previousPage = false;
        this.nextPage = false;
      }
    });
  }
}
