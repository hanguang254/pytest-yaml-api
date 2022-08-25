'''
@Project ：pytest-API-Project 
@File ：test_CDk.py
@Author ：le
@Date ：2022/8/23 10:36 
'''
import os
import sys
import allure
import pytest
from common import ReadYaml
from common.RequestsUitl import RequestsUitl
from common import Logger
from common.AllureRun import AllureRun
from common.get_token import login_Token


# 替换接口需要的token
api =login_Token().template_token('../data/Alogin.yaml','../data/CdkApi.yaml')


@allure.feature('CDK接口测试')
class Test_CDK:


    def setup_class(self):
        self.file=os.path.basename(sys.argv[0])
        self.log=Logger.Log(self.file).Logger()
        self.log.info('测试开始')

    def teardown_class(self):
        self.log.info('测试完成')

    @allure.story('CDK接口驱动')
    @pytest.mark.parametrize('key',api)
    def test_cdk(self,key):
        # print(key)

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

        try:
            assert res['code'] == 20000

        except AssertionError as a:
            self.log.error('断言错误：{}'.format(a))
            # raise 断言错误， 爆出用例运行失败
            raise




if __name__ == '__main__':
    # pytest.main(['test_CDk.py','-qsv'])
    AllureRun().Run_allure('test_CDk.py')