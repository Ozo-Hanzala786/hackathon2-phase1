// Frontend API service for communicating with the backend

const API_BASE_URL = process.env.NEXT_PUBLIC_API_BASE_URL || 'http://localhost:8000';

class ApiService {
  private getToken(): string | null {
    // In a real app, this would come from auth context or localStorage
    return typeof window !== 'undefined' ? localStorage.getItem('authToken') : null;
  }

  private async request(url: string, options: RequestInit = {}) {
    const headers = {
      'Content-Type': 'application/json',
      ...(this.getToken() && { 'Authorization': `Bearer ${this.getToken()}` }),
      ...options.headers,
    };

    const response = await fetch(`${API_BASE_URL}${url}`, {
      ...options,
      headers,
    });

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    return response.json();
  }

  // Authentication methods
  async login(email: string, password: string) {
    // This would be a real login endpoint
    // For now, returning mock data
    return { token: 'mock-token', user: { id: 'user123', email } };
  }

  async signup(email: string, password: string) {
    // This would be a real signup endpoint
    // For now, returning mock data
    return { token: 'mock-token', user: { id: 'user123', email } };
  }

  // Task methods
  async getTasks(userId: string) {
    return this.request(`/api/${userId}/tasks`);
  }

  async createTask(userId: string, taskData: { title: string; description?: string }) {
    return this.request(`/api/${userId}/tasks`, {
      method: 'POST',
      body: JSON.stringify(taskData),
    });
  }

  async updateTask(userId: string, taskId: string, taskData: { title?: string; description?: string; completed?: boolean }) {
    return this.request(`/api/${userId}/tasks/${taskId}`, {
      method: 'PUT',
      body: JSON.stringify(taskData),
    });
  }

  async deleteTask(userId: string, taskId: string) {
    return this.request(`/api/${userId}/tasks/${taskId}`, {
      method: 'DELETE',
    });
  }

  async toggleTaskCompletion(userId: string, taskId: string, completed: boolean) {
    return this.request(`/api/${userId}/tasks/${taskId}/complete`, {
      method: 'PATCH',
      body: JSON.stringify({ completed }),
    });
  }
}

export const apiService = new ApiService();