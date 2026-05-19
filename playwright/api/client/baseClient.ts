import { APIRequestContext, expect } from '@playwright/test';

export class BaseClient {
  constructor(
    protected request: APIRequestContext,
    protected baseUrl: string
  ) {}

  async get(endpoint: string, options = {}) {
    const response = await this.request.get(`${this.baseUrl}${endpoint}`, options);
    expect(response.ok()).toBeTruthy();
    return response;
  }

  async post(endpoint: string, data: any, options = {}) {
    const response = await this.request.post(`${this.baseUrl}${endpoint}`, {
      data,
      ...options
    });
    expect(response.ok()).toBeTruthy();
    return response;
  }

  async put(endpoint: string, data: any, options = {}) {
    const response = await this.request.put(`${this.baseUrl}${endpoint}`, {
      data,
      ...options
    });
    expect(response.ok()).toBeTruthy();
    return response;
  }

  async delete(endpoint: string, options = {}) {
    const response = await this.request.delete(`${this.baseUrl}${endpoint}`, options);
    expect(response.ok()).toBeTruthy();
    return response;
  }
}