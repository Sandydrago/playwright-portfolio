import fs from 'fs';
import path from 'path';

export function loadConfig(env: string) {
  const filePath = path.join(__dirname, `../configs/config.${env}.json`);

  if (!fs.existsSync(filePath)) {
    throw new Error(`Config file not found for environment: ${env}`);
  }

  const raw = fs.readFileSync(filePath, 'utf-8');
  return JSON.parse(raw);
}