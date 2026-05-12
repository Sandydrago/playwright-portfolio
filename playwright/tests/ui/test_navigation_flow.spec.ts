import { test, expect } from '@playwright/test';
import { HomePage } from '../../src/pages/home_page';
import { NavigationMenu } from '../../src/pages/navigation_menu';

test.describe('Navigation Flow', () => {
  test('should navigate through main menu links', async ({ page }) => {
    const home = new HomePage(page);
    const nav = new NavigationMenu(page);

    await home.goto();

    await nav.goToProducts();
    await expect(page).toHaveURL(/products/);

    await nav.goToUsers();
    await expect(page).toHaveURL(/users/);

    await nav.goToRoles();
    await expect(page).toHaveURL(/roles/);
  });
});
