from datetime import datetime
import json


def count_students(data_list):
    """
    Функция считывает количество студентов в списке
    :param data_list: список словарей с данными о студентах
    :return: общее количество студентов
    """
    return len(data_list)


def age_counter(data_list):
    """
    Функция считает средний возраст студентов в момент их поступления на курс
    :param data_list: тут находится список словарей с ключами birth_date и enrollment_date
    :return: Возвращает средний возраст студентов в годах
    """
    sum_age = []
    for i in data_list:
        birth_date = datetime.strptime(i["birth_date"], "%d.%m.%Y")
        enrollment_date = datetime.strptime(i["enrollment_date"], "%d.%m.%Y")
        diff_days = enrollment_date - birth_date
        sum_age.append(diff_days.days // 365)

    return sum(sum_age) / len(sum_age)


def stud_courses(data_list):
    """
    Функция считает количество студентов на каждом курсе
    :param data_list: тут находиться список словарей с ключом courses
    :return: возвращает словарь данными курса и количество участвующих в нём студентов
    """
    stats = {}
    for i in data_list:
        courses_list = i.get("courses", [])
        for j in courses_list:
            if j not in stats:
                stats[j] = 1
            else:
                stats[j] += 1


    return stats


def saving_data(source, path):
    """
    Функция агрегирует данных предыдущих трёх функций и сохраняет их в файл формата json
    :param source: путь к исходному файлу , где находяться данные о студентах
    :param path: путь , куда сохраняются данные
    :return: сообщает пользователю , что данные успешно сохранены
    """
    with open(source, "r", encoding="utf-8") as f:
        loaded_data = json.load(f)
    path_dict = {"total_students": count_students(loaded_data),
            'average_enrollment_age': age_counter(loaded_data),
            'students_per_course': sorted(stud_courses(loaded_data))}

    with open(path, "w", encoding="utf-8") as new_file:
        json.dump(path_dict, new_file, ensure_ascii=False, indent=4)

        return f"Information has been saved successfully"


print(saving_data("student_courses.json", "student_courses_report.json"))