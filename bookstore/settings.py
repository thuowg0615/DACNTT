"""
Cấu hình Django cho dự án ADCBooks.

Được tạo bởi 'django-admin startproject' sử dụng Django 5.2.8.
"""

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


# CẢNH BÁO BẢO MẬT: giữ bí mật khóa này khi chạy thực tế!
SECRET_KEY = 'django-insecure-6i35_h&c6s3!(h6wrfk)&sxl*=qy3x23(j11bu=$nuf__6tkq)'

DEBUG = True

ALLOWED_HOSTS = []



INSTALLED_APPS = [
    # Các app mặc định của Django
    'django.contrib.admin',          
    'django.contrib.auth',           
    'django.contrib.contenttypes',   
    'django.contrib.sessions',       
    'django.contrib.messages',       
    'django.contrib.staticfiles',    

    # Các thư viện bổ trợ
    'django_extensions',             
    'django_htmx',                   
    'tailwind',                      
    'theme',                         

    # Các nghiệp vụ 
    'books',                         
    'cart',                          
    'orders',                        
]

# Lớp trung gian
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django_htmx.middleware.HtmxMiddleware',         # Middleware cho HTMX
    'django.middleware.csrf.CsrfViewMiddleware',     # Bảo mật chống giả mạo request
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'bookstore.urls'

# Cấu hình Giao diện (Templates)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'cart.context_processors.cart_count', # Hiển thị số lượng giỏ hàng ở mọi nơi
            ],
        },
    },
]

WSGI_APPLICATION = 'bookstore.wsgi.application'


# Cơ sở dữ liệu (Database)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Sử dụng SQLite cho đơn giản
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Kiểm tra độ mạnh của mật khẩu
AUTH_PASSWORD_VALIDATORS = [
    { 'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator' },
    { 'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator' },
    { 'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator' },
    { 'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator' },
    { 'NAME': 'bookstore.validators.ComplexPasswordValidator' }, # Validator tùy chỉnh của bạn
]


# Đa ngôn ngữ và Thời gian
LANGUAGE_CODE = 'vi' # Bạn có thể đổi 'en-us' thành 'vi' để dùng tiếng Việt

TIME_ZONE = 'Asia/Ho_Chi_Minh' # Đổi sang giờ Việt Nam

USE_I18N = True

USE_TZ = True


# Tệp tĩnh và Tệp phương tiện (Ảnh, Video)
STATIC_URL = 'static/'
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media' # Nơi lưu trữ ảnh bìa sách bạn upload lên

# Kiểu dữ liệu mặc định cho ID (Primary Key)
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Cấu hình Tailwind
TAILWIND_APP_NAME = "theme"

# Điều hướng Xác thực (Login/Logout)
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'