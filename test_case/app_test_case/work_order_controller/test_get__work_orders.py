from common.login_token import get_token
import unittest
import json
from config.config_test import Conf
from common.http_requests import HttpRequests
from common.mysql_data import Mysql_connet


class Test_Get_Index(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_APP_URL.value
        cls.http = HttpRequests(cls.url)
        cls.mysql = Mysql_connet('device')
        cls.mysql.insert_device()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.mysql.delete_device()

    def test_get_index_success(self):
        """根据工单ID获取窖井信息成功用例: /work/order/getAppCellarWellDetail"""
        payload = {
            "id": self.mysql.work_order_id,
        }
        headers = {'Content-Type': 'application/json','token': get_token()}
        response = Test_Get_Index.http.get('/work/order/getAppCellarWellDetail', params=payload, headers=headers)
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertEqual(str(0), str(response.json()['code']), '根据工单ID获取窖井信息失败')


if __name__ == '__main__':
    unittest.main()
