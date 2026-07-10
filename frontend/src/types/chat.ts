export interface RetrievedChunk {
  chunk_id: string;
  document_filename: string;
  page_number: number;
  chunk_number: number;
  text: string;
  distance: number;
}

export interface ChatResponse {
  answer: string;
  sources: RetrievedChunk[];
}