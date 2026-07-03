import { Page, Locator } from '@playwright/test';
import { loadConfig } from '../utils/configLoader';

export class HomePage {
  readonly page: Page;
  readonly url: string;

  // TodoMVC elements
  readonly todoInput: Locator;
  readonly todoItems: Locator;
  readonly filterAll: Locator;
  readonly filterActive: Locator;
  readonly filterCompleted: Locator;

  constructor(page: Page) {
    this.page = page;

    const env = loadConfig();
    this.url = env.uiBaseUrl; // TodoMVC has no /home route

    // Selectors based on TodoMVC DOM
    this.todoInput = page.locator('.new-todo');
    this.todoItems = page.locator('.todo-list li');
    this.filterAll = page.getByRole('link', { name: 'All' });
    this.filterActive = page.getByRole('link', { name: 'Active' });
    this.filterCompleted = page.getByRole('link', { name: 'Completed' });
  }

  async goto() {
    await this.page.goto(this.url);
  }

  async addTodo(text: string) {
    await this.todoInput.fill(text);
    await this.todoInput.press('Enter');
  }
}