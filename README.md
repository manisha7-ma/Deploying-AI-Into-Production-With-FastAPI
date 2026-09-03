# FastAPI Fundamentals — Learning Repository

A hands-on learning repository for following along with the FastAPI Fundamentals course on Pluralsight.

This repository contains my notes, examples, exercises, and mini-projects while learning FastAPI.

The goal is not just to complete the course, but to understand why FastAPI works the way it does and become comfortable building real-world Python APIs.

---

# Course

Course: FastAPI Fundamentals
Platform: Pluralsight

Course link:

https://app.pluralsight.com/ilx/video-courses/0a8aeab3-beaf-4272-b14f-4b58084afd8a/1f4a9d6b-8487-430d-823a-4c9f6f922942/9028350c-53b4-48f4-bd5c-90e0939e5689

---

# Learning Goals

By the end of this repository, I want to be comfortable with:

* Python type hints
* FastAPI fundamentals
* Creating REST APIs
* HTTP methods
* API routes and endpoints
* Path parameters
* Query parameters
* Request bodies
* Response models
* Pydantic models
* Data validation
* Dependency injection
* HTTP status codes
* Error handling
* Async programming
* API documentation
* Swagger and OpenAPI
* Project structure
* Database integration
* Authentication concepts
* Testing FastAPI applications
* Running FastAPI locally
* Building APIs that can be used by a frontend

---

# How I Am Using This Repository

I am following a learn, code, experiment, and document approach.

For every concept:

1. Watch the relevant course section.
2. Reproduce the example myself.
3. Type the code instead of copying it.
4. Change something in the example.
5. Break it intentionally.
6. Understand the error.
7. Write down what I learned.
8. Commit the changes to Git.

The objective is understanding, not just completing the videos.

---

# Repository Structure

The repository will gradually grow into something similar to:

```text
fastapi-fundamentals/
│
├── README.md
│
├── 01-basics/
│   ├── main.py
│   └── README.md
│
├── 02-path-parameters/
│   ├── main.py
│   └── README.md
│
├── 03-query-parameters/
│   ├── main.py
│   └── README.md
│
├── 04-request-body/
│   ├── main.py
│   └── models.py
│
├── 05-response-models/
│   ├── main.py
│   └── models.py
│
├── 06-validation/
│   ├── main.py
│   └── models.py
│
├── 07-dependencies/
│   ├── main.py
│   └── dependencies.py
│
├── 08-error-handling/
│   └── main.py
│
├── 09-async/
│   └── main.py
│
├── 10-database/
│   ├── main.py
│   ├── database.py
│   └── models.py
│
├── 11-authentication/
│   └── main.py
│
├── 12-testing/
│   └── test_main.py
│
└── requirements.txt
```

The exact folders may change as I progress through the course.

---

# Prerequisites

Before starting, I should be comfortable with basic Python.

Important Python concepts:

* Variables
* Functions
* Lists
* Dictionaries
* Classes
* Modules
* Imports
* Exceptions
* Virtual environments
* pip
* Basic type hints

Especially important:

```python
def add(a: int, b: int) -> int:
    return a + b
```

Understanding this will make FastAPI much easier because FastAPI uses Python type hints heavily.

---

# Python Environment Setup

## 1. Create the project

```bash
mkdir fastapi-fundamentals
cd fastapi-fundamentals
```

## 2. Create a virtual environment

Windows:

```powershell
python -m venv .venv
```

Activate it:

```powershell
.venv\Scripts\activate
```

Linux/macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

# Install FastAPI

Install FastAPI and Uvicorn:

```bash
pip install fastapi uvicorn
```

Save dependencies:

```bash
pip freeze > requirements.txt
```

---

# First FastAPI Application

Create:

```text
main.py
```

Example:

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World"}
```

Run the application:

```bash
uvicorn main:app --reload
```

The API should be available at:

```text
http://127.0.0.1:8000
```

---

# Automatic API Documentation

FastAPI automatically provides interactive API documentation.

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

ReDoc:

```text
http://127.0.0.1:8000/redoc
```

One of the important things I want to understand is:

How does FastAPI automatically generate these API documents from my Python code?

---

# Understanding APIs

Before learning individual FastAPI features, understand the basic API flow:

```text
Client
   |
   | HTTP Request
   v
FastAPI Application
   |
   | Route matching
   v
Endpoint function
   |
   | Business logic
   v
Response
   |
   | HTTP Response
   v
Client
```

Example:

```text
GET /users/10
```

means:

"Give me the user whose ID is 10."

---

# HTTP Methods

I need to understand the purpose of the common HTTP methods:

| Method | Purpose                |
| ------ | ---------------------- |
| GET    | Retrieve data          |
| POST   | Create data            |
| PUT    | Replace or update data |
| PATCH  | Partially update data  |
| DELETE | Delete data            |

FastAPI example:

```python
@app.get("/users")
def get_users():
    return {"users": []}


