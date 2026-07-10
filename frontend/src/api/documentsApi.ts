import { apiClient } from "./client";
import type { Document } from "../types/document";

export async function uploadDocument(file: File): Promise<Document>  {

    const formData = new FormData();

    formData.append("file", file);

    const response = await apiClient.post(
        "/documents/upload",
        formData,
    );

    return response.data;

}