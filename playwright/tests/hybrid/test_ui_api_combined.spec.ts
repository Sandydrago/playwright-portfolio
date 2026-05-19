import { test, expect } from '../../api/apiFixture';

test('Create TODO via API and verify in UI', async ({ page, apiClient }) => {
  // 1. Create data via API
  const newTodo = { title: 'Hybrid Test Todo', completed: false };
  const createResponse = await apiClient.createTodo(newTodo);
  const created = await createResponse.json();

  // 2. Navigate to UI
  await page.goto('/todos');

  // 3. Verify the new TODO appears
  await expect(page.getByText(created.title)).toBeVisible();

  // 4. Clean up via API
  await apiClient.deleteTodo(created.id);
});