@app.post("/users")
def create_user():
    return {"message": "User created"}


@app.put("/users/{user_id}")
def update_user(user_id: int):
    return {"user_id": user_id}


@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    return {"message": "User deleted"}
```

---

# Path Parameters

A path parameter is part of the URL.

Example:

```text
/users/10
```

FastAPI:

```python
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}
```

Here:

```python
user_id: int
```

means FastAPI expects `user_id` to be an integer.

---

# Query Parameters

Query parameters appear after `?`.

Example:

```text
/users?limit=10
```

FastAPI:

```python
@app.get("/users")
def get_users(limit: int = 10):
    return {"limit": limit}
```

Multiple query parameters:

```text
/users?limit=10&active=true
```

---

# Request Body

When sending structured data to an API, we can use a request body.

Example:

```python
from pydantic import BaseModel


class User(BaseModel):
    name: str
    age: int
    email: str


@app.post("/users")
def create_user(user: User):
    return user
```

Example request:

```json
{
    "name": "Manisha",
    "age": 25,
    "email": "example@email.com"
}
```

FastAPI and Pydantic can validate the incoming data.

---

# Pydantic Models

Pydantic models are extremely important when working with FastAPI.

Example:

```python
from pydantic import BaseModel


class Product(BaseModel):
    name: str
    price: float
    quantity: int
```

Then:

```python
@app.post("/products")
def create_product(product: Product):
    return product
```

Things to understand:

* What is BaseModel?
* How does validation work?
* What happens when the wrong data type is provided?
* What happens when a required field is missing?
* What happens when an extra field is provided?

---

# Response Models

Request models describe what the API receives.

Response models describe what the API returns.

Example:

```python
class UserResponse(BaseModel):
    id: int
    name: str


@app.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int):
    return {
        "id": user_id,
        "name": "John"
    }
```

Important question:

Why should I use a response model instead of simply returning a dictionary?

---

# Error Handling

APIs need to return useful errors.

Example:

```python
from fastapi import HTTPException


@app.get("/users/{user_id}")
def get_user(user_id: int):

    if user_id != 1:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return {
        "id": 1,
        "name": "John"
    }
```

Understand:

```text
200 → Success
201 → Created
400 → Bad Request
401 → Unauthorized
403 → Forbidden
404 → Not Found
500 → Internal Server Error
```

---

# Dependency Injection

FastAPI has a dependency injection system.

Example:

```python
from fastapi import Depends


def common_parameters():
    return {
        "limit": 10
    }


@app.get("/items")
def get_items(
    params=Depends(common_parameters)
):
    return params
```

I want to understand:

* What is dependency injection?
* Why do we need it?
* What does Depends() do?
* Where would I use it in a real application?

---

# Async Programming

FastAPI supports asynchronous Python.

Example:

```python
@app.get("/items")
async def get_items():
    return {"items": []}
```

Important concepts:

```text
def
async def
await
asyncio
```

I should understand the difference between:

```python
def function():
```

and:

```python
async def function():
```

rather than simply memorizing the syntax.

---

# Database Integration

Eventually, the API should communicate with a database.

Typical architecture:

```text
Client
   |
   v
FastAPI
   |
   v
Service / Business Logic
   |
   v
Repository / Database Layer
   |
   v
Database
```

Things to learn:

* Database connection
* Models
* CRUD operations
* Sessions
* Transactions
* Async database access
* SQLAlchemy
* Database migrations

---

# Authentication

Important authentication concepts to learn:

* Authentication vs authorization
* Password hashing
* Access tokens
* JWT
* OAuth2
* Bearer tokens
* Protected endpoints
* Current user dependencies

Example concept:

```text
Client
   |
   | Login
   v
FastAPI
   |
   | Token
   v
Client
   |
   | Authorization: Bearer token
   v
Protected API
```

---

# Testing

I want to learn how to test FastAPI applications.

Example:

```python
def test_root():
    response = client.get("/")
    assert response.status_code == 200
