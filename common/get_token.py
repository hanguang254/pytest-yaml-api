import pytest
import requests
import json
import jsonpath
from common import ReadYaml
from common import RequestsUitl


class login_Token():

    """
    :param data: yaml文件读取值

    """
    def get_token(self,data):

        try:
            method=ReadYaml.ReadYaml().get_method(data)      #请求方法
            url=ReadYaml.ReadYaml().get_url(data)            #请求地址
            get_data=ReadYaml.ReadYaml().get_data(data)      #请求参数
            # json格式响应
            result = RequestsUitl.RequestsUitl().requests_send(method=method,url=url,data=get_data).json()
            #通过jsonpath搜索键值对
            if jsonpath.jsonpath(result,'$..token') :
                #token值
                r=result['data']['token']
                token = {'X-token':r} #{直接引用到头部请求  # header}
                # print(token)
                #将token写入yaml文件
                ReadYaml.ReadYaml().writer_yaml('../data/token.yaml',{'X-token':r})
                return token
            else:
                print("无token值！")

        except Exception as e:
            print('错误原因：',e)




if __name__ == '__main__':
    api = ReadYaml.ReadYaml().red_yaml('../data/Alogin.yaml')
    print(api)
    res = login_Token().get_token(api)
    print(res)