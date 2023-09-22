from unittest import TestCase
from second_trainer import top3_names
import json


class TestTask(TestCase):
    def setUp(self):
        with open('mentors_data.json', 'r', encoding='utf-8') as json_file:
            self.data = json.load(json_file)
    
    def test_function(self):
        res = top3_names(self.data)
        expected = 'Александр: 5 раз(а), Евгений: 4 раз(а), Ринат: 3 раз(а)'
        self.assertMultiLineEqual(res, expected)
