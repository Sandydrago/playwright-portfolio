import fs from 'fs';
import path from 'path';
import { TestData } from './types';

function loadJson(filePath: string) {
  return JSON.parse(fs.readFileSync(filePath, 'utf-8'));
}

export function loadTestData(): TestData {
  const basePath = path.join(__dirname);
  const env = process.env.TEST_ENV || 'dev';
  const overridePath = path.join(basePath, 'overrides', env);

  // Load base files
  const users = loadJson(path.join(basePath, 'users.json'));
  const products = loadJson(path.join(basePath, 'products.json'));
  const roles = loadJson(path.join(basePath, 'roles.json'));
  const testIds = loadJson(path.join(basePath, 'test-ids.json'));

  // Apply overrides if they exist
  const overrideFiles = ['users.json', 'products.json', 'roles.json', 'test-ids.json'];

  for (const file of overrideFiles) {
    const overrideFile = path.join(overridePath, file);
    if (fs.existsSync(overrideFile)) {
      const overrideData = loadJson(overrideFile);

      switch (file) {
        case 'users.json':
          Object.assign(users, overrideData);
          break;
        case 'products.json':
          Object.assign(products, overrideData);
          break;
        case 'roles.json':
          Object.assign(roles, overrideData);
          break;
        case 'test-ids.json':
          Object.assign(testIds, overrideData);
          break;
      }
    }
  }

  return {
    users,
    products,
    roles,
    testIds
  };
}
