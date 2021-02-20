import os,nnlog
'''
配置路径
'''

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LOG_PATH = os.path.join(BASE_PATH, 'log')
REPORT_PATH = os.path.join(BASE_PATH, 'report/')
SNAPSHOT_PATH = os.path.join(BASE_PATH, 'snapshot/')
TEST_PATH =  os.path.join(BASE_PATH, 'test_case/')
DATA_PATH = os.path.join(BASE_PATH, 'data')

logname = os.path.join(LOG_PATH, 'logs.txt')

log = nnlog.Logger(file_name=logname, level='debug', when='D')


print(DATA_PATH)



print(logname)