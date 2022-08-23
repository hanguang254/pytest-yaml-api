
"""
封装request

"""

import os
import random
import requests

# 封装get和post
import logging


class RequestsHandler:

    def get_Req(self, url, params, **kw):
        """
        
        :param url: 请求的url地址
        :param params: 请求数据
        :param kw: 这个的传参需要为key=value(headers)
        :return:
        """
        # **kwargs是不定长参数，headers是放在这个不定长参数里
        # '''封装一个get方法，发送get请求'''
        try:  # 当处理不成功时，比如URL地址输入方式错误，或者接口超时timeout，需要抛出一个异常
            res = requests.get(url, params=params, **kw)

        except TimeoutError:
            # 会去捕获上面请求发送时的异常(请求不成功, 超时, 地址错误)
            # 记录日志信息，放入logger里边，这样我们就能知道问题出在哪里
            logging.error('访问不成功')
            
        else:
            # 未捕获到异常,则会将请求结果return返回出去
            return res

    def post_Req(self, url, data=None, json=None, **kw):
        """
        
        :param url: 请求url地址
        :param data: 传入data时, 请求格式为 form表单格式
        
        :param json: 传入JSON时, 请求格式为JSON格式
        :param kw: 这个的传参需要为key=value(headers)
        :return:
        """
        # '''封装一个post方法，发送post请求'''
        if data:
            logging.info("请求URL:{}\n 请求数据:{}".format(url,data))
        elif json:
            logging.info("请求URL:{}\n 请求数据:{}".format(url, json))
        try:  # 当处理不成功时，比如URL地址输入方式错误，或者接口超时timeout，需要抛出一个异常
            res = requests.post(url, data=data, json=json, **kw)  # 其中data是form表单形式的
        except TimeoutError:
            # 记录日志信息，放入logger里边，这样我们就能知道问题出在哪里
            logging.error('访问不成功')
        else:
            return res

    # vist方法是整合接口请求的方法
    def vist_Req(self, method, url, params=None, data=None, json=None, **kw):
        """
        
        :param method: 请求方式, get, post
        :param url: 请求的url地址
        :param params: get请求的请求数据
        :param data: post请求并且Content-Type : multipart/form-data的请求数据
        :param json: post请求并且Content-Type : application/json的请求数据
        :param kw:  这个的传参需要为key=value(headers)
        :return:
        """
        """访问接口"""
        # 'GET,如果传输进来的是大写的GET。可以使用lower方法'
        # '会将传进的method转为小写然后判断使用get请求还是post请求'
        if method.lower == 'get':
            return self.get_Req(url, params=params, **kw)
        elif method.lower == 'post':
            return self.post_Req(url, data=data, json=json, **kw)

        # 如果接口中还有其他的请求方式比如put,option之类色，可以用下方的方法，实际工作中常用的是get和post
        else:
            # '非get和post请求时会直接使用requests包的request方法'
            return requests.request(method, url, **kw)

    def json(self, method, url, params=None, data=None, json=None, **kw):  # json是要再vist方法下去进行进一步的处理
        """
        
        :param method: 请求方式
        :param url: 请求url
        :param params: get请求数据
        :param data:  post请求并且Content-Type : multipart/form-data的请求数据
        :param json:  post请求并且Content-Type : application/json的请求数据
        :param kw:    key=value格式数据
        :return:
        """
        """访问接口，获取json数据"""
        # 这个是可以直接使用jsonpath包解决
        
        res = self.vist_Req(url, method, params=params, data=data, json=json, **kw)
        # 获取json数据
        try:
            return res.json()
        except:
            # 记录日志信息
            logging.error('不是json格式的数据')




request = RequestsHandler()
