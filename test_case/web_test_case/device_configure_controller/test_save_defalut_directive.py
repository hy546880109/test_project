import unittest,os,sys,json

path = os.path.join(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(path)
from config.config_test import Conf
from common.http_requests import HttpRequests


class Test_Add_Task(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_URL.value
        cls.http = HttpRequests(cls.url)
        
    
    def test_add_task_success(self):
        '''恢复出厂设置成功用例：/device/config/saveDefalutDirective'''
        payload = {
        "terminalNos": ["123456789"]
        }
        payload = json.dumps(payload)
        response = Test_Add_Task.http.post('/device/config/saveDefalutDirective',data=payload)
        self.assertEqual(200,response.status_code,'返回非200')
        self.assertEqual(str(0), str(response.json()['code']),'恢复出厂设置失败')


if __name__ == '__main__':
    unittest.main()