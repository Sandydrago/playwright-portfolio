import fs from 'fs';
import path from 'path';

export function loadTestData(fileName: string) {
  const filePath = path.join(__dirname, fileName);

  if (!fs.existsSync(filePath)) {
    throw new Error(`Test data file not found: ${fileName}`);
  }

  const raw = fs.readFileSync(filePath, 'utf-8');
  return JSON.parse(raw);
}