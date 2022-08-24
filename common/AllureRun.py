'''
@Project ：pytest-API-Project 
@File ：AllureRun.py
@Author ：le
@Date ：2022/8/22 15:05 
'''
import os
import pytest



class AllureRun():


    """
    Allure报告运行方法
    """
    def Run_allure(self,test_filename):
        """
        :param test_filename:  测试文件名字包括后缀(示例：test_login.py)
        :return:
        """
        try:
            result_dir = "../test_Report/json"  # json存储位置
            report_dir = "../test_Report/report_test"  # 报告存储位置
            pytest.main(["-qs", "--alluredir=%s" % result_dir, "--clean-alluredir", test_filename])
            os.system("allure generate --clean %s -o %s" % (result_dir, report_dir))
            print('报告已生成至{}'.format(report_dir))
        except Exception :
            print('错误：{}'.format(Exception))