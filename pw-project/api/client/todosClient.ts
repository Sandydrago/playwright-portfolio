import { BaseClient } from './baseClient';

export class TodosClient extends BaseClient {
  async getTodos() {
    return this.get('/todos');
  }

  async getTodo(id: number) {
    return this.get(`/todos/${id}`);
  }

  async createTodo(todo: any) {
    return this.post('/todos', todo);
  }

  async updateTodo(id: number, todo: any) {
    return this.put(`/todos/${id}`, todo);
  }

  async deleteTodo(id: number) {
    return this.delete(`/todos/${id}`);
  }
}
