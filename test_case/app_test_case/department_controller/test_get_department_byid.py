from common.mysql_data import Mysql_connet
from common.login_token import get_token
import unittest,os,sys

from requests.api import head

path = os.path.join(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(path)
from config.config_test import Conf
from common.http_requests import HttpRequests


class Test_Add_Task(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_APP_URL.value
        cls.http = HttpRequests(cls.url)
        cls.mysql = Mysql_connet('device')
        cls.mysql.insert_user()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.mysql.delete_user()
        cls.mysql.close()  
    
    def test_add_task_success(self):
        '''根据ID获取部门成功用例：/department/getDepartmentById'''
        payload  = {"id":self.mysql.department_id}
        headers = {'token': get_token()}
        response = Test_Add_Task.http.get('/department/getDepartmentById',params=payload, headers=headers)
        self.assertEqual(200,response.status_code,'返回非200')
        self.assertEqual(str(0), str(response.json()['code']),'根据ID获取部门失败')


if __name__ == '__main__':
    unittest.main()
