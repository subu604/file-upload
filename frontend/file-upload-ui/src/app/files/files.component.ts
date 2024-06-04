import { Component } from '@angular/core';
import { FileService } from '../../file.service';

@Component({
  selector: 'app-files',
  templateUrl: './files.component.html',
  styleUrls: ['./files.component.css'],
})
export class FilesComponent {
  path: any;
  filename: any;
  version: any;
  fileContent: any;

  constructor(private fileService: FileService) {}

  getFile(): void {
    this.fileService
      .getFile(this.path, this.filename, this.version)
      .subscribe((response) => {
        this.fileContent = response.content;
      });
  }
}
