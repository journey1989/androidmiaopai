from base.config import REPORT_PATH,TEST_PATH
import unittest
from BeautifulReport import BeautifulReport as bf
from common.tools import *
import datetime




def report():

    nowtime = time.strftime('%Y%m%d %H%M%S')
    discover = unittest.defaultTestLoader.discover(TEST_PATH, 'AMP_*.py')
    report_name = '秒拍ui自动化测试报告' + str(nowtime)


    bf(discover).report(description='秒拍ui自动化测试报告', filename=report_name, report_dir=REPORT_PATH, theme='theme_cyan')


before_time = datetime.datetime.now()
log.debug('自动化开始时间%s' % before_time)
report()
curr_time = datetime.datetime.now()
log.debug('自动化结束时间%s' % curr_time)
test_finsih()
now = curr_time - before_time
log.debug('自动化使用：%s'% now)






