# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : Huny
# @Email : hy546880109@qq.com
# @date  : 2020.12.08
# @Project: 云平台接口测试用例

import enum

class Conf(enum.Enum):
    '''
    环境配置枚举类
    '''
    # TEST_URL = 'http://192.168.1.15:9527/admin/v1.0'
    # TEST_URL = 'http://139.159.199.99:9527/admin/v1.0'
    TEST_URL = 'http://14.18.41.229:9527/admin/v1.0'

    # TEST_APP_URL = 'http://139.159.199.99:9527/api/v1.0'
    TEST_APP_URL = 'http://14.18.41.229:9527/api/v1.0'
    PROD_URL = ''

    SEND_EMAIL = 'hy546880109@qq.com'
    SEND_EMAIL_PASSWD = 'lwveldyrecfybdce'  #邮箱授权码
    TO_EMAIL = ['hy546880109@qq.com']
   
    foxmail = 'smtp.263.net'
    qqmail = 'smtp.qq.com'

    host = '14.18.41.229'
    port = 3306
    user = 'root'
    password = 'Root@2021'
    
    # host = '139.159.202.43'
    # port = 3306
    # user = 'root'
    # password = 'Antian!2020'



if __name__ == '__main__':
    print(Conf.TEST_URL)
    print(Conf.TEST_URL.value)
    print(','.join(Conf.TO_EMAIL.value))