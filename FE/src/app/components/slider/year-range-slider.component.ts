import { Component } from '@angular/core';
import {Options} from "../ng5-slider/options";


@Component({
  selector: 'fr-year-range-slider',
  templateUrl: './year-range-slider.component.html'
})
export class YearRangeSliderComponent {
  minValue: number = (new Date()).getFullYear() - 10;
  maxValue: number = (new Date()).getFullYear();
  options: Options = {
    floor: (new Date()).getFullYear() - 20,
    ceil: (new Date()).getFullYear(),
    step: 1,
    draggableRange: true
  };
}
