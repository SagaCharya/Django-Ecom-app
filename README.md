# eCommerce App

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/downloads/)

A fully-featured **eCommerce app** built with **Django**. This app supports user registration, product listings, shopping carts, checkout, and order management.

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Setup](#setup)
- [Contact](#contact)

## Features

- **User Authentication**: Sign up, login, and manage user profiles.
- **Product Listings**: Display products with sorting and filtering options.
- **Shopping Cart**: Add, update, and remove products in the shopping cart.
- **Checkout Process**: Users can place orders and make payments.
- **Search Functionality**: Search products by name or category.

## Tech Stack

- **Backend**: Django
- **Frontend**: HTML, CSS, JavaScript (with jQuery or vanilla JS)
- **Database**: SQLite (or any other preferred database)
- **Payment Gateway**: Stripe.
- **Authentication**: Django’s built-in authentication system


## Installation

### Prerequisites

- Python 3.8 or above
- PostgreSQL (or another database of your choice)
- Redis (for Celery)
- Git

### Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/SagaCharya/Django-Ecom-app.git
   cd ecommerce-app
   
2. Create a Virtual Environment
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install dependencies
    ```bash
    pip install -r requirements.txt
4. Configure the database:
  -Update the DATABASES setting in your settings.py with your database credentials.
  -Run migrations:
     ```bash
     python manage.py migrate
5. Run the Django development server:
   ```bash
   python manage.py runserver
6. Access the application: Open your browser and go to http://127.0.0.1:8000/.

## Contact

For any questions or inquiries, feel free to reach out to me at sagacharya77@gmail.com.
   
