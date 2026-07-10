import { apiClient } from "./client";
import type { ChatResponse } from "../types/chat";

export async function askQuestion(
  question: string
): Promise<ChatResponse> {

  const response = await apiClient.post<ChatResponse>(
    "/chat/ask",
    {
      question,
    }
  );

  return response.data;
}