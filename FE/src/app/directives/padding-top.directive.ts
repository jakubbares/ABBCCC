import {ElementRef, Directive, AfterContentInit, HostBinding} from '@angular/core';

@Directive({
    selector: '[padding-auto]'
})

export class PaddingAuto implements AfterContentInit {
  @HostBinding('style.padding-top.px') padding: number;

  constructor(public element: ElementRef) {}

  ngAfterContentInit() {
    const { parentNode, clientHeight, innerHTML } = this.element.nativeElement;
    console.log(parentNode.clientHeight, clientHeight, innerHTML)
    this.padding = parentNode.clientHeight - innerHTML.length;
  }
}
