from unittest import TestCase
from third_trainer import supername
import json


class TestTask(TestCase):
    def setUp(self):
        with open('mentors_data.json', 'r', encoding='utf-8') as json_file:
            self.data = json.load(json_file)
        
        self.courses = [
        "Python-разработчик с нуля",
        "Java-разработчик с нуля",
        "Fullstack-разработчик на Python",
        "Frontend-разработчик с нуля",
    ]
    
    def test_function(self):
        res = supername(self.courses, self.data)
        expected = f"На курсах 'Python-разработчик с нуля' и 'Java-разработчик с нуля' преподают: Александр, Анна, Олег. На курсах 'Python-разработчик с нуля' и 'Fullstack-разработчик на Python' преподают: Александр, Ринат. На курсах 'Python-разработчик с нуля' и 'Frontend-разработчик с нуля' преподают: Александр, Ринат, Сергей. На курсах 'Java-разработчик с нуля' и 'Fullstack-разработчик на Python' преподают: Александр, Алексей, Евгений, Константин, Роман, Юрий. На курсах 'Java-разработчик с нуля' и 'Frontend-разработчик с нуля' преподают: Александр, Евгений, Роман. На курсах 'Fullstack-разработчик на Python' и 'Frontend-разработчик с нуля' преподают: Александр, Алена, Антон, Евгений, Елена, Павел, Ринат, Роман, Татьяна. "
        self.assertMultiLineEqual(res, expected)
