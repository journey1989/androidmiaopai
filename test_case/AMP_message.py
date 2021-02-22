from base.tools import *
import unittest, yaml
from base.config import RECORDER_PATH
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
auto_setup(__file__)

'''
消息模块

'''

with open('%s/resourceid.yaml'%DATA_PATH) as f:
    yaml_data = yaml.load(f)

class TestMessage(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def test_01_message(self):
        '''消息:打开通知开关再关闭'''
        stars_app()
        recorder().start_recording(max_time=1800)
        poco(text='消息').click()
        poco(text='登录/注册').click()
        sim_code_login()
        sleep(1)
        poco(text='系统通知').click()
        poco(yaml_data['setting']).click()
        poco(yaml_data['message_switch']).click()
        sleep(1)
        get_snapshot('打开通知开关')
        poco(yaml_data['message_switch']).click()
        sleep(1)
        get_snapshot('关闭通知开关')
        recorder().stop_recording(output='%s通知.mp4' % RECORDER_PATH)

    def test_02_message(self):
        '''消息:查看收到的赞'''
        recorder().start_recording(max_time=1800)
        keyevent("KEYCODE_BACK")
        keyevent("KEYCODE_BACK")
        sleep(1)
        poco(text='收到的赞').click()
        sleep(1)
        get_snapshot('消息:查看收到的赞')
        recorder().stop_recording(output='%s收到的赞.mp4' % RECORDER_PATH)

    def test_03_message(self):
        '''消息:查看粉丝关注'''
        recorder().start_recording(max_time=1800)
        keyevent("KEYCODE_BACK")
        poco(text='粉丝关注').click()
        sleep(1)
        get_snapshot('消息:查看粉丝关注')
        recorder().stop_recording(output='%s粉丝关注.mp4' % RECORDER_PATH)

    def test_04_message(self):
        '''消息:查看评论回复'''
        recorder().start_recording(max_time=1800)
        keyevent("KEYCODE_BACK")
        poco(text='评论回复').click()
        sleep(1)
        get_snapshot('消息:查看评论回复')
        if poco(yaml_data['cover']).exists():
            poco(yaml_data['cover']).click()
            sleep(2)
            keyevent("KEYCODE_BACK")
        else:
            keyevent("KEYCODE_BACK")
        recorder().stop_recording(output='%s评论回复.mp4' % RECORDER_PATH)







    def tearDown(self) -> None:
        pass