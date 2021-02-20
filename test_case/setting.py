from base.tools import *
import unittest,string,random
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
auto_setup(__file__)



class TestSting(unittest.TestCase):

    def setUp(self) -> None:
        pass


    def test_01_setting(self):
        '''设置：青少年模式'''
        stars_app()
        poco(text='我的').click()
        poco('com.yixia.videoeditor:id/iv_avatar').click()
        sim_code_login()
        poco('com.yixia.videoeditor:id/btn_back').click()
        poco('com.yixia.videoeditor:id/tv_setting_teenager').click()
        poco('com.yixia.videoeditor:id/btn_kids_mode').click()
        for i in range(2):
            for j in range(4):
                poco('com.yixia.videoeditor:id/edit_text_view').click()
                text("0")
        poco('com.yixia.videoeditor:id/btn_password_next').click()
        sleep(1)
        get_snapshot('青少年模式')
        poco('com.yixia.videoeditor:id/test_kids_mode_quit').click()
        poco('com.yixia.videoeditor:id/btn_kids_mode').click()
        for i in range(1,5):
            poco('com.yixia.videoeditor:id/edit_text_view').click()
            text("0")

    def test_02_setting(self):
        '''设置：黑名单'''
        poco(text='我的').click()
        poco('com.yixia.videoeditor:id/btn_back').click()
        poco('com.yixia.videoeditor:id/cl_setting_blacklist').click()
        sleep(1)
        get_snapshot('黑名单列表')
        if poco('com.yixia.videoeditor:id/btn_remove'):
            poco('com.yixia.videoeditor:id/btn_remove').click()
            poco('com.yixia.videoeditor:id/btn_ok').click()
            keyevent("KEYCODE_BACK")
        else:
            keyevent("KEYCODE_BACK")

    def test_03_setting(self):
        '''设置：我的钱包'''
        poco('com.yixia.videoeditor:id/cl_setting_wallet').click()
        poco(text='常见问题').click()
        sleep(1)
        get_snapshot('常见问题')
        keyevent("KEYCODE_BACK")
        poco(text='立即提现').click()
        sleep(1)
        get_snapshot('立即提现')
        poco(text='账单').click()
        sleep(1)
        get_snapshot('账单')
        keyevent("KEYCODE_BACK")
        keyevent("KEYCODE_BACK")
        keyevent("KEYCODE_BACK")

    def test_04_setting(self):
        '''设置：检查更新'''
        poco('com.yixia.videoeditor:id/cl_setting_check_update').click()
        sleep(1)
        get_snapshot('检查更新')

    def test_05_setting(self):
        '''设置：隐私协议'''
        poco('com.yixia.videoeditor:id/cl_setting_privacy').click()
        sleep(1)
        get_snapshot('隐私协议')
        keyevent("KEYCODE_BACK")

    def test_06_setting(self):
        '''设置：秒拍app声明'''
        poco('com.yixia.videoeditor:id/cl_setting_app_statement').click()
        sleep(1)
        get_snapshot('秒拍app声明')
        keyevent("KEYCODE_BACK")

    def test_07_setting(self):
        '''设置：意见反馈'''
        poco('com.yixia.videoeditor:id/cl_setting_feedback').click()
        sleep(1)
        value = ''.join(random.sample(string.digits + string.ascii_letters, 10))
        number = ''.join(random.sample(string.digits + string.digits, 11))
        poco('com.yixia.videoeditor:id/et_feedback_suggestion').set_text(value)
        poco('com.yixia.videoeditor:id/et_feedback_phone').set_text(number)
        sleep(1)
        get_snapshot('意见反馈内容')
        poco('com.yixia.videoeditor:id/tv_feedback_submit').click()
        get_snapshot('提交意见反馈')

    def test_08_setting(self):
        '''设置：清除缓存'''
        poco('com.yixia.videoeditor:id/cl_setting_clear_cache').click()
        poco('com.yixia.videoeditor:id/btn_ok').click()
        sleep(1)
        get_snapshot('清除缓存')

    def test_09_setting(self):
        '''设置：高级设置'''
        poco('com.yixia.videoeditor:id/cl_setting_additional_setting').click()
        poco('com.yixia.videoeditor:id/tv_setting_logoff').click()
        sleep(1)
        get_snapshot('高级设置')
        keyevent("KEYCODE_BACK")
        keyevent("KEYCODE_BACK")

    def test_10_setting(self):
        '''设置：退出登录'''
        poco('com.yixia.videoeditor:id/tv_setting_logout').click()
        poco('com.yixia.videoeditor:id/btn_ok').click()
        sleep(1)
        get_snapshot('退出登录')
        value = poco('com.yixia.videoeditor:id/btn_login').attr('text')
        assert_equal(value, '登录/注册', msg='退出登录')

    def tearDown(self) -> None:
        pass