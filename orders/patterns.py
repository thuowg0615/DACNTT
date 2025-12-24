import threading
from decimal import Decimal
from datetime import datetime
from .models import Order, OrderItem


class OrderBuilder:
    """
    Builder pattern for creating Order and OrderItem objects.
    Handles the complex creation process step by step.
    """

    def __init__(self):
        self._user = None
        self._items = []
        self._status = 'paid'

    def set_user(self, user):
        self._user = user
        return self

    def add_item(self, book, quantity, price):
        self._items.append({
            'book': book,
            'quantity': quantity,
            'price': price,
        })
        return self

    def set_status(self, status):
        self._status = status
        return self

    def calculate_total(self):
        total = Decimal('0')
        for item in self._items:
            total += item['price'] * item['quantity']
        return total

    def build(self):
        if not self._user:
            raise ValueError("Người dùng phải được thiết lập trước khi tạo đơn hàng.")
        if not self._items:
            raise ValueError("Ít nhất một mặt hàng phải được thêm vào trước khi tạo đơn hàng.")

        total = self.calculate_total()

        order = Order.objects.create(
            user=self._user,
            total_price=total,
            status=self._status
        )

        for item in self._items:
            OrderItem.objects.create(
                order=order,
                book=item['book'],
                quantity=item['quantity'],
                price=item['price']
            )

        return order

    def reset(self):
        self._user = None
        self._items = []
        self._status = 'paid'
        return self


class InvoiceGenerator:
    """
    Singleton pattern for invoice generation.
    Ensures a single instance manages invoice formatting.
    Thread-safe implementation.
    """

    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance

    def generate_invoice(self, order):
        lines = [
            "=" * 50,
            "                    INVOICE",
            "=" * 50,
            "",
            f"Order #: {order.id}",
            f"Date: {order.created_at.strftime('%Y-%m-%d %H:%M:%S')}",
            f"Customer: {order.user.username}",
            f"Email: {order.user.email or 'N/A'}",
            "",
            "-" * 50,
            "ITEMS:",
            "-" * 50,
        ]

        for item in order.items.all():
            lines.append(f"  {item.book.name}")
            lines.append(f"    Quantity: {item.quantity} x {item.price} .VNĐ = {item.subtotal()} .VNĐ")
            lines.append("")

        lines.extend([
            "-" * 50,
            f"TOTAL: {order.total_price} .VNĐ",
            "-" * 50,
            "",
            f"Status: {order.get_status_display()}",
            "",
            "=" * 50,
            "          Cảm ơn bạn đã mua hàng!",
            "=" * 50,
        ])

        return "\n".join(lines)
