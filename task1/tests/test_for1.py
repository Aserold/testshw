from unittest import TestCase
from first_trainer import unique_names
import json


class TestTask(TestCase):
    def setUp(self):
        with open('mentors_data.json', 'r', encoding='utf-8') as json_file:
            self.data = json.load(json_file)
    
    def test_function(self):
        res = unique_names(self.data)
        expected = 'Уникальные имена преподавателей: Азамат, Александр, Алексей, Алена, Анатолий, Анна, Антон, Вадим, Евгений, Елена, Иван, Кирилл, Константин, Михаил, Николай, Олег, Павел, Ринат, Роман, Сергей, Татьяна, Эдгар, Юрий'
        self.assertMultiLineEqual(res, expected)

