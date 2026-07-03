import { test, expect } from '@playwright/test';
import { HomePage } from '../../pages/home_page';

test.describe('Smoke Test', () => {

  test('Home page loads @smoke @ui', async ({ page }) => {
    const home = new HomePage(page);

    await home.goto();

    // TodoMVC page title
    await expect(page).toHaveTitle(/TodoMVC/i);

    // Input should be visible
    await expect(home.todoInput).toBeVisible();
  });

  test('basic UI smoke test', async ({ page }) => {
    const home = new HomePage(page);

    await home.goto();

    // Add a simple todo
    await home.addTodo('Smoke Test Todo');

    // Verify it appears
    await expect(home.todoItems.first()).toHaveText('Smoke Test Todo');

    // Footer should now be visible
    await expect(page.locator('.footer')).toBeVisible();
  });

});


