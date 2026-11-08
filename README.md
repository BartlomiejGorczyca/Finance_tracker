# Finance_tracker

## About

A web app to manage monthly personal finances: Track your incomes and expanses, manage your budget, create custom categories, visualize financial data through interactive graphs and statistics.

This project is being developed as part of the "Front-end Programing" course.

## Team

Bartek Gorczyca

## Features

Below is a list of the planned application features.

| Feature Name             | What the user does                     | View                  | Data      | Most challenging                              | Done when                                        |
| :----------------------- | :------------------------------------- | :-------------------- | :-------- | :-------------------------------------------- | :----------------------------------------------- |
| **Registration & Login** | Creates an account, logs in, logs out. | Login/Register screen | API (JWT) | Correct handling of tokens in the API client. | User sees their Dashboard only after logging in. |

| **Custom Categories** | Adds, edits, and deletes categories (name, type, color, icon). | `/categories` | API | Selecting color and icon from ready-made libraries | A new category appears in the list and can be used in a transaction. |

| **Add/Edit Transaction** | Fills out a form (amount, date, category, description) with validation. | Modal on `/transactions` | API | Form validation before submitting. | The form blocks invalid data (e.g., negative amount), and a valid transaction is saved to the DB. |

| **Transaction List with Filters** | Browses history, filters by month, category, and type. | `/transactions` | API | Synchronizing UI filters with backend queries. | Changing the filter immediately updates the list visible on the screen. |

| **Monthly Budget** | Sets a spending limit for a category. Sees a progress bar. | `/budgets` | API | Visual alert (red bar) when the limit is exceeded. | User sees on the Dashboard that they spent e.g., 80% of their food budget. |

| **Monthly Dashboard** | Views total income, expenses, and current balance. | `/` (main) | API | Fetching and summing data in a single request (aggregation). | Cards on the main page show current data for the current month. |

| **Charts** | Analyzes expenses by category and monthly trend. | `/` (main) | API | Correctly mapping data from the API to the structure required by Recharts. | Charts render correctly and react to data changes. |

## Stack

**Frontend:**

- React 19.3.0 + Typescript 7.0.2 + vite 8.3.2
- React Router 8.4.0
- TanStack Query 5 + Zustand 5.0.15
- Tailwind CSS 4.3.3
- Recharts 3.10.1
- React hook form 7.89.0 + zod 4.6.5

**backend:**

- Python 3.14.7 + Django 6.1.2 + Django REST Framework 3.18.1
- Django ORM
- DRF Serializers
- SimpleJWT
- Django Admin
- Django Migrations

**database:**

- PostgresSQL 18.6

**Devops:**

- Docker 29.8.2
- Github Actions 2.337.0
- Sentry 2.71.0
- Prometheus 3.15.0 + Grafana 13.3.0

## How to initialize

---
