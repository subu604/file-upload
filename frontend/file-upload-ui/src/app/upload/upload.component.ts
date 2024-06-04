import { Component } from '@angular/core';
// import { FileService } from '../../file.service';
import { FileUploadService } from '../file-upload.service';

@Component({
  selector: 'app-upload',
  templateUrl: './upload.component.html',
  styleUrls: ['./upload.component.css'],
})
export class UploadComponent {
  shortLink: string = ''; // Variable to store shortLink from api response
  loading: boolean = false; // Flag variable
  file: File = null; // Variable to store file to Upload

  // Inject service
  constructor(private fileUploadService: FileUploadService) {}

  // On file Select
  onChange(event) {
    this.file = event.target.files[0];
  }

  // OnClick of button Upload
  onUpload() {
    if (this.file) {
      this.loading = !this.loading;
      console.log(this.file);
      this.fileUploadService.uploadFile(this.file).subscribe((event: any) => {
        if (typeof event === 'object') {
          // Short link via api response
          this.shortLink = event.link;
          this.loading = false; // Flag variable
        }
      });
    }
  }
}
