import { defineConfig } from '@playwright/test';
import { loadConfig } from './utils/configLoader';

const env = process.env.ENV || 'qa';
const configData = loadConfig(env);

export default defineConfig({
  testDir: './tests',
  globalSetup: './global-setup.ts',
  use: {
    baseURL: configData.uiBaseUrl,
    actionTimeout: configData.timeouts.pageLoad,
    trace: 'on-first-retry',
    screenshot: 'only-on-failure',
    video: 'retain-on-failure'
  }
});
