
#  **SDET Portfolio — Python API + Playwright UI/API Automation**

Welcome to my SDET automation portfolio.  
I built this repository to demonstrate my ability to design **real-world, scalable, and maintainable automation frameworks** across both backend (API) and frontend (UI) layers.

This portfolio contains two complete automation projects:

- A **Python API testing framework** with a custom Petstore API client  
- A **Playwright UI/API hybrid testing framework** using modern best practices  

My goal is to show not just that I can write tests, but that I can **architect automation systems** the way real engineering teams expect.

---

# ⭐ **Table of Contents**

```
1. Python API Automation Framework
   1. Overview
   2. Tech Stack
   3. Folder Structure
   4. How to Install & Run Tests
   5. API Client Overview
   6. Test Suite Overview
   7. HTML Reporting (Optional)
   8. Why This Project Matters
   9. Future Enhancements

2. Playwright UI/API Hybrid Framework
   1. Overview
   2. Tech Stack
   3. Folder Structure
   4. Page Object Model (POM)
   5. Fixtures
   6. Hybrid UI + API Testing
   7. Trace Viewer Integration
   8. Why This Project Matters

3. Portfolio Summary

4. Contact / About Me
```

---

# ⭐ **Section 1 — Python API Automation Framework**

## **1. Overview**

I built this Python project to demonstrate how I design backend automation using clean architecture, typed models, reusable fixtures, and a custom API client.  
The framework interacts with the public Petstore API and includes full CRUD coverage for Pets, Users, and Orders.

---

## **2. Tech Stack**

- Python 3.11+  
- pytest  
- requests  
- dataclasses  
- typing  
- pytest-html (optional)  

---

## **3. Folder Structure**

### **API Client (root-level)**

```
api/
│
├── petstore/
│   ├── models/
│   │   ├── pet.py
│   │   ├── user.py
│   │   ├── order.py
│   │   └── __init__.py
│   │
│   ├── base_api.py
│   ├── exceptions.py
│   ├── pets_api.py
│   ├── store_api.py
│   ├── users_api.py
│   └── __init__.py
│
└── __init__.py
```

### **Python Test Framework**

```
python-api/
│
├── config/
├── fixtures/
├── testdata/
├── tests/
│   └── api/
└── .pytest_cache/
```

---

## **4. How to Install & Run Tests**

```bash
git clone <repo>
cd python-api
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
pytest -v
```

---

## **5. API Client Overview**

I built a fully custom API client that includes:

- typed dataclass models  
- modular endpoint classes  
- centralized request/response handling  
- custom exceptions  
- defensive JSON parsing  

This mirrors real SDK design.

---

## **6. Test Suite Overview**

The test suite includes:

- CRUD tests for Pets, Users, Orders  
- negative scenarios  
- data-driven tests  
- reusable fixtures  
- clean assertions  

---

## **7. HTML Reporting (Optional)**

```bash
pytest --html=report.html --self-contained-html
```

---

## **8. Why This Project Matters**

This project demonstrates my ability to:

- build maintainable automation architecture  
- work with real, inconsistent APIs  
- design clean, typed Python code  
- validate backend systems thoroughly  

---

## **9. Future Enhancements**

- schema validation  
- retry logic  
- expanded negative testing  
- CI/CD integration  
- logging middleware  

---

# **Section 2 — Playwright UI/API Hybrid Framework**

## **1. Overview**

I built this Playwright project to demonstrate modern UI automation, API testing, and hybrid workflows using Page Object Model and reusable fixtures.

---

## **2. Tech Stack**

- Playwright Test (TypeScript)  
- Node.js  
- POM architecture  
- API request context  
- Trace viewer  

---

## **3. Folder Structure**

```
playwright/
│
├── api/
│   └── client/
├── configs/
├── fixtures/
├── pages/
├── testdata/
│   ├── api/
│   └── ui/
├── tests/
│   ├── api/
│   ├── ui/
│   └── hybrid/
└── utils/
```

---

## **4. Page Object Model (POM)**

Each page class includes:

- locators  
- actions  
- assertions  
- navigation helpers  

This keeps UI tests clean and maintainable.

---

## **5. Fixtures**

I use fixtures for:

- browser context  
- authenticated sessions  
- API context  
- test data  
- reporting hooks  

---

## **6. Hybrid UI + API Testing**

My hybrid tests demonstrate:

- creating data via API  
- validating UI behavior  
- cleaning up via API  
- verifying state changes  

This mirrors how modern SDET teams test complex systems.

---

## **7. Trace Viewer Integration**

```bash
npx playwright show-trace trace.zip
```

---

## **8. Why This Project Matters**

This project shows that I can:

- build scalable UI automation  
- combine UI and API layers  
- design maintainable Playwright architecture  
- debug using trace viewer  

---

# **Section 3 — Portfolio Summary**

Together, these two frameworks demonstrate my ability to build automation across both backend and frontend layers using modern tools and real-world engineering practices.

I focus on:

- architecture  
- maintainability  
- clarity  
- resilience  
- scalability  

This portfolio reflects how I approach automation as an engineer.

---

# **Section 4 — Contact / About Me**

Hi, I’m **Sandra**, and I’m passionate about building automation that is clean, reliable, and scalable.  
I approach automation like an engineer — focusing on architecture, maintainability, and real-world resilience.

If you’d like to connect:

- **Email:** sandy.pencek@gmail.com 
- **LinkedIn:** www.linkedin.com/in/sandy-pencek 
- **GitHub:** github.com/Sandydrago

---


