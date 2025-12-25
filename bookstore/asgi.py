"""
Cấu hình ASGI cho project bookstore.
File này cung cấp ASGI callable dưới dạng biến ở cấp module có tên là ``application``.
Để biết thêm thông tin về file này, xem tại:
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookstore.settings')
application = get_asgi_application()
