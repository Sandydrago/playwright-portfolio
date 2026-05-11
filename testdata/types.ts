export interface UserData {
  username: string;
  password: string;
  email: string;
}

export interface ProductData {
  id: number;
  name: string;
  price: number;
}

export interface RoleData {
  permissions: string[];
}

export interface TestIds {
  [key: string]: string;
}

export interface TestData {
  users: Record<string, UserData>;
  products: Record<string, ProductData>;
  roles: Record<string, RoleData>;
  testIds: TestIds;
}
