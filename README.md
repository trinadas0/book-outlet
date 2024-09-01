# Book Outlet - Django Online Bookstore

## Overview

**Book Outlet** is an online bookstore built with Django. Users can browse books, add them to their cart, and manage their shopping experience with features like quantity updates and deletion of items from the cart. The application includes user authentication, allowing users to sign up, log in, log out, and manage their cart securely.

## Features

- Browse available books
- View detailed information about each book
- Add books to a shopping cart
- Update quantities or remove books from the cart
- User authentication (sign up, log in, log out)
- Responsive and clean user interface with Flexbox layout
  
### Prerequisites

- Python 3.x installed on your system
- Django 3.x or 4.x
- Virtual environment (recommended)

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/bookoutlet.git
    cd bookoutlet
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

3. **Install dependencies:**

    ```bash
    pip install django
    ```

4. **Apply migrations to set up the database:**

    ```bash
    python manage.py migrate
    ```

5. **Create a superuser for admin access (optional but recommended):**

    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

7. **Access the application:**

    Open your web browser and go to `http://127.0.0.1:8000/` to view the site.

## Usage

### Navigating the Site

- **Home Page:** Browse available books.
- **Book Details:** Click on any book to view more details.
- **Cart:** Add books to your cart, update quantities, or remove items.
- **Authentication:** Sign up, log in, and log out using the navigation bar.

### Admin Interface

If you've created a superuser, you can access the Django admin interface to manage books, users, and other data.

- Visit `http://127.0.0.1:8000/admin/` to log in to the admin panel.
