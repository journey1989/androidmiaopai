from common.tools import *
import allure, yaml
from base.config import RECORDER_PATH

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
auto_setup(__file__)

with open('%s/resourceid.yaml' % DATA_PATH) as f:
    yaml_data = yaml.load(f)


@allure.feature('遍历APP青少年模块')
class TestTeenager:
    def setUp(self) -> None:
        pass

    @allure.story('青少年模式：首次启动进入青少年模式')
    @allure.title('青少年模式：首次启动进入青少年模式')
    def test_01_teenager(self):

        sleep(10)
        log.info('=======青少年==========')
        recorder().start_recording(max_time=1800)
        teenager_mode()
        sleep(1)
        for i in range(2):
            for j in range(4):
                poco(yaml_data['text_view']).click()
                text("0")
        poco(yaml_data['password_next']).click()
        sleep(1)
        get_snapshot('青少年模式')
        recorder().stop_recording(output='%s首次启动进入青少年.mp4' % RECORDER_PATH)

    @allure.story('青少年模式：滑动10条数据并播放视频')
    @allure.title('青少年模式：滑动10条数据并播放视频')
    def test_02_teenager(self):

        recorder().start_recording(max_time=1800)
        if poco().exists():
            for i in range(1, 21):
                swipe((561, 1686), (561, 245))
                poco(yaml_data['play']).click()
                sleep(5)
                print('已滑动%s次' % i)
        else:
            sleep(1)
            get_snapshot('青少年无视频数据')
            sleep(1)
            poco(yaml_data['test_kids_mode_quit']).click()
            poco(yaml_data['kids_mode']).click()
            for j in range(4):
                poco(yaml_data['edit_text_view']).click()
                text("0")
            log.error('=======暂停青少年自动化测试======')
        recorder().stop_recording(output='%s播放10条数据.mp4' % RECORDER_PATH)

    @allure.story('青少年模式：列表页面元素点击')
    @allure.title('青少年模式：列表页面元素点击')
    def test_03_teenager(self):
        recorder().start_recording(max_time=1800)
        poco(yaml_data['avatar']).click()  # 头像
        poco(yaml_data['name']).click()  # 名称
        poco(yaml_data['follow']).click()  # 关注
        poco(yaml_data['praise']).click()  # 点赞
        poco(text='分享').click()
        recorder().stop_recording(output='%s列表元素点击.mp4' % RECORDER_PATH)

    @allure.story('退出青少年模式')
    @allure.title('退出青少年模式')
    def test_04_teenager(self):

        recorder().start_recording(max_time=1800)
        poco(yaml_data['test_kids_mode_quit']).click()
        poco(yaml_data['kids_mode']).click()
        for j in range(4):
            poco(yaml_data['edit_text_view']).click()
            text("0")
        sleep(1)
        get_snapshot('退出青少年模式')
        recorder().stop_recording(output='%s退出青少年模式.mp4' % RECORDER_PATH)

    def tearDown(self) -> None:
        pass
