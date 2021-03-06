import {Input, Component, OnInit, ViewEncapsulation} from '@angular/core';

@Component({
  selector: 'app-card',
  templateUrl: './card.component.html',
  styleUrls: ['./card.component.css'],
  encapsulation: ViewEncapsulation.None,
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
  @Input() types: string | string[] = [];
  @Input() manaCost: string | undefined = "";
  firstFace: boolean = true;

  constructor() { }

  ngOnInit(): void {
  }

  toggleFace(): void {
    if (!this.firstFace ) this.firstFace = true
    else this.firstFace = false
  }

}
