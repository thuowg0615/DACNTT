import threading
from decimal import Decimal
from datetime import datetime
from .models import Order, OrderItem


class OrderBuilder:
    """
    Mẫu thiết kế Builder để tạo các đối tượng Order và OrderItem.
    Xử lý quá trình tạo đơn hàng phức tạp theo từng bước.
    """

    def __init__(self):
        self._user = None
        self._items = []
        self._status = 'paid'  

    def set_user(self, user):
        """Thiết lập người dùng cho đơn hàng"""
        self._user = user
        return self

    def add_item(self, book, quantity, price):
        """Thêm một mặt hàng (sách) vào danh sách chờ của đơn hàng"""
        self._items.append({
            'book': book,
            'quantity': quantity,
            'price': price,
        })
        return self

    def set_status(self, status):
        """Thiết lập trạng thái đơn hàng"""
        self._status = status
        return self

    def calculate_total(self):
        """Tính tổng tiền dựa trên các mặt hàng đã thêm"""
        total = Decimal('0')
        for item in self._items:
            total += item['price'] * item['quantity']
        return total

    def build(self):
        """
        Kiểm tra tính hợp lệ và lưu Đơn hàng vào Cơ sở dữ liệu.
        Trả về đối tượng Order đã tạo.
        """
        if not self._user:
            raise ValueError("Người dùng phải được thiết lập trước khi tạo đơn hàng.")
        if not self._items:
            raise ValueError("Ít nhất một mặt hàng phải được thêm vào trước khi tạo đơn hàng.")

        total = self.calculate_total()

        # Order chính
        order = Order.objects.create(
            user=self._user,
            total_price=total,
            status=self._status
        )

        # chi tiết OrderItem
        for item in self._items:
            OrderItem.objects.create(
                order=order,
                book=item['book'],
                quantity=item['quantity'],
                price=item['price']
            )

        return order

    def reset(self):
        """Làm mới Builder để sẵn sàng tạo đơn hàng mới"""
        self._user = None
        self._items = []
        self._status = 'paid'
        return self


class InvoiceGenerator:
    """
    Mẫu thiết kế Singleton để tạo hóa đơn; chỉ có một instance duy nhất quản lý việc định dạng hóa đơn.
    """

    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        # Double-checked locking để tối ưu hiệu suất
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance

    def generate_invoice(self, order):
        """Chuyển đổi dữ liệu đơn hàng thành định dạng văn bản hóa đơn"""
        lines = [
            "=" * 50,
            "                HÓA ĐƠN BÁN HÀNG",
            "=" * 50,
            "",
            f"Mã đơn hàng: {order.id}",
            f"Ngày đặt: {order.created_at.strftime('%d-%m-%Y %H:%M:%S')}",
            f"Khách hàng: {order.user.username}",
            f"Email: {order.user.email or 'N/A'}",
            "",
            "-" * 50,
            "DANH SÁCH MẶT HÀNG:",
            "-" * 50,
        ]

        for item in order.items.all():
            lines.append(f"  {item.book.name}")
            lines.append(f"    Số lượng: {item.quantity} x {item.price} VNĐ = {item.subtotal()} VNĐ")
            lines.append("")

        lines.extend([
            "-" * 50,
            f"TỔNG CỘNG: {order.total_price} VNĐ",
            "-" * 50,
            "",
            f"Trạng thái: {order.get_status_display()}",
            "",
            "=" * 50,
            "          Cảm ơn bạn đã mua hàng!",
            "=" * 50,
        ])

        return "\n".join(lines)