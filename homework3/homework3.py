def integer_to_base_six_recursive(n):
    """Рекурсивная функция для перевода целой части числа в шестиричную систему счисления."""
    if n == 0:
        return ""
    return integer_to_base_six_recursive(n // 6) + str(n % 6)


def fraction_to_base_six_recursive(fraction, precision=10, result=""):
    """Рекурсивная функция для перевода дробной части числа в шестиричную систему с заданной точностью."""
    if fraction == 0 or len(result) >= precision:
        return result
    fraction *= 6
    digit = int(fraction)
    return fraction_to_base_six_recursive(fraction - digit, precision, result + str(digit))


def convert_to_base_six(exit_flag):
    if exit_flag:
        return
    try:
        decimal_number = input("Введите десятичное число для перевода в шестиричную систему (или 'q' для выхода): ")
        if decimal_number.lower() == 'q':
            exit_flag = True
        else:
            # Проверка, является ли введённое значение числом с плавающей точкой
            if '.' in decimal_number:
                decimal_number = float(decimal_number)

                # Разделение на целую и дробную части
                integer_part = int(decimal_number)
                fraction_part = decimal_number - integer_part

                # Перевод целой части в шестиричную систему
                if integer_part == 0:
                    integer_base_six = "0"
                else:
                    integer_base_six = integer_to_base_six_recursive(abs(integer_part))

                # Перевод дробной части в шестиричную систему
                fraction_base_six = fraction_to_base_six_recursive(abs(fraction_part))

                # Объединение результатов для числа с плавающей точкой
                if decimal_number < 0:
                    result = f"-{integer_base_six}.{fraction_base_six}"
                else:
                    result = f"{integer_base_six}.{fraction_base_six}"

                print("Число в шестиричной системе с плавающей точкой:", result)

            else:
                # Обработка целого числа
                decimal_number = int(decimal_number)

                # Перевод целого числа в шестиричную систему
                if decimal_number == 0:
                    result = "0"
                else:
                    result = integer_to_base_six_recursive(abs(decimal_number))

                if decimal_number < 0:
                    result = f"-{result}"

                print("Целое число в шестиричной системе:", result)

    except ValueError:
        print("Ошибка: Введите правильное десятичное число.")

    # Рекурсивный вызов с обновлённым значением exit_flag
    convert_to_base_six(exit_flag)


def main():
    exit_flag = False
    convert_to_base_six(exit_flag)


if __name__ == '__main__':
    main()
