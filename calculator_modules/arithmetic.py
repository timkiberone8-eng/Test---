
def add(x, y):
    """Возвращает сумму двух чисел"""
    return x + y


def subtract(x, y):
    """Возвращает разность двух чисел"""
    return x - y


def multiply(x, y):
    """Возвращает произведение двух чисел"""
    return x * y


def divide(x, y):
    """Возвращает частное двух чисел. Деление на ноль вызывает ошибку"""
    if y != 0:
        return x / y
    else:
        return "Ошибка: деление на ноль"