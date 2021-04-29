import os,nnlog,time,sys
'''
配置路径
'''
sys.path.append(r'/Users/yixia/PycharmProjects/bobo/venv/lib/python3.6/site-packages')
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LOG_PATH = os.path.join(BASE_PATH, 'log')
REPORT_PATH = os.path.join(BASE_PATH, 'allure-report')
SNAPSHOT_PATH = os.path.join(BASE_PATH, 'snapshot/')
TEST_PATH = os.path.join(BASE_PATH, 'testCase/')
DATA_PATH = os.path.join(BASE_PATH, 'data')

nowtime = time.strftime('%Y%m%d %H%M%S')
RECORDER_PATH = os.path.join(BASE_PATH , 'recorder' + '/'+ nowtime)
logname = os.path.join(LOG_PATH, 'logs.txt')

log = nnlog.Logger(file_name=logname, level='debug', when='D')