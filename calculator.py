import math
import logging

# Настройка логгера
logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')

class Calculator:
    def add(self, a, b):
        logging.info(f"Сложение: {a} + {b}")
        return a + b

    def subtract(self, a, b):
        logging.info(f"Вычитание: {a} - {b}")
        return a - b

    def multiply(self, a, b):
        logging.info(f"Умножение: {a} * {b}")
        return a * b

    def divide(self, a, b):
        logging.info(f"Деление: {a} / {b}")
        if b == 0:
            raise ValueError("Нельзя делить на ноль.")
        return a / b

    def power(self, a, b):
        logging.info(f"Степень: {a} ^ {b}")
        return math.pow(a, b)

    def sqrt(self, a):
        logging.info(f"Корень: √{a}")
        if a < 0:
            raise ValueError("Корень из отрицательного числа невозможен.")
        return math.sqrt(a)

    def factorial(self, n):
        logging.info(f"Факториал: {n}!")
        if n < 0:
            raise ValueError("Факториал от отрицательного числа невозможен.")
        return math.factorial(n)

    def sin(self, angle_deg):
        logging.info(f"sin({angle_deg})")
        return math.sin(math.radians(angle_deg))

    def cos(self, angle_deg):
        logging.info(f"cos({angle_deg})")
        return math.cos(math.radians(angle_deg))

    def tan(self, angle_deg):
        logging.info(f"tan({angle_deg})")
        return math.tan(math.radians(angle_deg))


def show_menu():
    print("\n=== МЕНЮ КАЛЬКУЛЯТОРА ===")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")
    print("5. Возведение в степень")
    print("6. Квадратный корень")
    print("7. Факториал")
    print("8. Синус")
    print("9. Косинус")
    print("10. Тангенс")
    print("0. Выход")


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка: Введите корректное число.")


def get_integer(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Ошибка: Введите целое число.")


def main():
    calc = Calculator()
    while True:
        show_menu()
        choice = input("Выберите операцию: ")

        if choice == "1":
            a = get_number("Первое число: ")
            b = get_number("Второе число: ")
            print("Результат:", calc.add(a, b))
        elif choice == "2":
            a = get_number("Первое число: ")
            b = get_number("Второе число: ")
            print("Результат:", calc.subtract(a, b))
        elif choice == "3":
            a = get_number("Первое число: ")
            b = get_number("Второе число: ")
            print("Результат:", calc.multiply(a, b))
        elif choice == "4":
            a = get_number("Первое число: ")
            b = get_number("Второе число: ")
            try:
                result = calc.divide(a, b)
                print("Результат:", result)
            except ValueError as e:
                print("Ошибка:", e)
        elif choice == "5":
            a = get_number("Основание: ")
            b = get_number("Показатель: ")
            print("Результат:", calc.power(a, b))
        elif choice == "6":
            a = get_number("Число: ")
            try:
                print("Результат:", calc.sqrt(a))
            except ValueError as e:
                print("Ошибка:", e)
        elif choice == "7":
            n = get_integer("Целое число: ")
            try:
                print("Результат:", calc.factorial(n))
            except ValueError as e:
                print("Ошибка:", e)
        elif choice == "8":
            a = get_number("Введите угол в градусах: ")
            print("Результат:", calc.sin(a))
        elif choice == "9":
            a = get_number("Введите угол в градусах: ")
            print("Результат:", calc.cos(a))
        elif choice == "10":
            a = get_number("Введите угол в градусах: ")
            print("Результат:", calc.tan(a))
        elif choice == "0":
            print("До свидания!")
            break
        else:
            print("Некорректный выбор. Повторите ввод.")

if __name__ == "__main__":
    main()