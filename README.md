# Authentication Application

A simple full-stack Authentication application built for learning modern web development.

This project is the fourth step of the **Playground Learning Path**.
The goal is to learn how authentication works in modern web applications by implementing user registration, login,
protected endpoints, and profile management using JWT-based authentication.

## Project Structure

This project consists of two parts:

* Backend: FastAPI REST API
* Frontend: React Application

## Learning Goals

### Backend (FastAPI)

The backend focuses on implementing secure authentication and user management.

#### Topics

* REST API Design
* HTTP Methods
* User Registration
* User Authentication
* JWT (JSON Web Token)
* Access Tokens
* Password Hashing
* Protected Routes
* Authorization
* SQLAlchemy Models
* Pydantic Schemas
* Database Integration
* Request Validation
* Dependency Injection
* Authentication Dependencies
* API Documentation with Swagger

---

### Frontend (React)

The frontend focuses on managing authentication state and interacting with protected API endpoints.

#### Topics

* React Components
* Authentication Flow
* Login Form
* Registration Form
* Form Validation
* Fetching Protected Data
* JWT Storage
* Authorization Headers
* Route Protection
* Private Routes
* User Profile Page
* Profile Update Forms
* Password Change Form
* Logout Functionality
* Loading States
* Error Handling

## Features

Users can:

* Register a new account
* Log in with email/username and password
* Receive an access token
* Access protected endpoints
* View their own profile
* Update profile information
* Change their password
* Log out from the application

## Authentication Flow

This project introduces JWT-based authentication.

Typical flow:

1. User registers a new account.
2. User logs in using their credentials.
3. The backend validates the credentials and returns an access token.
4. The frontend stores the token securely.
5. The token is sent with every request to protected endpoints.
6. The backend validates the token before granting access.
7. The authenticated user can access endpoints such as `/me`, update their profile, or change their password.

## About Playground

**Playground** is a learning project series created to practice modern web development by building small full-stack
applications.

Each project focuses on introducing new concepts step by step, from basic CRUD operations to more advanced topics like
authentication, database relationships, and real-world application architecture.

The main goal is learning through building.

## Contributors

Built by:

* Backend **FastAPI**: [Amirhossein Mohammadi](https://github.com/BlackIQ)
* Frontend **React**: [Maedeh Sadat Khorasani](https://github.com/maedehskh80)

This project is part of a collaborative learning journey between backend and frontend development.
