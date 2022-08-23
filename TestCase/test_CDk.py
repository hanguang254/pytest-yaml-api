'''
@Project ：pytest-API-Project 
@File ：test_CDk.py
@Author ：le
@Date ：2022/8/23 10:36 
'''
import allure
import pytest
from common import ReadYaml
from common.RequestsUitl import RequestsUitl
from common import logging_Class


token = ReadYaml.ReadYaml().red_yaml('../data/token.yaml')
#替换接口需要的token值
All_api = ReadYaml.ReadYaml().template_yaml('../data/CdkApi.yaml',token)

# print(All_api)

@allure.feature('CDK接口测试')
class Test_CDK:

    def setup_class(self):
        self.log=logging_Class.BasePage().get_log()
        self.log.info('测试开始')
    def teardown_class(self):
        self.log.info('测试完成')


    @allure.story('CDK接口驱动')
    @pytest.mark.parametrize('key',All_api)
    def test_cdk(self,login_token,key):
        # x = key
        # print(x)

        #请求方法
        method = ReadYaml.ReadYaml().get_method(key)
        # 请求地址
        url = ReadYaml.ReadYaml().get_url(key)
        # 请求参数
        get_data = ReadYaml.ReadYaml().get_data(key)
        # 请求头
        header = ReadYaml.ReadYaml().get_headers(key)
        self.log.info('正在发送请求')

        res = RequestsUitl().requests_send(method=method,url=url,data=get_data,headers=header).json()
        self.log.info('响应结果：{}'.format(res))

        # print('响应结果:{}'.format(res))





if __name__ == '__main__':
    pytest.main(['test_CDk.py','-qsv'])