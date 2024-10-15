import threading

def decimal_to_octal(decimal_num):
    return oct(decimal_num).replace("0o", "")

def convert_decimal(exit_flag):
    try:
        decimal_number = input("Введите целое десятичное число для перевода (или 'q' для выхода): ")
        if decimal_number == 'q':
            exit_flag = True
        else:
            decimal_number = int(decimal_number)
            if decimal_number < 0:
                print("Пожалуйста, введите положительное десятичное число.")
            else:
                octal_number = decimal_to_octal(decimal_number)
                print(f"Десятичное число {decimal_number} в восьмеричной системе: {octal_number}")

    except ValueError:
        print("Ошибка: Введите целое десятичное число.")

    if not exit_flag:
        convert_decimal(exit_flag)

def main():
    exit_flag = False
    convert_decimal(exit_flag)
    # Создаем и запускаем поток для выполнения функции convert_decimal
    #thread = threading.Thread(target=convert_decimal, args=(exit_flag,))
    #thread.start()
    # Ждем завершения потока
    #thread.join()

if __name__ == '__main__':
    main()


