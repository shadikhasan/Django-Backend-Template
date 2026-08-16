# Django Backend Template v2

A reusable Django backend starter with environment-based settings, Docker support, JWT auth, health check, OpenAPI docs, and a basic accounts module.

---

## Features

- Django 4.2+
- Environment-based settings (`dev`, `prod`, `test`)
- PostgreSQL (prod/dev-ready) and SQLite (simple local/testing)
- Celery + Redis settings
- DRF + SimpleJWT authentication
- OpenAPI schema + Swagger + ReDoc (`drf-spectacular`)
- Basic `accounts` app with auth/profile/password flows
- Health endpoint
- Custom superuser bootstrap command

---

## Project Structure

```text
Django-Backend-Template/
├── accounts/
│   ├── management/commands/create_superuser.py
│   ├── migrations/
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
├── common/
├── core/
│   ├── settings/
│   │   ├── base.py
│   │   ├── dev.py
│   │   ├── prod.py
│   │   └── test.py
│   ├── health.py
│   └── urls.py
├── docker-compose.yml
├── Dockerfile
├── manage.py
└── requirements.txt
```

---

## Quick Start

### 0) Download v2 branch

```bash
git clone --branch v2 --single-branch https://github.com/shadikhasan/Django-Backend-Template.git
cd Django-Backend-Template
```

### 1) Install

```bash
pip install -r requirements.txt
```

### 2) Configure `.env`

Use your root `.env` (sample keys):

```env
SECRET_KEY=change-me
DJANGO_ENV=dev
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

DB_ENGINE=sqlite
DB_HOST=postgres_service
DB_NAME=postgres_db
DB_USER=postgres_user
DB_PASSWORD=postgres_password
DB_PORT=5432
```

### 3) Migrate

```bash
python3 manage.py migrate
```

### 4) Create Superuser (template command)

```bash
python3 manage.py create_superuser
```

Optional:

```bash
python3 manage.py create_superuser --manual
```

### 5) Run server

```bash
python3 manage.py runserver
```

---

## Docker

```bash
docker-compose up --build
```

---

## API Endpoints

Base URL: `http://localhost:8000`

- `GET /health/`
- `GET /api/schema/`
- `GET /api/docs/`
- `GET /api/redoc/`

Accounts:

- `POST /api/accounts/login/`
- `POST /api/accounts/token/refresh/`
- `POST /api/accounts/logout/`
- `GET/PATCH /api/accounts/me/`
- `POST /api/accounts/change-password/`
- `POST /api/accounts/forgot-password/`
- `POST /api/accounts/reset-password/`

---

## Notes

- Custom user model is enabled: `AUTH_USER_MODEL = "accounts.User"`.
- Health endpoint returns app/database status and environment metadata.
- For production, replace template defaults (especially superuser/password/email settings).

---

## License

MIT
