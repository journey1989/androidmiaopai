from base.config import REPORT_PATH,TEST_PATH
import time,unittest,os
from BeautifulReport import BeautifulReport as bf
from base.tools import *


def report():

    nowtime = time.strftime('%Y%m%d %H%M%S')
    discover = unittest.defaultTestLoader.discover(TEST_PATH, 'player.py')
    report_name = '秒拍ui自动化测试报告' + str(nowtime)


    bf(discover).report(description='秒拍ui自动化测试报告', filename=report_name, report_dir=REPORT_PATH, theme='theme_cyan')



report()
test_finsih()




