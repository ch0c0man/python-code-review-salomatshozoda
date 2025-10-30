# 1. Нарушение PEP 8 (именование и пробелы)
def ADD(x, y):
    return x+y

# 2. Нарушение PEP 8 (пробелы вокруг оператора) и неочевидное именование
def subtract(a,b):
    r = a - b # 3. Неочевидное именование переменной (r - что это?)
    return r

# 4. Избыточный код
def multiply(a, b):
    c = a * b
    return c

# 5. Потенциальная ошибка деления на ноль
def divide(a, b):
    return a / b

# 6. Магическое число в коде
def check_result(result):
    if result > 100: # Что означает 100?
        print("Результат большой!")
    return result

def main():
    print("Калькулятор")
    # 7. Отсутствие обработки ошибок ввода (используем int вместо float, чтобы сломаться на дроби)
    a = int(input("Первое число: "))
    b = int(input("Второе число: "))
    op = input("Операция (+, -, *, /): ")

    if op == '+':
        result = ADD(a, b)
    elif op == '-':
        result = subtract(a, b)
    elif op == '*':
        result = multiply(a, b)
    elif op == '/':
        result = divide(a, b)

    result = check_result(result)
    print("Ответ:", result)

if __name__ == "__main__":
    main()
