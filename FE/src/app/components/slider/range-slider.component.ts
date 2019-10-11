import {Component, EventEmitter, Input, OnInit, Output} from '@angular/core';
import {Options} from "../ng5-slider/options";


@Component({
  selector: 'eh-range-slider',
  templateUrl: './range-slider.component.html',
  styleUrls: ['custom-slider.component.scss']
})
export class RangeSliderComponent implements OnInit {
  @Input() minOfRange: number = 0;
  @Input() topOfRange: number = 1;
  @Input() bottomValue: number;
  @Input() topValue: number;
  @Input() step: number = 1;
  @Output() bottomValueChange = new EventEmitter();
  @Output() topValueChange = new EventEmitter();
  options: Options = {
    floor: this.minOfRange,
    ceil: this.topOfRange,
    step:  this.step,
    draggableRange: true,
    precision: 2
  };

  ngOnInit() {
    this.options.ceil = this.topOfRange > 1 ? this.topOfRange : 1;
    this.options.floor = this.minOfRange;
    this.options.step = this.step;
  }
  // showTicks: true

  setBottomValue(value) {
    this.bottomValue= value;
  }

  setTopValue(value) {
    this.topValue = value;
  }

  bottomValChange(event) {
    this.bottomValueChange.emit(event);
  }

  topValChange(event) {
    this.topValueChange.emit(event);
  }
}
