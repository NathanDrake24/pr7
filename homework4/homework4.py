def solve_equation(a, b, c):
    x = 3 * a + 3 - b + 4 * c
    return x


def calculate_and_prompt():
    user_input = input("Введите значения a, b и c через пробел(или 'q' для выхода): ")

    if user_input.lower() == 'q':
        print("Выход из программы.")
        return  # Выход из функции и завершение программы

    try:
        # Разделяем введенные значения
        a, b, c = map(float, user_input.split())

        # Решение уравнения
        x = solve_equation(a, b, c)

        # Вывод результата
        print(f"Решение уравнения x = 3 * {a} + 3 - {b} + 4 * {c} равно: x = {x}")

    except ValueError:
        print("Ошибка: введите три числовых значения для a, b и c, разделенные пробелами.")

    # Рекурсивный вызов для следующего ввода
    calculate_and_prompt()


def main():
    calculate_and_prompt()


if __name__ == '__main__':
    main()
