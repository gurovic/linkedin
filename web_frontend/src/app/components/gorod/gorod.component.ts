import { Component } from '@angular/core';
import { DomSanitizer, SafeResourceUrl } from '@angular/platform-browser';

@Component({
  selector: 'app-gorod',
  templateUrl: './gorod.component.html',
  styleUrls: ['./gorod.component.css']
})
export class GorodComponent {
  UnityGameUrl = 'assets/web/index.html';
  sanitizedUnityGameUrl: SafeResourceUrl;

  constructor(private sanitizer: DomSanitizer) {
    this.sanitizedUnityGameUrl = this.sanitizer.bypassSecurityTrustResourceUrl(this.UnityGameUrl);
  }
}