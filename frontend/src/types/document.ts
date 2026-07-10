export interface DocumentMetadata {
  title: string;
  author: string;
  subject: string;
}

export interface DocumentPage {
  page_number: number;
  text: string;
}

export interface Document {
  filename: string;
  page_count: number;
  metadata: DocumentMetadata;
  pages: DocumentPage[];
}