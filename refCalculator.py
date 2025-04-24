import math
import logging

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')


class Calculator:
    def add(self, x, y): return x + y
    def subtract(self, x, y): return x - y
    def multiply(self, x, y): return x * y
    def divide(self, x, y):
        if y == 0:
            raise ValueError("Деление на ноль.")
        return x / y
    def power(self, base, exponent): return math.pow(base, exponent)
    def sqrt(self, value):
        if value < 0:
            raise ValueError("Отрицательное значение.")
        return math.sqrt(value)
    def factorial(self, n):
        if n < 0:
            raise ValueError("Факториал от отрицательного числа.")
        return math.factorial(n)
    def sin(self, degrees): return math.sin(math.radians(degrees))
    def cos(self, degrees): return math.cos(math.radians(degrees))
    def tan(self, degrees): return math.tan(math.radians(degrees))


def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка: Введите корректное число.")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Ошибка: Введите целое число.")


def show_menu():
    print("\n=== МЕНЮ КАЛЬКУЛЯТОРА ===")
    options = [
        "Сложение", "Вычитание", "Умножение", "Деление",
        "Степень", "Корень", "Факториал", "Синус", "Косинус", "Тангенс", "Выход"
    ]
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")


def main():
    calc = Calculator()
    operations = {
        "1": lambda: print("Результат:", calc.add(get_float("Первое число: "), get_float("Второе число: "))),
        "2": lambda: print("Результат:", calc.subtract(get_float("Первое число: "), get_float("Второе число: "))),
        "3": lambda: print("Результат:", calc.multiply(get_float("Первое число: "), get_float("Второе число: "))),
        "4": lambda: try_wrap(lambda: calc.divide(get_float("Первое число: "), get_float("Второе число: "))),
        "5": lambda: print("Результат:", calc.power(get_float("Основание: "), get_float("Показатель: "))),
        "6": lambda: try_wrap(lambda: calc.sqrt(get_float("Число: "))),
        "7": lambda: try_wrap(lambda: calc.factorial(get_int("Целое число: "))),
        "8": lambda: print("Результат:", calc.sin(get_float("Угол в градусах: "))),
        "9": lambda: print("Результат:", calc.cos(get_float("Угол в градусах: "))),
        "10": lambda: print("Результат:", calc.tan(get_float("Угол в градусах: "))),
        "11": lambda: exit_program()
    }

    while True:
        show_menu()
        choice = input("Выберите операцию: ")
        operation = operations.get(choice)
        if operation:
            operation()
        else:
            print("Некорректный выбор. Повторите ввод.")


def try_wrap(func):
    try:
        print("Результат:", func())
    except ValueError as e:
        print("Ошибка:", e)


def exit_program():
    print("До свидания!")
    exit()


if __name__ == "__main__":
    main()