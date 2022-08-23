'''
@Project ：pytest-API-Project 
@File ：test.py
@Author ：le
@Date ：2022/8/19 10:25 
'''
from string import Template


import yaml

from common import ReadYaml
from common import get_token

data = ReadYaml.ReadYaml().red_yaml('../data/token.yaml')

# print(data)
res_data = ReadYaml.ReadYaml().red_yaml('../data/CdkApi.yaml')




with open('../data/CdkApi.yaml','r',encoding='utf-8')as f:
    re = Template(f.read()).safe_substitute({'headers':data})
    # 转换格式
    result = yaml.safe_load(re)
print(result)