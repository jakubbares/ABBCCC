import {Component, Input} from '@angular/core';
import {LabelType, Options} from "../ng5-slider/options";


@Component({
  selector: 'fr-date-slider',
  templateUrl: './date-slider.component.html'
})
export class DateSliderComponent {
  @Input() startYear: number;
  @Input() endYear: number;
  dateRange: Date[] = this.createDateRange();
  minValue: number = this.dateRange[0].getTime();
  maxValue: number = this.dateRange[this.dateRange.length - 1].getTime();
  options: Options = {
    draggableRange: true,
    stepsArray: this.dateRange.map((date: Date) => {
      return { value: date.getTime() };
    }),
    translate: (value: number, label: LabelType): string => {
      return new Date(value).toDateString();
    }
  };

  createDateRange(): Date[] {
    const dates: Date[] = [];
    if (!this.endYear) { this.endYear = (new Date()).getFullYear()}
    if (!this.startYear) { this.startYear = this.endYear - 1}
    let year = this.startYear;
    let date = new Date(this.startYear, 1,1);
    while (year <= this.endYear) {
      dates.push(date);
      date.setDate(date.getDate() + 7);
    }
    return dates;
  }
}
