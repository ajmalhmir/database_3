# Customer Management API

A Django REST API for managing customer information including name, phone, and balance.

## Features

- Create, Read, Update, and Delete (CRUD) operations for customer data
- RESTful API endpoints
- Django REST Framework for API development

## API Endpoints

- `GET /api/customers/` - List all customers
- `POST /api/customers/` - Create a new customer
- `GET /api/customers/{id}/` - Retrieve a specific customer
- `PUT /api/customers/{id}/` - Update a customer (full update)
- `PATCH /api/customers/{id}/` - Partial update a customer
- `DELETE /api/customers/{id}/` - Delete a customer

## Customer Model

- `name`: Customer's full name
- `phone`: Customer's phone number
- `balance`: Customer's account balance
- `created_at`: Timestamp when the customer was created
- `updated_at`: Timestamp when the customer was last updated

## Setup and Installation

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run migrations: `python manage.py migrate`
4. Start the development server: `python manage.py runserver`

## Testing the API

You can use the included `test_api.py` script to test the API functionality:

```bash
python test_api.py
```

This script demonstrates creating, retrieving, updating, and deleting customers through the API.