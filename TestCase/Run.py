'''
@Project ：pytest-API-Project 
@File ：Run.py
@Author ：le
@Date ：2022/8/25 14:23 
'''
import os
import pytest


if __name__ == '__main__':
    pytest.main()
    os.system("allure generate ../test_Report/json –o ../test_Report/report_test --clean")
