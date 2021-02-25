from common.tools import *
from base.config import RECORDER_PATH
import unittest,string,random,yaml
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
auto_setup(__file__)



with open('%s/resourceid.yaml'%DATA_PATH) as f:
    yaml_data = yaml.load(f)


class TestSeting(unittest.TestCase):

    def setUp(self) -> None:
        pass




    def test_01_setting(self):
        '''设置：青少年模式'''
        sleep(10)
        log.info('=======设置==========')
        stars_app()
        recorder().start_recording(max_time=1800)
        poco(text='我的').click()
        poco(yaml_data['avatar']).click()
        sim_code_login()
        poco(yaml_data['back']).click()
        poco(yaml_data['setting_teenager']).click()
        poco(yaml_data['kids_mode']).click()
        for i in range(2):
            for j in range(4):
                poco(yaml_data['edit_text_view']).click()
                text("0")
        poco(yaml_data['password_next']).click()
        sleep(1)
        get_snapshot('青少年模式')
        poco(yaml_data['test_kids_mode_quit']).click()
        poco(yaml_data['kids_mode']).click()
        for i in range(1,5):
            poco(yaml_data['edit_text_view']).click()
            text("0")
        recorder().stop_recording(output='%s青少年模式.mp4' % RECORDER_PATH)

    def test_02_setting(self):
        '''设置：黑名单'''
        recorder().start_recording(max_time=1800)
        poco(text='我的').click()
        poco(yaml_data['back']).click()
        poco(yaml_data['setting_backlist']).click()
        sleep(1)
        get_snapshot('黑名单列表')
        if poco(yaml_data['remove']).exists():
            poco(yaml_data['remove']).click()
            poco(yaml_data['ok']).click()
            keyevent("KEYCODE_BACK")
        else:
            log.debug('======黑名单空空如也======')
            keyevent("KEYCODE_BACK")
        recorder().stop_recording(output='%s黑名单.mp4' % RECORDER_PATH)

    def test_03_setting(self):
        '''设置：我的钱包'''
        recorder().start_recording(max_time=1800)
        poco(yaml_data['setting_wallet']).click()
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
        recorder().stop_recording(output='%s我的钱包.mp4' % RECORDER_PATH)

    def test_04_setting(self):
        '''设置：检查更新'''
        recorder().start_recording(max_time=1800)
        poco(yaml_data['setting_check_update']).click()
        sleep(1)
        get_snapshot('检查更新')
        recorder().stop_recording(output='%s检查更新.mp4' % RECORDER_PATH)

    def test_05_setting(self):
        '''设置：隐私协议'''
        recorder().start_recording(max_time=1800)
        poco(yaml_data['setting_privacy']).click()
        sleep(1)
        get_snapshot('隐私协议')
        keyevent("KEYCODE_BACK")
        recorder().stop_recording(output='%s隐私协议.mp4' % RECORDER_PATH)

    def test_06_setting(self):
        '''设置：秒拍app声明'''
        recorder().start_recording(max_time=1800)
        poco(yaml_data['setting_app_statement']).click()
        sleep(1)
        get_snapshot('秒拍app声明')
        keyevent("KEYCODE_BACK")
        recorder().stop_recording(output='%s秒拍app声明.mp4' % RECORDER_PATH)

    def test_07_setting(self):
        '''设置：意见反馈'''
        recorder().start_recording(max_time=1800)
        poco(yaml_data['setting_feedback']).click()
        sleep(1)
        value = ''.join(random.sample(string.digits + string.ascii_letters, 10))
        number = ''.join(random.sample(string.digits + string.digits, 11))
        poco(yaml_data['feedback_suggestion']).set_text(value)
        poco(yaml_data['feedback_phone']).set_text(number)
        sleep(1)
        get_snapshot('意见反馈内容')
        poco(yaml_data['feedback_submit']).click()
        get_snapshot('提交意见反馈')
        recorder().stop_recording(output='%s提交意见反馈.mp4' % RECORDER_PATH)

    def test_08_setting(self):
        '''设置：清除缓存'''
        recorder().start_recording(max_time=1800)
        poco(yaml_data['setting_clear_cache']).click()
        poco(yaml_data['ok']).click()
        sleep(1)
        get_snapshot('清除缓存')
        recorder().stop_recording(output='%s清除缓存.mp4' % RECORDER_PATH)

    def test_09_setting(self):
        '''设置：高级设置'''
        recorder().start_recording(max_time=1800)
        poco(yaml_data['setting_additional_setting']).click()
        poco(yaml_data['setting_logoff']).click()
        sleep(1)
        get_snapshot('高级设置')
        keyevent("KEYCODE_BACK")
        keyevent("KEYCODE_BACK")
        recorder().stop_recording(output='%s高级设置.mp4' % RECORDER_PATH)

    def test_10_setting(self):
        '''设置：退出登录'''
        recorder().start_recording(max_time=1800)
        poco(yaml_data['setting_login']).click()
        poco(yaml_data['ok']).click()
        sleep(1)
        get_snapshot('退出登录')
        value = poco(yaml_data['login']).attr('text')
        assert_equal(value, '登录/注册', msg='退出登录')
        recorder().stop_recording(output='%s退出登录.mp4' % RECORDER_PATH)

    def tearDown(self) -> None:
        pass