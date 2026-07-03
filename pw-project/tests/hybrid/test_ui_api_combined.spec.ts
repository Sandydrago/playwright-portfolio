import { test, expect } from '../../api/apiFixture';
import { HomePage } from '../../pages/home_page';

test('Hybrid Test: API + UI Todo creation', async ({ page, apiClient }) => {
  const home = new HomePage(page);

  // 1. Create a TODO via API (fake API returns a placeholder object)
  const apiTodo = { title: 'API Hybrid Todo', completed: false };
  const createResponse = await apiClient.createTodo(apiTodo);
  const created = await createResponse.json();

  // Assert API responded successfully (but do NOT try to GET it again)
  expect(created).toBeTruthy();
  expect(created.title).toBe('API Hybrid Todo');

  // 2. Navigate to UI (TodoMVC)
  await home.goto();

  // 3. Add a TODO via UI
  await home.addTodo('UI Hybrid Todo');

  // 4. Verify the UI-created TODO appears
  await expect(home.todoItems.first()).toHaveText('UI Hybrid Todo');

  // 5. Cleanup API call (JSONPlaceholder ignores deletes but we call it anyway)
  await apiClient.deleteTodo(created.id);
});

