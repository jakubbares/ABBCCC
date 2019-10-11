import {BrowserModule} from '@angular/platform-browser';
import {NgModule} from '@angular/core';
import {FormsModule} from '@angular/forms';
import {AppComponent} from './app.component';
import {routes} from './app.routes';
import {AuthGuard} from './guards/auth.guard';
import {AuthenticationService} from './services/authentication.service';
import {UserComponent} from './pages/user/user.component';

import {MultiSelectModule} from 'primeng/multiselect';
import {BrowserAnimationsModule} from '@angular/platform-browser/animations';
import {TableModule} from 'primeng/table';
import {DropdownModule} from 'primeng/dropdown';
import {ButtonModule} from 'primeng/button';
import {AutoCompleteModule, MessagesModule} from 'primeng/primeng';
import {PlayerSortPipe, SortMulStringPipe, SortPipe, SortStringPipe} from './pipes/sort.pipe';
import {FilterPipe} from './pipes/filter.pipe';
import {DataService} from './services/data.service';
import {SharedModule} from './shared.module';
import {HttpClientModule} from '@angular/common/http';
import {HeatmapChart} from './components/heatmap/heatmap.chart';
import {LeafletDemoModule} from "./components/leaflet/leaflet-demo.module";


@NgModule({
  imports: [
    SharedModule,
    BrowserModule,
    LeafletDemoModule,
    BrowserAnimationsModule,
    FormsModule,
    MessagesModule,
    HttpClientModule,
    MultiSelectModule,
    DropdownModule,
    TableModule,
    AutoCompleteModule,
    ButtonModule,
    routes
  ],
  declarations: [
    HeatmapChart,
    AppComponent,
    UserComponent,
    FilterPipe,
    PlayerSortPipe,
    SortStringPipe,
    SortMulStringPipe,
    SortPipe
  ],
  providers: [
    AuthGuard,
    DataService,
    AuthenticationService,
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
