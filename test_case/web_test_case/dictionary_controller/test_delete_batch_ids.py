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
        '''批量删除字典值成功用例：/dictionary/deleteBatchIds'''
        payload  =  [1404994626598809602]
        payload = json.dumps(payload)
        
        headers = {'Content-Type': 'application/json'}
        response = Test_Add_Task.http.post('/dictionary/deleteBatchIds',data=payload,headers=headers)
        self.assertEqual(200,response.status_code,'返回非200')
        self.assertEqual(str(0), str(response.json()['code']),'批量删除字典值失败')


if __name__ == '__main__':
    unittest.main()
