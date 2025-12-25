import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

class ComplexPasswordValidator:
    """
    Kiểm tra xem mật khẩu có đáp ứng các yêu cầu về độ phức tạp hay không:
    - Ít nhất 8 ký tự
    - Ít nhất 1 chữ cái viết hoa
    - Ít nhất 1 chữ cái viết thường
    - Ít nhất 1 chữ số
    - Ít nhất 1 ký tự đặc biệt
    """

    def validate(self, password, user=None):
        # 1. Kiểm tra độ dài
        if len(password) < 8:
            raise ValidationError( 
                "Mật khẩu phải có ít nhất 8 ký tự.",
                code='password_too_short',
            )

        # 2. Kiểm tra chữ cái viết hoa
        if not re.search(r'[A-Z]', password):
            raise ValidationError(
                "Mật khẩu phải chứa ít nhất một chữ cái viết hoa.",
                code='password_no_upper',
            )

        # 3. Kiểm tra chữ cái viết thường
        if not re.search(r'[a-z]', password):
            raise ValidationError(
                "Mật khẩu phải chứa ít nhất một chữ cái thường.",
                code='password_no_lower',
            )

        # 4. Kiểm tra chữ số
        if not re.search(r'\d', password):
            raise ValidationError(
                "Mật khẩu phải chứa ít nhất một chữ số.",
                code='password_no_digit',
            )

        # 5. Kiểm tra ký tự đặc biệt
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            raise ValidationError(
                "Mật khẩu phải chứa ít nhất một ký tự đặc biệt (!@#$%^&*(),.?\":{}|<>).",
                code='password_no_special',
            )

    def get_help_text(self):
        """
        Trả về đoạn văn bản hướng dẫn sẽ hiển thị dưới ô nhập mật khẩu trong các Form của Django.
        """
        return ( "Mật khẩu của bạn phải có ít nhất 8 ký tự và bao gồm ít nhất: "
            "một chữ cái viết hoa, một chữ cái viết thường, một chữ số và một ký tự đặc biệt."
        )