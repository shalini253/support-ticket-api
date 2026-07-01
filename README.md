# 🚀 Support Ticket API

A cloud-native customer support ticketing system built with FastAPI, PostgreSQL, Docker, and GitHub Actions.

This project demonstrates how modern backend applications are designed, containerized, and continuously integrated using production-style engineering practices.

---

## Features

- RESTful API built with FastAPI
- PostgreSQL database with SQLAlchemy ORM
- Create, retrieve, update, and delete support tickets
- Dockerized application and database using Docker Compose
- Automated CI pipeline with GitHub Actions
- Modular architecture (Router → Service → Database)

---

## Tech Stack

- Python 3.12
- FastAPI
- PostgreSQL
- SQLAlchemy
- Docker
- Docker Compose
- GitHub Actions
- Git

---

## Project Architecture

```
Client
   │
   ▼
FastAPI API
   │
   ▼
Service Layer
   │
   ▼
SQLAlchemy ORM
   │
   ▼
PostgreSQL
```

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /tickets | Create a support ticket |
| GET | /tickets | Retrieve all tickets |
| GET | /tickets/{id} | Retrieve a ticket by ID |
| PUT | /tickets/{id} | Update a ticket |
| DELETE | /tickets/{id} | Delete a ticket |

---

## Running Locally

```bash
git clone https://github.com/shalini253/support-ticket-api.git

cd support-ticket-api

docker compose up --build
```

Open:

```
http://localhost:8000/docs
```

to access the interactive Swagger API documentation.

---

## CI/CD

Every push to the `main` branch automatically:

- Checks out the repository
- Installs dependencies
- Builds the Docker image
- Validates that the application can be built successfully using GitHub Actions

---

## Future Improvements

- Terraform infrastructure provisioning
- AWS deployment
- Kubernetes deployment
- Helm charts
- Prometheus monitoring
- Grafana dashboards
- Authentication and authorization
- Redis caching
- API rate limiting

---

## Author

**Shalini Mallik**

GitHub: https://github.com/shalini253