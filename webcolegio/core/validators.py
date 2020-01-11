from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_only_letters(value):
    valor = value.replace(" ", "")
    if not valor.isalpha():
        raise ValidationError(
            _('Este campo solo admite letras'),
            params={'value': value},
        )
