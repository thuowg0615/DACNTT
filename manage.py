
"""Tiện ích dòng lệnh của Django cho các tác vụ quản trị."""
import os
import sys


def main():
    """Chạy các tác vụ quản trị."""
    # Thiết lập biến môi trường để Django biết nơi tìm tệp cài đặt (settings.py)
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookstore.settings')
    
    try:
        # Thử nhập hàm xử lý dòng lệnh từ thư viện Django
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # Lỗi này thường xảy ra nếu Django chưa được cài đặt hoặc 
        # chưa kích hoạt môi trường ảo (virtual environment)
        raise ImportError(
            "Không thể nhập (import) Django. Bạn có chắc chắn rằng nó đã được cài đặt và "
            "có sẵn trong biến môi trường PYTHONPATH không? Đừng quên "
            "kích hoạt môi trường ảo của bạn."
        ) from exc
    
    # Thực thi các lệnh được truyền vào từ cửa sổ dòng lệnh (terminal)
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()