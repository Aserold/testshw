courses = [
    "Python-разработчик с нуля",
    "Java-разработчик с нуля",
    "Fullstack-разработчик на Python",
    "Frontend-разработчик с нуля",
]

mentors = [
    [
        "Евгений Шмаргунов",
        "Олег Булыгин",
        "Дмитрий Демидов",
        "Кирилл Табельский",
        "Александр Ульянцев",
        "Александр Бардин",
        "Александр Иванов",
        "Антон Солонилин",
        "Максим Филипенко",
        "Елена Никитина",
        "Азамат Искаков",
        "Роман Гордиенко",
    ],
    [
        "Филипп Воронов",
        "Анна Юшина",
        "Иван Бочаров",
        "Анатолий Корсаков",
        "Юрий Пеньков",
        "Илья Сухачев",
        "Иван Маркитан",
        "Ринат Бибиков",
        "Вадим Ерошевичев",
        "Тимур Сейсембаев",
        "Максим Батырев",
        "Никита Шумский",
        "Алексей Степанов",
        "Денис Коротков",
        "Антон Глушков",
        "Сергей Индюков",
        "Максим Воронцов",
        "Евгений Грязнов",
        "Константин Виролайнен",
        "Сергей Сердюк",
        "Павел Дерендяев",
    ],
    [
        "Евгений Шмаргунов",
        "Олег Булыгин",
        "Александр Бардин",
        "Александр Иванов",
        "Кирилл Табельский",
        "Александр Ульянцев",
        "Роман Гордиенко",
        "Адилет Асканжоев",
        "Александр Шлейко",
        "Алена Батицкая",
        "Денис Ежков",
        "Владимир Чебукин",
        "Эдгар Нуруллин",
        "Евгений Шек",
        "Максим Филипенко",
        "Елена Никитина",
    ],
    [
        "Владимир Чебукин",
        "Эдгар Нуруллин",
        "Евгений Шек",
        "Валерий Хаслер",
        "Татьяна Тен",
        "Александр Фитискин",
        "Александр Шлейко",
        "Алена Батицкая",
        "Александр Беспоясов",
        "Денис Ежков",
        "Николай Лопин",
        "Михаил Ларченко",
    ],
]

def top3_names(mentors):
    all_names_list = [name.split()[0] for mentor_group in mentors for name in mentor_group]

    # Создаем словарь для подсчета количества упоминаний каждого имени
    name_counts = {}
    for name in all_names_list:
        if name in name_counts:
            name_counts[name] += 1
        else:
            name_counts[name] = 1

    # Сортируем имена по количеству упоминаний и, в случае равных количеств, по алфавиту
    sorted_names = sorted(name_counts.keys(), key=lambda x: (-name_counts[x], x))

    # Получаем топ-3 имен с количеством упоминаний
    top_3 = sorted_names[:3]

    # Формируем строку с топ-3 именами и их количеством упоминаний
    result = ", ".join([f"{name}: {name_counts[name]} раз(а)" for name in top_3])

    return result

