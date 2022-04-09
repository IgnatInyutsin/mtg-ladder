import { CardObject } from "./card";

export class PageResponseObject {
  constructor(public count:number, public next:string, public previous:string, public results:CardObject[]) {
  }
}
