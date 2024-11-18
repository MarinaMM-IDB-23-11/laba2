import re


def find_in_file(name_file: str) -> bool:
    pattern: str = r'UTC([+-])(\d?\d)(:(00|30|45))?'  # регулярное выражение

    try:
        with open(name_file, 'r', encoding='utf-8') as file:
            text: str = file.read()

    except FileNotFoundError:
        print("Мы не можем получить доступ к файлу.")
        return False

    else:
        matches: list = re.findall(pattern, text)
        result: list[str] = []
        for match in matches:
            hours = int(match[1])  # Преобразуем часы в целое число
            # Проверяем, что часы находятся в диапазоне от 0 до 12
            if 0 <= hours <= 12:
                time_str: str = f"UTC{match[0]}{match[1]}"  # match[0] - знак, match[1] - часы

                if match[3]:  # Если минуты найдены
                    # Проверяем, что минуты равны 00, 30 или 45
                    if match[3] in ['00', '30', '45']:
                        time_str += f"{match[2]}"
                        result.append(time_str)
                else:
                    result.append(time_str)  # Если минут нет, добавляем только часы

        if not result:
            print("Здесь нет корректного обозначения")
            return False
        print(result)
        return True


def checking_the_input(entry: str) -> list[str] | None:
    pattern: str = r'UTC([+-])(\d?\d)(:(00|30|45))?'  # регулярное выражение

    matches: list = re.findall(pattern, entry)
    print(matches)  # Для отладки
    result: list[str] = []

    for match in matches:
        # Проверяем, что часы находятся в диапазоне от 1 до 12
        if '0' <= match[1] <= '12':
            time_str: str = f"UTC{match[0]}{match[1]}"  # match[0] - знак, match[1] - часы

            if match[3]:  # Если минуты найдены
                # Проверяем, что минуты равны 00, 30 или 45
                if match[3] in ['00', '30', '45']:
                    time_str += f"{match[2]}"
                    result.append(time_str)
                else:
                    break
            else:
                result.append(time_str)  # Если минут нет, добавляем только часы

    if not result:
        print("Здесь нет корректного обозначения")
        return None
    else:
        print(result)
        return result


if __name__ == "__main__":
    while True:
        choice: str = input("Если хотите провести поиск в файле, то введите 1. "
                            "Если хотите ввести в ручную, то введите 2. Выход - 3: ")
        if choice == "1":
            find_in_file('Article_about_UTC.txt')

        elif choice == "2":
            line: str = input("Введите текст: ")
            checking_the_input(line)

        elif choice == "3":
            break

        else:
            print("Некорректное значение, попытайтесь снова")
