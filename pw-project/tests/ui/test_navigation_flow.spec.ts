import { test, expect } from '@playwright/test';
import { HomePage } from '../../pages/home_page';

test.describe('TodoMVC Navigation Flow (Filters)', () => {

  test('should navigate through All, Active, and Completed filters', async ({ page }) => {
    const home = new HomePage(page);

    await home.goto();

    // Add three todos
    await home.addTodo('Task 1');
    await home.addTodo('Task 2');
    await home.addTodo('Task 3');

    // Complete Task 2
    await page.locator('li', { hasText: 'Task 2' }).locator('input.toggle').check();


    // 1. All filter
    await home.filterAll.click();
    await expect(home.todoItems).toHaveCount(3);

    // 2. Active filter
    await home.filterActive.click();
    await expect(home.todoItems).toHaveCount(2); // Task 1 + Task 3

    // 3. Completed filter
    await home.filterCompleted.click();
    await expect(home.todoItems).toHaveCount(1); // Task 2
  });

});
