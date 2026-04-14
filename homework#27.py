filename = input("Введите имя файла для поиска: ").strip()
keyword = input("Введите ключевое слово: ").strip()
try:
    with open(filename, "r", encoding="utf-8") as source_file:
        found_lines = []
        for line in source_file:
            if keyword in line:
                found_lines.append(line)
    if found_lines:
        new_filename = f"{keyword}_{filename}"
        with open(new_filename, "w", encoding="utf-8") as result_file:
            result_file.writelines(found_lines)
        print(f"Строки  содержащие '{keyword}'  сохранены в {new_filename}.")
    else:
        print(f"Строки  содержащие '{keyword}' не найдены")
except FileNotFoundError:
    print("Ошибка!Файл не существует")


#------------------------------------------



filename = input("Введите имя файла: ").strip()
try:
    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()
    found = set()
    unique_lines = []
    for line in lines:
        if line not in found:
            found.add(line)
            unique_lines.append(line)
    new_filename = f"unique_{filename}"
    with open(new_filename, "w", encoding="utf-8") as result:
        result.writelines(unique_lines)
    print(f"Дубликаты удалены. Уникальные строки сохранены в {new_filename}.")
except FileNotFoundError:
    print("Ошибка! Файл не существует.")
