import fs from 'fs';
import path from 'path';

export function loadConfig() {
  // Always default to 'qa' if ENV is missing
  const env = process.env.ENV || 'qa';

  const filePath = path.join(__dirname, `../configs/config.${env}.json`);

  if (!fs.existsSync(filePath)) {
    throw new Error(`Config file not found for environment: ${env}`);
  }

  const raw = fs.readFileSync(filePath, 'utf-8');
  return JSON.parse(raw);
}
