import re


def validate_amount(amount_str):
    try:
        parts = amount_str.split(' ')
        return len(parts[0]) == 3 and float(parts[1])
    except ValueError:
        return False


def validate_phone(phone_str):
    try:
        return re.match('^\+\d{1,3}\d{3,}$', phone_str)
    except ValueError:
        return False