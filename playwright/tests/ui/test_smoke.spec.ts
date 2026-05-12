import { test, expect } from '@playwright/test';
import { HomePage } from '../../src/pages/home_page';

test.describe('Smoke Test', () => {
  test('basic UI smoke test', async ({ page }) => {
    const home = new HomePage(page);

    await home.goto();
    await expect(home.header).toBeVisible();
    await expect(page).toHaveTitle(/Home/i);
  });
});
