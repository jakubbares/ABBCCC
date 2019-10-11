import {ModuleWithProviders} from "@angular/core";
import {RouterModule, Routes} from "@angular/router";
import {UserComponent} from "./pages/user/user.component";
import {HeatmapChart} from "./components/heatmap/heatmap.chart";
import {LeafletDemoComponent} from "./components/leaflet/leaflet-demo.component";


export const router: Routes = [
  { path: '', redirectTo: 'heat', pathMatch: 'full' },
  { path: 'user', component: UserComponent },
  { path: 'heat', component: HeatmapChart },
  { path: 'map', component: LeafletDemoComponent },
  { path: '**', redirectTo: 'heat' }
];

export const routes: ModuleWithProviders = RouterModule.forRoot(router);
