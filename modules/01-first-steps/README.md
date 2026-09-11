# Module 1: First Steps

## Overview

This module introduces the basic structure of a FastAPI application.

The main objective is to understand how to:

* Create a FastAPI project
* Create a FastAPI application
* Install FastAPI
* Run the application
* Create an API endpoint
* Access the API from a browser
* Understand the automatically generated documentation
* Understand how FastAPI executes endpoint functions

---

# 1. Project Setup

## Python Version

FastAPI requires Python 3.8 or newer.

For this project, I am using:

```bash
python --version
```

## Virtual Environment

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\activate
```

Activate it on Linux/macOS:

```bash
source .venv/bin/activate
```

The purpose of a virtual environment is to keep the dependencies for this project isolated from other Python projects.

---

# 2. Installing FastAPI

Install FastAPI:

```bash
python -m pip install "fastapi[standard]"
```

The standard extras provide additional tools needed to run and work with FastAPI applications.

---

# 3. Creating the FastAPI Application

Create a file called:

```text
main.py
```

Basic application:

```python
from fastapi import FastAPI

app = FastAPI()
```

Here:

```python
app = FastAPI()
```

creates the FastAPI application object.

This `app` object is used to define the API routes.

---

# 4. Creating an Endpoint

Example:

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World"}
```

The important parts are:

```python
@app.get("/")
```

and:

```python
def root():
```

`@app.get("/")` tells FastAPI that the `root()` function should be executed when a client sends a GET request to `/`.

---

# 5. Understanding the Request Flow

The basic flow is:

```text
Client
   |
   | GET /
   v
FastAPI
   |
   | Finds matching route
   v
root()
   |
   | Returns dictionary
   v
FastAPI converts response
   |
   v
Client
```

---

# 6. Running the Application

Run:

```bash
uvicorn main:app --reload
```

Meaning:

```text
uvicorn
    |
    |-- ASGI server

main
    |
    |-- Python file: main.py

app
    |
    |-- FastAPI application object

--reload
    |
    |-- Restart server when code changes
```

---

# 7. Testing the API

Open:

```text
http://127.0.0.1:8000
```

Expected response:

```json
{
    "message": "Hello World"
}
```

---

# 8. Automatic API Documentation

FastAPI automatically generates API documentation.

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

ReDoc:

```text
http://127.0.0.1:8000/redoc
```

Important concept:

FastAPI uses the information in the Python code, including routes and type hints, to generate an OpenAPI schema and interactive documentation.

---

# 9. What I Learned

## FastAPI

FastAPI is a Python web framework used to build APIs.

## Uvicorn

Uvicorn is the server used to run the FastAPI application.

## Endpoint

An endpoint is a specific URL and HTTP method that the API responds to.

Example:

```text
GET /
```

## Route

A route connects an HTTP request to a Python function.

Example:

```python
@app.get("/")
def root():
    ...
```

---

# 10. Things I Need to Understand Better

* What exactly is an ASGI server?
* What happens between the browser sending a request and my Python function executing?
* What is OpenAPI?
* How does FastAPI generate `/docs` automatically?
* What exactly does the `@app.get()` decorator do?
* Why do we need Uvicorn?

---

# 11. Experiment

Try changing:

```python
@app.get("/")
def root():
    return {"message": "Hello World"}
```

to:

```python
@app.get("/")
def root():
    return {"message": "My first FastAPI application"}
```

Then refresh the browser.

Next, create another endpoint:

```python
@app.get("/hello")
def hello():
    return {"message": "Hello from another endpoint"}
```

Test:

```text
http://127.0.0.1:8000/hello
```

Then check:

```text
http://127.0.0.1:8000/docs
```

Observe how the new endpoint automatically appears in Swagger UI.

---

# 12. Questions I Should Be Able to Answer

Before moving to the next module, I should be able to answer:

1. What is FastAPI?
2. What is Uvicorn?
3. What is an API endpoint?
4. What does `@app.get()` do?
5. What is a route?
6. What does `--reload` do?
7. Where does FastAPI get its API documentation from?
8. What is OpenAPI?
9. What happens when I visit `/` in the browser?
10. What is the difference between the FastAPI application and the Uvicorn server?

---

# 13. Completion Checklist

* [X] Created Python project
* [X] Created virtual environment
* [X] Installed FastAPI
* [ ] Created `main.py`
* [ ] Created FastAPI application
* [ ] Created first GET endpoint
* [ ] Started application using Uvicorn
* [ ] Tested API in browser
* [ ] Opened Swagger UI
* [ ] Opened ReDoc
* [ ] Created a second endpoint
* [ ] Experimented with the code
* [ ] Answered the questions above
* [ ] Committed code to Git

---

# Git Commit

Example:

```bash
git add .
git commit -m "Complete FastAPI first steps"
git push
```
