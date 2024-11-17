import re


def find_in_file(name_file: str, pattern_zero: any) -> None:
    try:
        with open(name_file, 'r', encoding='utf-8') as file:
            text: str = file.read()
    except FileNotFoundError:
        print("Мы не можем получить доступ к файлу.")
    else:
        matches: list = re.findall(pattern_zero, text)
        result: list[str] = []
        for match in matches:
            # match[0] - часы, match[3] - минуты (если есть)
            time_str: str = f"UTC{match[0]}"
            if match[2]:  # Если минуты найдены
                time_str += f":{match[2]}"
            result.append(time_str)  # Формируем список совпадений в нужном формате

        print(result)


def checking_the_input(entry: str, pattern_zero: any) -> None:
    matches: list = re.findall(pattern_zero, entry)
    result: list[str] = []

    for match in matches:
        # match[0] - часы, match[2] - минуты (если есть)
        time_str: str = f"UTC{match[0]}"

        if match[2]:  # Если минуты найдены
            time_str += f":{match[2]}"

        # Добавляем только если минуты равны 00, 30 или 45
        if match[2] in ['00', '30', '45', '']:
            result.append(time_str)

    if not result:
        print("Здесь нет корректного обозначения")
    else:
        print(result)


if __name__ == "__main__":
    pattern: str = r'UTC[+-](0|1[0-2]|[1-9])(:([0]{2}|30|45))?'

    while True:
        choice: str = input("Если хотите провести поиск в файле, то введите 1. "
                            "Если хотите ввести в ручную, то введите 2. Выход - 3: ")
        if choice == "1":
            find_in_file('Article_about_UTC.txt', pattern)

        elif choice == "2":
            line: str = input("Введите текст: ")
            checking_the_input(line, pattern)

        elif choice == "3":
            break

        else:
            print("Некорректное значение, попытайтесь снова")
