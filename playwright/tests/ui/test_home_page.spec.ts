import { test, expect } from '@playwright/test';
import { HomePage } from '../../src/pages/home_page';

test.describe('Home Page', () => {
  test('should load the home page and display the correct title', async ({ page }) => {
    const home = new HomePage(page);

    await home.goto();
    await expect(page).toHaveTitle(/Home/i);
    await expect(home.header).toBeVisible();
  });
});