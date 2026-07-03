import { test as base } from '@playwright/test';
import { loadConfig } from '../utils/configLoader';

const env = process.env.ENV || 'qa';
const config = loadConfig(env);

export const test = base.extend({
  config: async ({}, use) => {
    await use(config);
  }
});

export const expect = test.expect;