```

Things to understand:

* Unit tests
* API tests
* Test clients
* Fixtures
* Mocking
* Testing database interactions

---

# Useful Commands

Run FastAPI:

```bash
uvicorn main:app --reload
```

Install a package:

```bash
pip install package-name
```

Save dependencies:

```bash
pip freeze > requirements.txt
```

Create virtual environment:

```bash
python -m venv .venv
```

Check Python:

```bash
python --version
```

Check pip:

```bash
pip --version
```

---

# Learning Notes

For every major topic, I will maintain notes using this format.

## Topic: __________________

### What is it?

Explain the concept in simple words.

### Why do we need it?

Explain the problem it solves.

### Syntax

```python
# example
```

### Example

```python
# practical example
```

### What I understood

Write my own explanation here.

### What confused me

Write questions here.

### Experiment

Change the example and see what happens.

### Key takeaway

One or two sentences summarizing the concept.

---

# Experiment Log

This section is intentionally for experiments.

| Date | Experiment | Result | What I learned |
| ---- | ---------- | ------ | -------------- |
|      |            |        |                |
|      |            |        |                |
|      |            |        |                |

Examples of experiments:

* What happens if I remove a required field?
* What happens if I send a string instead of an integer?
* What happens if the endpoint does not exist?
* What happens if I change def to async def?
* What happens if I change the response model?
* What happens if I raise a different HTTP status code?

---

# Questions I Should Be Able to Answer

Before considering a topic complete, I should be able to explain it without looking at the course.

## FastAPI

* What is FastAPI?
* Why use FastAPI instead of a basic Python HTTP server?
* What is an endpoint?
* What is a route?
* What does @app.get() do?
* What does @app.post() do?

## Python

* What are type hints?
* What is async?
* What is await?
* What is a decorator?
* What is dependency injection?

## Pydantic

* What is BaseModel?
* How does validation work?
* What is a response model?

## HTTP

* What is HTTP?
* What is the difference between GET and POST?
* What is a status code?
* What is JSON?
* What are headers?
* What is a request body?

## APIs

* What is REST?
* What makes an API RESTful?
* What is CRUD?
* How does a frontend communicate with a backend?

---

# Final Project

After completing the fundamentals, I will build a small application without following the course step-by-step.

## Project: Task Management API

The application should support:

### Users

```text
POST   /users
GET    /users
GET    /users/{id}
PUT    /users/{id}
DELETE /users/{id}
```

### Tasks

```text
POST   /tasks
GET    /tasks
GET    /tasks/{id}
PUT    /tasks/{id}
DELETE /tasks/{id}
```

### Features

* FastAPI
* Pydantic
* Validation
* CRUD
* Database
* Error handling
* Authentication
* Dependency injection
* Async operations
* Automated tests
* API documentation

---

# Learning Checklist

## Python

* [ ] Functions
* [ ] Classes
* [ ] Type hints
* [ ] Decorators
* [ ] Exceptions
* [ ] Virtual environments
* [ ] async and await

## FastAPI

* [ ] Create FastAPI application
* [ ] Create routes
* [ ] GET
* [ ] POST
* [ ] PUT
* [ ] PATCH
* [ ] DELETE
* [ ] Path parameters
* [ ] Query parameters
* [ ] Request bodies
* [ ] Response models
* [ ] Validation
* [ ] HTTP exceptions
* [ ] Status codes
* [ ] Dependencies
* [ ] Middleware
* [ ] Async endpoints

## Pydantic

* [ ] BaseModel
* [ ] Field validation
* [ ] Optional fields
* [ ] Nested models
* [ ] Response models
* [ ] Serialization

## Database

* [ ] SQL basics
* [ ] SQLAlchemy
* [ ] Models
* [ ] Sessions
* [ ] CRUD
* [ ] Migrations
* [ ] Async database access

## Authentication

* [ ] Authentication
* [ ] Authorization
* [ ] Password hashing
* [ ] JWT
* [ ] OAuth2
* [ ] Protected routes

## Testing

* [ ] pytest
* [ ] Test client
* [ ] API tests
* [ ] Fixtures
* [ ] Mocking

## Project

* [ ] Build API independently
* [ ] Connect database
* [ ] Add authentication
* [ ] Add tests
* [ ] Document API
* [ ] Clean project structure
* [ ] Push final project to GitHub

---

# End Goal

At the end of this repository, I should be able to look at a FastAPI project and understand:

```text
Frontend
   |
   v
HTTP Request
   |
   v
FastAPI Route
   |
   v
Validation
   |
   v
Dependencies
   |
   v
Business Logic
   |
   v
Database
   |
   v
Response Model
   |
   v
HTTP Response
   |
   v
Frontend
```

And, more importantly, I should be able to build a similar application myself without following a tutorial line-by-line.

---

# Git Workflow

After completing each meaningful section:

```bash
git status
git add .
git commit -m "Learn FastAPI path parameters"
git push
```

Example commit messages:

```text
Learn FastAPI basics
Add path parameter examples
Add query parameter examples
Add Pydantic request models
Add response models
Add validation examples
Add error handling
Add dependency injection examples
Add async examples
Add database integration
Add authentication
Add API tests
Add final task management API
```

---

# Personal Rule

Consistency is more important than speed.

I do not need to finish the course quickly.

I need to reach the point where I can explain what I built and why it works.
