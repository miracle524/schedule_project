
# Django CRUD API with JWT Authentication

This project demonstrates a Django REST API for managing weekly schedules with JWT (JSON Web Token) authentication. The API uses `djangorestframework-simplejwt` for JWT and Swagger for interactive documentation.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Setup](#setup)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [JWT Authentication](#jwt-authentication)
- [Swagger Documentation](#swagger-documentation)

## Features

- Django REST Framework for API
- JWT Authentication using `djangorestframework-simplejwt`
- Swagger UI for API documentation
- CRUD operations for weekly schedules

## Installation

1. **Clone the repository**:

   ```bash
   git clone <repository-url>
   cd config
   ```

2. **Create and activate a virtual environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. **Install the dependencies**:

   ```bash
   pip install django djangorestframework djangorestframework-simplejwt drf-yasg
   ```

## Setup

1. **Apply Migrations**:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

2. **Create a Superuser**:

   ```bash
   python manage.py createsuperuser
   ```

3. **Run the Server**:

   ```bash
   python manage.py runserver
   ```

## Usage

### Obtain JWT Token

```bash
curl -X POST http://localhost:8000/api/token/ -d '{"username": "user", "password": "pass"}'
```

### Access Protected Endpoints

Use `Bearer your_access_token` in the `Authorization` header.

```bash
curl -X GET http://localhost:8000/api/schedules/ -H "Authorization: Bearer your_access_token"
```

## API Endpoints

- `POST /api/token/`: Get JWT token
- `GET /api/schedules/`: List schedules
- `POST /api/schedules/`: Create schedule
- `PUT /api/schedules/{id}/`: Update schedule
- `DELETE /api/schedules/{id}/`: Delete schedule

## JWT Authentication

1. **Add JWT Settings in `settings.py`**:

   ```python
   INSTALLED_APPS = [
       'rest_framework',
       'rest_framework_simplejwt',
   ]
   REST_FRAMEWORK = {
       'DEFAULT_AUTHENTICATION_CLASSES': (
           'rest_framework_simplejwt.authentication.JWTAuthentication',
       ),
   }
   ```

2. **Add Token URLs in `urls.py`**:

   ```python
   from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
   urlpatterns += [
       path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
       path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
   ]
   ```

## Swagger Documentation

Add Swagger URLs for API documentation:

```python
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Schedule API",
      default_version='v1',
   ),
   public=True,
)

urlpatterns += [
    path('swagger/', schema_view.with_ui('swagger'), name='schema-swagger-ui'),
]
```

Access Swagger at `http://localhost:8000/swagger/`.
