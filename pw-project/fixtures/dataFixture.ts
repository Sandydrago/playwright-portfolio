import { test as base } from '@playwright/test';
import { loadTestData } from '../testdata/dataLoader';

export const test = base.extend({
  testData: async ({}, use) => {
    const users = loadTestData('users.json');
    await use({ users });
  }
});

export const expect = test.expect;