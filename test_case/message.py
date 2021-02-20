from base.tools import *
import unittest,string,random
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
auto_setup(__file__)

'''
消息模块

'''
class TestMessage(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def test_01_message(self):
        '''消息:打开通知开关再关闭'''
        stars_app()
        poco(text='消息').click()
        poco(text='登录/注册').click()
        sim_code_login()
        sleep(1)
        poco(text='系统通知').click()
        poco('com.yixia.videoeditor:id/btn_setting').click()
        poco('com.yixia.videoeditor:id/btn_message_switch').click()
        sleep(1)
        get_snapshot('打开通知开关')
        poco('com.yixia.videoeditor:id/btn_message_switch').click()
        sleep(1)
        get_snapshot('关闭通知开关')

    def test_02_message(self):
        '''消息:查看收到的赞'''
        keyevent("KEYCODE_BACK")
        keyevent("KEYCODE_BACK")
        sleep(1)
        poco(text='收到的赞').click()
        sleep(1)
        get_snapshot('消息:查看收到的赞')

    def test_03_message(self):
        '''消息:查看粉丝关注'''
        keyevent("KEYCODE_BACK")
        poco(text='粉丝关注').click()
        sleep(1)
        get_snapshot('消息:查看粉丝关注')

    def test_04_message(self):
        '''消息:查看评论回复'''
        keyevent("KEYCODE_BACK")
        poco(text='评论回复').click()
        sleep(1)
        get_snapshot('消息:查看评论回复')
        if poco('com.yixia.videoeditor:id/iv_cover').exists():
            poco('com.yixia.videoeditor:id/iv_cover').click()
            sleep(2)
            keyevent("KEYCODE_BACK")
        else:
            keyevent("KEYCODE_BACK")







    def tearDown(self) -> None:
        pass