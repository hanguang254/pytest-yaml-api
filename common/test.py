'''
@Project ：pytest-API-Project 
@File ：test.py
@Author ：le
@Date ：2022/8/19 10:25 
'''
from string import Template

import requests
import yaml

from common import ReadYaml
from common import get_token

# data = ReadYaml.ReadYaml().red_yaml('../data/token.yaml')
#
# # print(data)
# res_data = ReadYaml.ReadYaml().red_yaml('../data/CdkApi.yaml')




# with open('../data/CdkApi.yaml','r',encoding='utf-8')as f:
#     re = Template(f.read()).safe_substitute({'headers':data})
#     # 转换格式
#     result = yaml.safe_load(re)
# print(result)


# res = requests.request(url='https://dogechain.info/api/v1/block/4422432',method='GET').text
# print(res)


from web3 import Web3, HTTPProvider
from eth_account.messages import encode_defunct

private_key = "0x227dbb8586117d55284e26620bc76534dfbd2394be34cf4a09cb775d593b6f2b"
address = "0x5B38Da6a701c568545dCfcB03FcB875f56beddC4"
rpc = 'https://rpc.ankr.com/eth'
w3 = Web3(HTTPProvider(rpc))

#打包信息
msg = Web3.solidityKeccak(['address','uint256'], [address,0])
print(f"消息：{msg.hex()}")
#构造可签名信息
message = encode_defunct(hexstr=msg.hex())
#签名
signed_message = w3.eth.account.sign_message(message, private_key=private_key)
print(f"签名：{signed_message['signature'].hex()}")