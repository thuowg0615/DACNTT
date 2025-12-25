"""
Cấu hình WSGI cho dự án bookstore (Nhà sách).

Tệp này giúp các máy chủ web (web server) có thể giao tiếp với ứng dụng Django của bạn.
Nó chứa một biến có tên là ``application`` để máy chủ web gọi tới.

Để biết thêm thông tin về tệp này, vui lòng truy cập:
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# Thiết lập cài đặt mặc định cho môi trường Django thông qua file settings của dự án.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookstore.settings')

# Khởi tạo ứng dụng WSGI. Đây là đối tượng mà các máy chủ như Gunicorn hoặc uWSGI sẽ sử dụng.
application = get_wsgi_application()