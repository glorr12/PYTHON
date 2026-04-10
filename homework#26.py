import os
import sys

finder = sys.argv[1]
print(f"Содержимое директории : {finder}")
print("Папки : ")
for root, dirs, files in os.walk(finder):
    for dir in dirs:
        print(f"- {dir}\n")
print("Файлы : ")
for root, dirs, files in os.walk(finder):
    for file in files:
        print(f"- {file}\n")


# ---------------------------------------------------------


random = sys.argv[1]
extension = sys.argv[2]

for root, dirs, files in os.walk(random):
    for file in files:
        if file.endswith(extension):
            print(f"Найден файл с расширением: '{extension}': ")
            print(f"- {os.path.join(root, file)}")
            while True:
                delete_file = input("Вы хотите удалить этот файл? (y/n): ").lower()
                try:
                    if delete_file not in ["y", "n"]:
                        raise ValueError("Введите коррентные даннын типа y(да), n(нет)")
                except ValueError as e:
                    print(f"Найдена ошибка! {e}")
                else:
                    if delete_file == "y":
                        os.remove(os.path.join(root, file))
                        print("Файл удалён")
                        break
                    else:
                        pass
                        break