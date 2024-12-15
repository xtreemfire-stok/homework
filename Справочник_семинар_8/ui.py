from logger import input_data, print_data

def interface():
    print("Здравствуйте!!! Вы попали на специальный бот справочник! \n 1 - Запись данных \n 2 Ввод данных")
    command = int(input())

    while command != 1 and command != 2:
        print("Неправильный ввод")
        command = int(input("ВВедите число"))

    if command == 1:
        input_data()
    elif command == 2:
        print_data()