'''
@Project ：pytest-API-Project 
@File ：conftest.py
@Author ：le
@Date ：2022/8/23 10:18 
'''
import pytest
from common import get_token
from common import ReadYaml


@pytest.fixture(scope='session')
def login_token():
    data  = ReadYaml.ReadYaml().red_yaml('../data/Alogin.yaml')
    # print(data)
    token = get_token.login_Token().get_token(data)

    yield token




if __name__ == '__main__':
    # login_token
    # print(s)
    pass