import {RuleObject} from "./rule";


export class CardObject {
  constructor(public id:number,
              public scryfall_id:string = '',
              public name:string,
              public text:string = '',
              public colors:[],
              public types:[] | string,
              public mana_value:number | undefined,
              public mana_cost:string = "",
              public power:string = '',
              public toughness:string = '',
              public loyalty:string = '',
              public rules:RuleObject[],
              public imgUrl:string = '',
              public usdPrice:string = 'Неизвестно',
              public eurPrice:string = 'Неизвестно',
              public tixPrice:string = 'Неизвестно',
              public manyFaces:boolean = false,
              public secondImgUrl:string = '',
              public secondText:string = '') {}

}
