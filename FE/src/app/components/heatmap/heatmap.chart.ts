import {AfterViewInit, Component, ElementRef, HostListener, Input, OnChanges, ViewChild} from '@angular/core';
import simpleheat from './simpleheat';
import {scale} from "../../shared/shared.functions";
import {ChartService} from "../../services/chart.service";

@Component({
  selector: 'eh-heatmap-chart',
  template: `
      <leafletDemo></leafletDemo>
      <canvas #canvas id="canvas" [width]="width" [height]="height"></canvas>
  `,
  styleUrls: ['heatmap.chart.scss']
})
export class HeatmapChart implements AfterViewInit, OnChanges {
  width = 771;
  height = 519;
  data: any[] = [];
  @Input() name: string;
  @Input() club: any;
  @Input() match: any;
  @Input() max: number;
  @Input() radius = 10;
  @Input() blur = 12;
  @ViewChild('canvas') canvas: ElementRef;
  heat: any;


  constructor(
    private chartService: ChartService,
  ) {
    window['heat'] = this;
  }


  ngAfterViewInit() {
    this.render();
  }

  ngOnChanges() {
    this.render();
  }


  draw() {
    let data = this.data;
    const max = this.max ? this.max : data.reduce((highest, current) => current[2] > highest ? current[2] : highest, 0);
    data = data.map(a => [scale(a.coor[0], 105, this.width), this.height - scale(a.coor[1], 68, this.height), a.coor[2]]);
    this.heat.data(data).max(max).draw();
  }

  render() {
    this.chartService.getHeatMap('defense', this.match.match_instatid, this.club.instatid, (players, data) => {
      this.data = data;
      this.canvas.nativeElement.getContext('2d').clearRect(0, 0, this.width, this.height);
      if (data.length === 0) return;
      this.heat = simpleheat(this.canvas.nativeElement).radius(this.radius, this.blur);
      this.draw();
    });
  }
}
