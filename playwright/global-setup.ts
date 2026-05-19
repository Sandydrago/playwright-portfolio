import { FullConfig } from '@playwright/test';
import { loadConfig } from './utils/configLoader';

async function globalSetup(config: FullConfig) {
  const env = process.env.ENV || 'qa';
  const loaded = loadConfig(env);

  console.log(`\n🔧 Running tests in environment: ${loaded.envName}`);
  console.log(`🌐 UI Base URL: ${loaded.uiBaseUrl}`);
  console.log(`🔗 API Base URL: ${loaded.apiBaseUrl}\n`);
}

export default globalSetup;