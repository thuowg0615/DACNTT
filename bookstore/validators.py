import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _


class ComplexPasswordValidator:
    """
    Validate that the password meets complexity requirements:
    - At least 8 characters
    - At least 1 uppercase letter
    - At least 1 lowercase letter
    - At least 1 digit
    - At least 1 special character
    """

    def validate(self, password, user=None):
        if len(password) < 8:
            raise ValidationError(
                _("Mật khẩu phải có ít nhất 8 ký tự."),
                code='password_too_short',
            )

        if not re.search(r'[A-Z]', password):
            raise ValidationError(
                _("Mật khẩu phải chứa ít nhất một chữ cái viết hoa."),
                code='password_no_upper',
            )

        if not re.search(r'[a-z]', password):
            raise ValidationError(
                _("Mật khẩu phải chứa ít nhất một chữ cái thường."),
                code='password_no_lower',
            )

        if not re.search(r'\d', password):
            raise ValidationError(
                _("Mật khẩu phải chứa ít nhất một chữ số."),
                code='password_no_digit',
            )

        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            raise ValidationError(
                _("Mật khẩu phải chứa ít nhất một ký tự đặc biệt (!@#$%^&*(),.?\":{}|<>)."),
                code='password_no_special',
            )

    def get_help_text(self):
        return _(
            "Mật khẩu của bạn phải có ít nhất 8 ký tự và chứa ít nhất"
            "một chữ cái viết hoa, một chữ cái viết thường, một chữ số và một ký tự đặc biệt."
        )
