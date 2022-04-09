import { Input, Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-card',
  templateUrl: './card.component.html',
  styleUrls: ['./card.component.css']
})
export class CardComponent implements OnInit {
  @Input() name: string = "";
  @Input() text: string = "";
  @Input() imgUrl: string = "";
  @Input() usdPrice: string = "";
  @Input() eurPrice: string = "";
  @Input() tixPrice: string = "";
  @Input() manyFaces: boolean = false;
  @Input() secondImgUrl: string = '';
  @Input() secondText: string = '';

  constructor() { }

  ngOnInit(): void {
  }

}
