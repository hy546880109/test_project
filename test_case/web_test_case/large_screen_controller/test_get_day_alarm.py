import unittest
from config.config_test import Conf
from common.http_requests import HttpRequests


class Test_Add_Task(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_URL.value
        cls.http = HttpRequests(cls.url)
        
    
    def test_add_task_success(self):
        '''日报警趋势成功用例：/large/screen/getDayAlarm'''
        response = Test_Add_Task.http.get('/large/screen/getDayAlarm')
        self.assertEqual(200,response.status_code,'返回非200')
        self.assertEqual(str(0), str(response.json()['code']),'日报警趋势失败')


if __name__ == '__main__':
    unittest.main()
