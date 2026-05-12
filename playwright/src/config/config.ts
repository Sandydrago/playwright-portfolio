import fs from 'fs';
import path from 'path';

export interface EnvConfig {
  envName: string;
  ui: {
    baseURL: string;
  };
  api: {
    baseURL: string;
    auth: {
      login: string;
      refresh: string;
    };
    users: {
      getUser: string;
      listUsers: string;
    };
  };
}

export function loadConfig(): EnvConfig {
  const env = process.env.TEST_ENV || 'dev';

  // FIXED PATH
  const filePath = path.join(__dirname, '../../config', `${env}.json`);

  if (!fs.existsSync(filePath)) {
    throw new Error(`Config file not found for environment: ${env}`);
  }

  const raw = fs.readFileSync(filePath, 'utf-8');
  return JSON.parse(raw) as EnvConfig;
}
