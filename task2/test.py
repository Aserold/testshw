import requests
import time
from unittest import TestCase
from yandex_ts import create_folder


class TestYandex(TestCase):
    def setUp(self):
        self.url = 'https://cloud-api.yandex.net/v1/disk/resources'
        self.token = 'OAuth y0_AgAAAAAr95ioAADLWwAAAADlOs0-KEy73EtkQ3GOrhUhMQDjotaWkyw'
        self.foldname = 'TEST_TEST'
        
        
    def test_creating(self):
        expected = 201
        res = create_folder(self.token, self.foldname)
        self.assertEqual(expected, res)
        
    
    def tearDown(self):
        time.sleep(1)
        requests.delete(self.url, params={'path': self.foldname}, headers={"Authorization" : self.token})