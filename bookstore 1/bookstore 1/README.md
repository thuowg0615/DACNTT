# 📚 Bookstore - Django Textbook Store

A comprehensive Django-based online bookstore for textbooks with features like authentication, cart management, ratings, comments, and demo payment processing.

## Features

### 1. Authentication
- User registration and login using Django's built-in authentication
- Secure password handling
- User-specific cart and order history

### 2. Book Catalog
- Browse textbooks with detailed information (name, price, image, grade, subject)
- Filter books by grade and subject
- Search books by name (exact text search)
- View average ratings and total number of ratings
- Quick "Add to Cart" functionality from the list view

### 3. Book Details
- Detailed book information page
- User ratings (1-5 stars)
- User comments and reviews
- Add books to cart with custom quantity

### 4. Shopping Cart
- View all items in cart
- Update quantities using HTMX for seamless experience
- Remove items from cart
- Real-time cart count in navigation
- Calculate subtotals and total price

### 5. Checkout & Payment
- Select which items to purchase
- Demo payment interface (no actual payment processing)
- Automatic order creation and history tracking
- Payment success notification

### 6. Admin Panel
- Manage grades, subjects, and books
- View and moderate ratings and comments
- Manage orders and user carts

## Tech Stack

- **Backend**: Django 5.2.8
- **Frontend**: Tailwind CSS 4 + DaisyUI 5
- **Interactive UI**: HTMX 2.0.8
- **Package Manager**: uv
- **Database**: SQLite (default)

## Installation & Setup

### Prerequisites
- Python 3.12+
- uv package manager

### Steps

1. **Install dependencies** (already done):
```bash
uv add django django-tailwind pillow
```

2. **Run migrations** (already done):
```bash
uv run python manage.py migrate
```

3. **Create sample data** (already done):
```bash
uv run python manage.py setup_data
```

4. **Create a superuser** (for admin access):
```bash
uv run python manage.py createsuperuser
```

5. **Start the development server**:
```bash
uv run python manage.py runserver
```

6. **Access the application**:
- Main site: http://localhost:8000/
- Admin panel: http://localhost:8000/admin/

## Usage Guide

### For Users

1. **Register an account**:
   - Click "Register" in the navigation
   - Fill in username, email, and password
   - You'll be automatically logged in

2. **Browse books**:
   - Use filters to find books by grade or subject
   - Use the search bar to find specific books
   - View ratings and prices

3. **View book details**:
   - Click on any book to see full details
   - Read comments from other users
   - Add ratings and comments (requires login)

4. **Add to cart**:
   - Click "Add to Cart" from the book list
   - Or specify quantity on the book detail page
   - Cart count updates automatically in navigation

5. **Manage cart**:
   - Click "Cart" in navigation
   - Update quantities or remove items
   - Proceed to checkout when ready

6. **Complete purchase**:
   - Select items you want to purchase
   - Click "Complete Payment" for demo checkout
   - View your order in "Orders" section

### For Admins

1. **Access admin panel**:
   - Login at http://localhost:8000/admin/
   - Use superuser credentials

2. **Manage content**:
   - Add/edit/delete grades and subjects
   - Add books with images, prices, and descriptions
   - Moderate ratings and comments
   - View all orders

## Project Structure

```
bookstore/
├── books/              # Book catalog, ratings, comments
│   ├── models.py       # Book, Grade, Subject, Rating, Comment models
│   ├── views.py        # Book views and authentication
│   ├── forms.py        # Registration form
│   ├── admin.py        # Admin configuration
│   └── templates/      # Book-related templates
├── cart/               # Shopping cart functionality
│   ├── models.py       # Cart and CartItem models
│   ├── views.py        # Cart management views
│   ├── context_processors.py  # Cart count in navigation
│   └── templates/      # Cart templates
├── orders/             # Order processing
│   ├── models.py       # Order and OrderItem models
│   ├── views.py        # Checkout and order history
│   └── templates/      # Order templates
├── theme/              # Tailwind/DaisyUI theme
│   └── templates/      # Base template with navigation
└── bookstore/          # Main project settings
    ├── settings.py     # Django settings
    └── urls.py         # URL configuration
```

## Key Technologies Used

### HTMX Integration
- Seamless cart updates without page refresh
- Smooth item removal from cart
- Enhanced user experience with minimal JavaScript

### DaisyUI Components
- Navbar with dropdown
- Cards for books and orders
- Forms with styled inputs
- Badges for cart count and order status
- Toast notifications for user feedback

### Django Features
- Class-based and function-based views
- Model relationships (ForeignKey, OneToOne)
- Context processors for global data
- Admin customization
- Built-in authentication

## Sample Data

The application comes with pre-populated data:
- **Grades**: Lớp 1 through Lớp 12 (Vietnamese grade levels)
- **Subjects**: Toán, Tiếng Việt, Tiếng Anh, Vật Lý, Hóa Học, Sinh Học, Lịch Sử, Địa Lý, Tin Học, Công Nghệ
- **Sample Books**: 2 sample textbooks for testing

## Notes

- This is a demo application with simulated payment processing
- Images are optional - books without images show a book emoji placeholder
- The cart automatically creates when a user adds their first item
- Ratings are limited to one per user per book
- All prices are in Vietnamese Dong (₫) but displayed with $ symbol

## Future Enhancements

Potential features to add:
- Real payment gateway integration
- Book inventory management
- Wishlist functionality
- Advanced search with multiple filters
- Email notifications for orders
- User profile pages
- Book recommendations
- Reviews moderation system