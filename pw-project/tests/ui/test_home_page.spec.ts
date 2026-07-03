import { test, expect } from '@playwright/test';
import { HomePage } from '../../pages/home_page';

test.describe('TodoMVC Home Page', () => {

  test('Home page loads', async ({ page }) => {
    const home = new HomePage(page);

    await home.goto();

    // TodoMVC page title
    await expect(page).toHaveTitle(/TodoMVC/i);

    // Input should be visible
    await expect(home.todoInput).toBeVisible();

   });

});
