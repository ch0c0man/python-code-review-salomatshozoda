def add(a, b):
    """Возвращает сумму двух чисел."""
    return a + b


def subtract(a, b):
    """Возвращает разность двух чисел."""
    return a - b


def multiply(a, b):
    """Возвращает произведение двух чисел."""
    return a * b


def divide(a, b):
    """Возвращает результат деления a на b.
    Обрабатывает ошибку деления на ноль.
    """
    if b == 0:
        return "Ошибка: деление на ноль!"
    return a / b


def main():
    """Основная функция, предоставляющая консольный интерфейс для калькулятора."""
    print("Добро пожаловать в простой калькулятор!")
    print("Доступные операции: +, -, *, /")
    print("Для выхода введите 'exit'.")

    while True:
        user_input = input("\nВведите операцию (например, 5 + 3): ").strip()

        if user_input.lower() == 'exit':
            print("Выход из калькулятора.")
            break

        # Разбиваем ввод пользователя
        parts = user_input.split()
        if len(parts) != 3:
            print("Ошибка: неверный формат. Используйте: <число> <операция> <число>")
            continue

        a_str, op, b_str = parts

        # Пробуем преобразовать введенные данные в числа
        try:
            a = float(a_str)
            b = float(b_str)
        except ValueError:
            print("Ошибка: оба операнда должны быть числами.")
            continue

        # Выполняем операцию в зависимости от введенного символа
        result = None
        if op == '+':
            result = add(a, b)
        elif op == '-':
            result = subtract(a, b)
        elif op == '*':
            result = multiply(a, b)
        elif op == '/':
            result = divide(a, b)
        else:
            print(f"Ошибка: неизвестная операция '{op}'.")
            continue

        # Выводим результат
        print(f"Результат: {result}")


if __name__ == "__main__":
    main()
