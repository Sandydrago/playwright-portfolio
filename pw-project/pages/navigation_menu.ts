import { Page, Locator } from '@playwright/test';

export class NavigationMenu {
  readonly page: Page;
  readonly productsLink: Locator;
  readonly usersLink: Locator;
  readonly rolesLink: Locator;

  constructor(page: Page) {
    this.page = page;

    this.productsLink = page.getByTestId('nav-products');
    this.usersLink = page.getByTestId('nav-users');
    this.rolesLink = page.getByTestId('nav-roles');
  }

  async goToProducts() {
    await this.productsLink.click();
  }

  async goToUsers() {
    await this.usersLink.click();
  }

  async goToRoles() {
    await this.rolesLink.click();
  }
}

