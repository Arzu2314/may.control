def filter_short_strings(strings):
    result = []
    for string in strings:
        if len(string) <= 3:
            result.append(string)
    return result

def main():
    # Ввод исходного массива строк
    strings = input("Введите элементы массива через пробел: ").split()

    # Фильтрация строк длиной <= 3 символов
    filtered_strings = filter_short_strings(strings)

    # Вывод отфильтрованного массива
    print("Отфильтрованный массив строк:", filtered_strings)

if __name__ == "__main__":
    main()
