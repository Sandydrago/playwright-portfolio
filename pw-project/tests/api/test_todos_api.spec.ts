import { test, expect } from '../../api/apiFixture';

test('GET todos returns a list', async ({ apiClient }) => {
  const response = await apiClient.getTodos();
  const data = await response.json();

  expect(Array.isArray(data)).toBe(true);
  expect(data.length).toBeGreaterThan(0);
});