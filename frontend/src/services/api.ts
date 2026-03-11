import { QueryResponse } from "@/types";

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

export const api = {
  async postQuery(query: string, history: { role: string; content: string }[] = []): Promise<QueryResponse> {
    const response = await fetch(`${API_BASE_URL}/query`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ query, history }),
    });

    if (!response.ok) {
      throw new Error("Failed to get response from server");
    }

    return response.json();
  },

  async getHealth(): Promise<any> {
    const response = await fetch(`${API_BASE_URL}/health`);
    if (!response.ok) {
      throw new Error("Health check failed");
    }
    return response.json();
  }
};
