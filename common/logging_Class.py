# _*_ coding:utf-8 _*-
# @author：尹乐
import logging
import os
from logout import get_local
import time
class BasePage():

    def get_log(self):
        # 创建一个logger
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        filepath = get_local.get_cwd()
        print(filepath)

        # 设置日志存放路径，日志文件名
        # 获取本地时间，转换为设置的格式

        # 创建handler
        # 创建一个handler写入所有日志
        name = time.strftime("%Y%m%d%H%M%S", time.localtime())
        filename = filepath + "\All_log" + "\\" + name + ".log"

        fh = logging.FileHandler(filename, encoding='utf8')
        fh.setLevel(logging.INFO)
        # 创建一个handler写入错误日志
        filename = filepath + "\Error_log" + "\\" + name + ".log"
        eh = logging.FileHandler(filename, encoding="utf8")
        eh.setLevel(logging.ERROR)
        # 创建一个handler输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # 定义日志输出格式
        # 以时间-日志器名称-日志级别-日志内容的形式展示
        all_log_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        # 以时间-日志器名称-日志级别-文件名-函数行号-错误内容
        error_log_formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(module)s  - %(lineno)s - %(message)s')
        # 将定义好的输出形式添加到handler
        fh.setFormatter(all_log_formatter)
        ch.setFormatter(all_log_formatter)
        eh.setFormatter(error_log_formatter)

        # 给logger添加handler
        logger.addHandler(fh)
        logger.addHandler(eh)
        logger.addHandler(ch)

        return logger

        # 截图操作

    def get_windows_img(self):
        """
        在这里我们把file_path这个参数写死，直接保存到我们项目根目录的一个文件夹./testOutput/screenshots下
        """
        file_path = os.path.dirname(os.path.abspath('.'))
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        screen_name = file_path + r"\test_img\异常截图" + rq + '.png'
        print(screen_name)
        try:
            self.driver.get_screenshot_as_file(screen_name)
            return rq + '.png'
        except:
            self.logger.info("截图失败")
