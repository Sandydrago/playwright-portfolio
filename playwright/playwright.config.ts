import { defineConfig } from '@playwright/test';
import { loadConfig } from './src/config/config';

const envConfig = loadConfig();
/* console.log("Loaded environment:", envConfig.envName, envConfig.ui.baseURL); */


export default defineConfig({
  use: {
    baseURL: envConfig.ui.baseURL,
    trace: 'retain-on-failure',
    screenshot: 'only-on-failure',
    video: 'retain-on-failure'
  },
  reporter: [
    ['html', { open: 'never' }],
    ['list']
  ]
});
