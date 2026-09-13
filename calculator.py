a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))

operation = input("Введите операцию (сложение, вычитание, умножение, деление): ").strip().lower()

if operation == "сложение":
    result = a + b
elif operation == "вычитание":
    result = a - b
elif operation == "умножение":
    result = a * b
elif operation == "деление":
    result = a / b
else:
    result = "Неизвестная операция"

print(f"Результат: {result}")
