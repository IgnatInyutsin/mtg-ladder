import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'mana_symbols'
})
export class ManaSymbolsPipe implements PipeTransform {
  transform(value: string[], args?: any): string {
    let result = ""

    for (let i=0; i < value.length; i++) {
      result = result + "{" + value[i] +"}"
    }
    return result
  }
}
