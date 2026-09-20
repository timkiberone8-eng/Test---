from calculator_modules.arithmetic import add, subtract, multiply, divide


def main():
    try:
        print("Добро пожаловать в калькулятор!")
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))
        operation = input("Введите операцию (сложение, вычитание, умножение, деление): ").strip().lower()

        if operation == "сложение":
            result = add(a, b)
        elif operation == "вычитание":
            result = subtract(a, b)
        elif operation == "умножение":
            result = multiply(a, b)
        elif operation == "деление":
            result = divide(a, b)
        else:
            result = "Неизвестная операция"

        print(f"Результат: {result}")

    except ZeroDivisionError:
        print("Не дели на 0")

    except ValueError:
        print('Введено не число')

    finally:
        print("Операция завершена")


class NegativeNumberError(Exception):
    """исключение если отрицательное число"""


def sqrt_win_check(x):
    """корень с проверкой.Для отрицательного числа выбрасывает свое исключение"""


if __name__ == "__main__":
    main()
