SDET Automation Portfolio
Welcome to my SDET automation portfolio.
This repository demonstrates my ability to design real-world, scalable, and maintainable automation frameworks across both backend (API) and frontend (UI) layers.

This portfolio contains two complete automation projects, each built using industry-standard patterns:

Python API Testing Framework using a custom Petstore API client

Playwright UI/API Hybrid Testing Framework using Page Objects, fixtures, and environment configs

My goal is to show not just that I can write tests, but that I can architect automation systems the way real engineering teams expect.

Quick Start
Clone the repo and run either project:

Python API Tests
Code
cd python-api
pip install -r requirements.txt
pytest -v
Playwright Tests
Code
cd pw-project
npm install
npx playwright test
Top-Level Folder Structure
Code
playwright-portfolio/
│
├── api/                # Python API client (Petstore models + endpoint classes)
├── python-api/         # Python API automation framework (pytest)
├── pw-project/         # Playwright UI/API hybrid automation framework
├── test-data/          # Shared test data (if needed)
├── test-results/       # Playwright output artifacts
└── README.md
Section 1 — Python API Automation Framework
1. Overview
This Python project demonstrates backend automation using:

clean architecture

typed dataclass models

reusable fixtures

a custom API client

full CRUD coverage for Pets, Users, and Orders

It interacts with the public Petstore API and mirrors real SDK design patterns.

2. Tech Stack
Python 3.11+

pytest

requests

dataclasses-json

pytest-html (optional)

3. Folder Structure
API Client (root-level)
Code
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
Python Test Framework
Code
python-api/
│
├── config/
├── fixtures/
├── testdata/
├── tests/
│   └── api/
└── venv/
4. How to Install & Run Tests
Code
git clone <repo>
cd python-api
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
pytest -v
5. API Client Overview
The custom API client includes:

typed dataclass models

modular endpoint classes

centralized request/response handling

custom exceptions

defensive JSON parsing

This structure mirrors real-world SDK design.

6. Test Suite Overview
The test suite includes:

CRUD tests for Pets, Users, Orders

negative scenarios

data-driven tests

reusable fixtures

clean assertions

7. HTML Reporting (Optional)
Code
pytest --html=report.html --self-contained-html
8. Why This Project Matters
This project demonstrates my ability to:

build maintainable automation architecture

work with real, inconsistent APIs

design clean, typed Python code

validate backend systems thoroughly

9. Future Enhancements
schema validation

retry logic

expanded negative testing

CI/CD integration

logging middleware

Section 2 — Playwright UI/API Hybrid Framework
1. Overview
This Playwright project demonstrates modern UI automation, API testing, and hybrid workflows using:

Page Object Model

reusable fixtures

environment-driven configuration

parallel execution

trace viewer debugging

2. Tech Stack
Playwright Test (TypeScript)

Node.js

POM architecture

API request context

Trace viewer

3. Folder Structure
Code
pw-project/
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
4. Page Object Model (POM)
Each page class includes:

locators

actions

assertions

navigation helpers

This keeps UI tests clean and maintainable.

5. Fixtures
Fixtures provide:

browser context

API context

test data

reusable setup/teardown

clean dependency injection

6. Hybrid UI + API Testing
Hybrid tests demonstrate:

creating data via API

validating UI behavior

cleaning up via API

verifying state changes

This mirrors how modern SDET teams test complex systems.

7. Trace Viewer Integration
Code
npx playwright show-trace trace.zip
8. Why This Project Matters
This project shows that I can:

build scalable UI automation

combine UI and API layers

design maintainable Playwright architecture

debug using trace viewer

Section 3 — CI/CD (Coming Soon)
This project will include GitHub Actions workflows for:

running Playwright tests in parallel

running Python API tests

publishing HTML reports and Playwright traces as artifacts

Section 4 — Portfolio Summary
Together, these two frameworks demonstrate my ability to build automation across both backend and frontend layers using modern tools and real-world engineering practices.

I focus on:

architecture

maintainability

clarity

resilience

scalability

This portfolio reflects how I approach automation as an engineer.

Section 5 — Contact / About Me
Hi, I’m Sandra, and I’m passionate about building automation that is clean, reliable, and scalable.
I approach automation like an engineer — focusing on architecture, maintainability, and real-world resilience.

If you’d like to connect:

Email: sandra.pencek.sdet@gmail.com
LinkedIn: www.linkedin.com/in/sandy-pencek  
GitHub: github.com/Sandydrago
