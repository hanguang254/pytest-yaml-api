'''
@Project ：pytest-API-Project 
@File ：test_login_api.py
@Author ：le
@Date ：2022/8/19 14:10 
'''
import allure
import pytest
from common import ReadYaml
from common import RequestsUitl
from common import logging_Class
from common import AllureRun



#全部用例到时候封装为一个类方法
api=ReadYaml.ReadYaml().red_yaml('../data/LoginApi.yaml')

@allure.feature("登录接口")
class Test_login:

    def setup_class(self):
        self.log= logging_Class.BasePage().get_log()
        self.log.info('测试开始')
    def teardown_class(self):
        self.log.info('测试完成')

    @allure.story('登录自动化')
    @pytest.mark.parametrize('key',api)
    def test_login_api(self,key):
        # 请求方法
        method = ReadYaml.ReadYaml().get_method(key)
        # 请求地址
        url = ReadYaml.ReadYaml().get_url(key)
        #请求参数
        get_data= ReadYaml.ReadYaml().get_data(key)
        # 期望值
        expected = ReadYaml.ReadYaml().get_expected(key)
        r = expected['code']
        self.log.info('预期结果：{}'.format(r))
        self.log.info('正在请求')
        res = RequestsUitl.RequestsUitl().requests_send(method=method,url=url,data=get_data).json()
        self.log.info('实际结果：{}'.format(res['code']))
        try:
            assert r == res['code']

        except Exception as e:

            self.log.error('断言错误:{}'.format(e))
            #raise 断言错误， 爆出用例运行失败
            raise




if __name__ == '__main__':

    AllureRun.AllureRun().Run_allure('test_login_api.py')