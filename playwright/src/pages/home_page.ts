import { Page, Locator } from '@playwright/test';
import { loadConfig } from '../config/config';

export class HomePage {
  readonly page: Page;
  readonly header: Locator;
  readonly url: string;

  constructor(page: Page) {
    this.page = page;

    const env = loadConfig();
    this.url = `${env.ui.baseURL}/home`;

    this.header = page.getByTestId('header-title');
  }

  async goto() {
    await this.page.goto(this.url);
  }
}