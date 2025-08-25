# 🍋 Little Lemon API

A **Django REST Framework (DRF)** powered API for managing restaurant categories, menu items, carts, orders, and order items.  
This project demonstrates a complete API backend with authentication, browsable endpoints, and JWT support.

---

## 🚀 Features

- User authentication via:
  - Session-based login (for development, browsable API)
  - Token-based authentication
  - JWT (JSON Web Token) authentication
- Manageable entities:
  - **Categories**: Grouping of menu items
  - **Menu Items**: Food & drinks with categories and prices
  - **Cart**: Store user-selected items before placing an order
  - **Orders**: Track customer orders with status and assigned delivery crew
  - **Order Items**: Items belonging to a specific order
- Admin panel for managing data
- RESTful endpoints with CRUD support
- Optional browsable documentation (Swagger/Redoc)

---

## 🛠️ Tech Stack

- **Backend**: Django 5 + Django REST Framework
- **Authentication**: Djoser, DRF TokenAuth, JWT (SimpleJWT)
- **Database**: SQLite (dev) / PostgreSQL (production-ready)
- **Documentation**: DRF browsable API / Swagger / Redoc

---

## ⚙️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/your-username/little-lemon-api.git
cd little-lemon-api

Create and activate a virtual environment

python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows


Install dependencies

pip install -r requirements.txt


Run migrations

python manage.py makemigrations
python manage.py migrate


Create a superuser

python manage.py createsuperuser


Run the development server

python manage.py runserver


API is available at http://127.0.0.1:8000/api/.

Authentication

Session Authentication: /api-auth/login/ for browsable API testing.

Token Authentication (Djoser):

Obtain token: POST /auth/token/login/

Logout: POST /auth/token/logout/

JWT Authentication (SimpleJWT):

Obtain tokens: POST /api/token/

Refresh token: POST /api/token/refresh/

Blacklist token: POST /api/token/blacklist/

API Endpoints
Categories

GET /api/categories/ → List all categories

POST /api/categories/ → Create new category

GET /api/categories/{id}/ → Retrieve category by ID

PUT /api/categories/{id}/ → Update category

PATCH /api/categories/{id}/ → Partial update

DELETE /api/categories/{id}/ → Delete category

Menu Items

GET /api/menuitems/ → List all menu items

POST /api/menuitems/ → Create a new menu item

GET /api/menuitems/{id}/ → Retrieve menu item by ID

PUT /api/menuitems/{id}/ → Update menu item

PATCH /api/menuitems/{id}/ → Partial update

DELETE /api/menuitems/{id}/ → Delete menu item

Cart

GET /api/cart/ → List current user’s cart items

POST /api/cart/ → Add item to cart

GET /api/cart/{id}/ → Retrieve cart item

PUT /api/cart/{id}/ → Update cart item

PATCH /api/cart/{id}/ → Partial update

DELETE /api/cart/{id}/ → Remove cart item

Orders

GET /api/orders/ → List all orders

POST /api/orders/ → Create a new order

GET /api/orders/{id}/ → Retrieve order details

PUT /api/orders/{id}/ → Update order (status, delivery crew)

PATCH /api/orders/{id}/ → Partial update

DELETE /api/orders/{id}/ → Cancel/delete order

Order Items

GET /api/order-items/ → List all order items

POST /api/order-items/ → Create new order item

GET /api/order-items/{id}/ → Retrieve order item details

PUT /api/order-items/{id}/ → Update order item

PATCH /api/order-items/{id}/ → Partial update

DELETE /api/order-items/{id}/ → Delete order item

Group Management

POST /api/assign-group/ → Assign user to a group (Manager / Delivery Crew)

Browsable API

DRF Browsable API: http://127.0.0.1:8000/api/

Login/logout available via the top-right of the browsable API.

Permissions

IsManagerOnly → Managers only

IsDeliveryCrewOnly → Managers or Delivery Crew

IsOwnerOrManager → Object owner or manager

Example Seed Data
Categories

Appetizers

Main Course

Desserts

Drinks

Menu Items

Caesar Salad (Appetizers)

Grilled Chicken (Main Course)

Chocolate Cake (Desserts)

Lemonade (Drinks)

Development Notes

Default authentication in development:

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ]
}


In production, use JWT authentication, disable session auth, and secure with HTTPS.

Workflow Example

Register/Login a user via /auth/.

Obtain token from /auth/token/login/ or /api/token/.

Create categories and menu items.

Add items to cart.

Convert cart into orders.

Track order items and update order status.

License

MIT License © 2025


This includes **all endpoints**, full instructions, example seed data, authentication, and workflows.  

If you want, I can **also add curl examples for every endpoint** so someone can test the API without the browsable interface. This is really useful for documentation. Do you want me to do that?