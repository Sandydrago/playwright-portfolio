import { test as base } from '@playwright/test';
import { TodosClient } from './client/todosClient';
import { loadConfig } from '../utils/configLoader';

const env = process.env.ENV || 'qa';
const config = loadConfig(env);

export const test = base.extend({
  apiClient: async ({ request }, use) => {
    const client = new TodosClient(request, config.apiBaseUrl);
    await use(client);
  }
});

export const expect = test.expect;
