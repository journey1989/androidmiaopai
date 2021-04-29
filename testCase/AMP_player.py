from base.config import RECORDER_PATH
from common.tools import *
import allure, yaml , sys


poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
auto_setup(__file__)

with open('%s/resourceid.yaml' % DATA_PATH) as f:
    yaml_data = yaml.load(f)


@allure.feature('遍历APP播放模块')
class TestPlayer:

    def setup(self) -> None:
        pass

    @allure.title('精选：列表和全屏来回切换播放10条视频')
    @allure.story('精选：列表和全屏来回切换播放10条视频')
    def test_01_player(self):
        sleep(10)
        log.info('=======播放器==========')
        stars_app()
        recorder().start_recording(max_time=1800)
        for i in range(1, 21):
            poco(yaml_data['play']).click()
            sleep(5)
            poco(yaml_data['des']).click()
            sleep(3)
            poco(yaml_data['back']).click()
            sleep(1)
            swipe((561, 1686), (561, 260))
        recorder().stop_recording(output='%s列表和全屏来回切换播放10条视频.mp4' % RECORDER_PATH)

    @allure.title('精选：列表播放10条视频')
    @allure.story('精选：列表播放10条视频')
    def test_02_player(self):
        recorder().start_recording(max_time=1800)
        for i in range(1, 21):
            poco(yaml_data['play']).click()
            sleep(5)
            swipe((561, 1600), (561, 260))
        recorder().stop_recording(output='%s精选列表播放10条视频.mp4' % RECORDER_PATH)

    @allure.title('关注：列表播放15条视频')
    @allure.story('关注：列表播放15条视频')
    def test_03_player(self):
        recorder().start_recording(max_time=1800)
        poco(yaml_data['follow']).click()
        sim_code_login()
        sleep(1)
        poco(text='关注').click()
        if poco(yaml_data['play']).exists():
            for i in range(1, 21):
                poco(yaml_data['play']).click()
                sleep(5)
                swipe((561, 1600), (561, 260))
        else:
            log.debug('=====无视频，不需要操作=====')
        recorder().stop_recording(output='%s关注列表播放5条视频.mp4' % RECORDER_PATH)

    @allure.title('精选：全屏播放10条视频')
    @allure.story('精选：全屏播放10条视频')
    def test_04_player(self):

        recorder().start_recording(max_time=1800)
        poco(text='精选').click()
        poco(yaml_data['des']).click()
        for i in range(1, 21):
            sleep(5)
            swipe((561, 1600), (561, 260))
        poco(yaml_data['horizontal_screen']).click()
        recorder().stop_recording(output='%s全屏播放10条视频.mp4' % RECORDER_PATH)

    @allure.title('精选：横屏播放15条视频')
    @allure.story('精选：横屏播放15条视频')
    def test_05_player(self):

        recorder().start_recording(max_time=1800)
        for i in range(1, 21):
            sleep(5)
            swipe((1120, 926), (1120, 220))
        keyevent("KEYCODE_BACK")
        keyevent("KEYCODE_BACK")
        recorder().stop_recording(output='%s横屏播放10条视频.mp4' % RECORDER_PATH)

    @allure.title('沉浸式：顶部滑动5条+播放10条视频')
    @allure.story('沉浸式：顶部滑动5条+播放10条视频')
    def test_06_player(self):

        recorder().start_recording(max_time=1800)
        stop_app('com.yixia.videoeditor')
        start_app('com.yixia.videoeditor')
        poco(text='关注').click()
        poco(yaml_data['avatar'])[0].click()
        for i in range(1, 5):
            for j in range(1, 5):
                if poco(yaml_data['avatar']).exists():
                    poco(yaml_data['avatar'])[i].click()
                    sleep(3)
                    swipe((561, 1686), (561, 245))
                    sleep(2)
                else:
                    log.debug('=====无更多视频======')
        keyevent("KEYCODE_BACK")
        recorder().stop_recording(output='%s沉浸式顶部滑动5条+播放10条视频.mp4' % RECORDER_PATH)

    @allure.title('发现：种草播放3条视频')
    @allure.story('发现：种草播放3条视频')
    def test_07_player(self):

        recorder().start_recording(max_time=1800)
        stop_app('com.yixia.videoeditor')
        start_app('com.yixia.videoeditor')
        poco(text='发现').click()
        if poco(text='种草').exists():
            poco(text='种草').click()
            for i in range(10):
                if poco(yaml_data['cover']).exists():
                    poco(yaml_data['cover'])[i].long_click()
                    sleep(3)
                    poco(yaml_data['back']).click()
                else:
                    log.debug('======种草视频已被刷完=====')
        else:
            log.debug('======种草视频已下线======')
        sleep(1)
        get_snapshot('发现种草')
        recorder().stop_recording(output='%s种草播放5条视频.mp4' % RECORDER_PATH)

    @allure.title('发现：最炫乡风播放3条视频')
    @allure.story('发现：最炫乡风播放3条视频')
    def test_8_player(self):
        recorder().start_recording(max_time=1800)
        if poco(text='最炫乡风').exists():
            poco(text='最炫乡风').click()
            for i in range(6):
                if poco(yaml_data['cover']).exists():
                    poco(yaml_data['layout']).offspring(yaml_data['host']).child(yaml_data['group']) \
                        .child(yaml_data['pager']).child(yaml_data['group']).offspring(yaml_data['view']) \
                        .child(yaml_data['group'])[i].child(yaml_data['cover']).click()
                    sleep(3)
                    poco(yaml_data['back']).click()
                    i += 1
                    if i == 4:
                        sleep(1)
                        log.debug('当前第%s次' % i)
                        swipe((561, 1600), (561, 260))

                else:
                    log.debug('======最炫乡风已下线=====')
        poco(text='最新').click()
        for i in range(5):
            poco(yaml_data['layout']).offspring(yaml_data['host']).child(yaml_data['group']) \
                .child(yaml_data['pager']).child(yaml_data['group']).offspring(yaml_data['view']) \
                .child(yaml_data['group'])[i].child(yaml_data['cover']).click()
            sleep(3)
            poco(yaml_data['back']).click()
        sleep(1)
        get_snapshot('最炫乡风')
        recorder().stop_recording(output='%s最炫乡风.mp4' % RECORDER_PATH)

    @allure.title('发现：三农播放3条视频')
    @allure.story('发现：三农播放3条视频')
    def test_09_player(self):

        recorder().start_recording(max_time=1800)
        if poco(text='三农').exists():
            poco(text='三农').click()
            for i in range(10):
                if poco(yaml_data['cover']).exists():
                    poco(yaml_data['cover'])[i].long_click()
                    sleep(3)
                    poco(yaml_data['back']).click()
                else:
                    log.debug('======三农视频已被刷完=====')
        else:
            log.debug('=======生活类视频已下线======')
        sleep(1)
        get_snapshot('发现三农')
        recorder().stop_recording(output='%s三农播放5条视频.mp4' % RECORDER_PATH)

    @allure.title('发现：汽车播放3条视频')
    @allure.story('发现：汽车播放3条视频')
    def test_10_player(self):

        recorder().start_recording(max_time=1800)
        if poco(text='汽车').exists():
            poco(text='汽车').click()
            for i in range(10):
                if poco(yaml_data['cover']).exists():
                    poco(yaml_data['cover'])[i].long_click()
                    sleep(3)
                    poco(yaml_data['back']).click()
                else:
                    log.debug('======汽车视频已被刷完=====')
        else:
            log.debug('======汽车类视频已下线======')
        sleep(1)
        get_snapshot('发现汽车')
        recorder().stop_recording(output='%s汽车播放5条视频.mp4' % RECORDER_PATH)

    @allure.title('发现：生活播放3条视频')
    @allure.story('发现：生活播放3条视频')
    def test_11_player(self):

        recorder().start_recording(max_time=1800)
        if poco(text='生活').exists():
            poco(text='生活').click()
            for i in range(10):
                if poco(yaml_data['cover']).exists():
                    poco(yaml_data['cover'])[i].long_click()
                    sleep(3)
                    poco(yaml_data['back']).click()
                else:
                    log.debug('======生活视频已被刷完=====')
        else:
            log.debug('=======生活类视频已下线======')
        sleep(1)
        get_snapshot('发现生活')
        recorder().stop_recording(output='%s生活播放5条视频.mp4' % RECORDER_PATH)

    @allure.title('发现：影视播放3条视频')
    @allure.story('发现：影视播放3条视频')
    def test_12_player(self):

        recorder().start_recording(max_time=1800)
        if poco(text='影视').exists():
            poco(text='影视').click()
            for i in range(10):
                if poco(yaml_data['cover']).exists():
                    poco(yaml_data['cover'])[i].long_click()
                    sleep(3)
                    poco(yaml_data['back']).click()
                else:
                    log.debug('======影视视频已被刷完=====')
        else:
            log.debug('=======影视视频类已下线======')
        sleep(1)
        get_snapshot('发现影视')
        recorder().stop_recording(output='%s影视播放5条视频.mp4' % RECORDER_PATH)

    @allure.title('发现：社会播放3条视频')
    @allure.story('发现：社会播放3条视频')
    def test_13_player(self):

        recorder().start_recording(max_time=1800)
        if poco(text='社会').exists():
            poco(text='社会').click()
            for i in range(10):
                if poco(yaml_data['cover']).exists():
                    poco(yaml_data['cover'])[i].long_click()
                    sleep(3)
                    poco(yaml_data['back']).click()
                else:
                    log.debug('======社会视频已被刷完=====')
        else:
            log.debug('=======社会类视频已下线=====')
        sleep(1)
        get_snapshot('发现社会')
        recorder().stop_recording(output='%s社会播放5条视频.mp4' % RECORDER_PATH)

    @allure.title('发现：美食播放3条视频')
    @allure.story('发现：美食播放3条视频')
    def test_14_player(self):

        recorder().start_recording(max_time=1800)
        if poco(text='美食').exists():
            poco(text='美食').click()
            for i in range(10):
                if poco(yaml_data['cover']).exists():
                    poco(yaml_data['cover'])[i].long_click()
                    sleep(3)
                    poco(yaml_data['back']).click()
                else:
                    log.debug('======美食视频已被刷完=====')
        else:
            log.debug('======美食类视频已下线======')
        sleep(1)
        get_snapshot('发现美食')
        recorder().stop_recording(output='%s美食播放5条视频.mp4' % RECORDER_PATH)

    @allure.title('发现：旅行播放3条视频')
    @allure.story('发现：旅行播放3条视频')
    def test_15_player(self):

        recorder().start_recording(max_time=1800)
        if poco(text='旅行').exists():
            poco(text='旅行').click()
            for i in range(10):
                if poco(yaml_data['cover']).exists():
                    poco(yaml_data['cover'])[i].long_click()
                    sleep(3)
                    poco(yaml_data['back']).click()
                else:
                    log.debug('======旅行视频已被刷完=====')
        else:
            log.debug('======旅行类视频已下线=======')
        sleep(1)
        get_snapshot('发现旅行')
        recorder().stop_recording(output='%s旅行播放5条视频.mp4' % RECORDER_PATH)

    @allure.title('发现：抗击疫情播放3条视频')
    @allure.story('发现：抗击疫情播放3条视频')
    def test_16_player(self):

        recorder().start_recording(max_time=1800)
        if poco(text='抗击疫情').exists():
            poco(text='抗击疫情').click()
            for i in range(6):
                if poco(yaml_data['cover']).exists():
                    poco(yaml_data['layout']).offspring(yaml_data['host']).child(yaml_data['group']) \
                        .child(yaml_data['pager']).child(yaml_data['group']).offspring(yaml_data['view']) \
                        .child(yaml_data['group'])[i].child(yaml_data['cover']).click()
                    sleep(3)
                    poco(yaml_data['back']).click()
                    i += 1
                    if i == 4:
                        sleep(1)
                        log.debug('当前第%s次' % i)
                        swipe((561, 1600), (561, 260))

                else:
                    log.debug('======抗击疫情已下线=====')
        poco(text='最新').click()
        for i in range(5):
            poco(yaml_data['layout']).offspring(yaml_data['host']).child(yaml_data['group']) \
                .child(yaml_data['pager']).child(yaml_data['group']).offspring(yaml_data['view']) \
                .child(yaml_data['group'])[i].child(yaml_data['cover']).click()
            sleep(3)
            poco(yaml_data['back']).click()
        sleep(1)
        get_snapshot('抗击疫情')
        recorder().stop_recording(output='%s抗击疫情.mp4' % RECORDER_PATH)

    @allure.title('发现：网络过年播放3条视频')
    @allure.story('发现：网络过年播放3条视频')
    def test_17_player(self):

        recorder().start_recording(max_time=1800)
        if poco(text='网络过年').exists():
            poco(text='网络过年').click()
            for i in range(6):
                if poco(yaml_data['cover']).exists():
                    poco(yaml_data['layout']).offspring(yaml_data['host']).child(yaml_data['group']) \
                        .child(yaml_data['pager']).child(yaml_data['group']).offspring(yaml_data['view']) \
                        .child(yaml_data['group'])[i].child(yaml_data['cover']).click()
                    sleep(3)
                    poco(yaml_data['back']).click()
                    i += 1
                    if i == 4:
                        sleep(1)
                        log.debug('当前第%s次' % i)
                        swipe((561, 1600), (561, 260))

                else:
                    log.debug('======网络过年已下线=====')

        poco(text='最新').click()
        for i in range(5):
            poco(yaml_data['layout']).offspring(yaml_data['host']).child(yaml_data['group']) \
                .child(yaml_data['pager']).child(yaml_data['group']).offspring(yaml_data['view']) \
                .child(yaml_data['group'])[i].child(yaml_data['cover']).click()
            sleep(3)
            poco(yaml_data['back']).click()
        sleep(1)
        get_snapshot('网络过年')
        recorder().stop_recording(output='%s网络过年.mp4' % RECORDER_PATH)

    # @allure.title('发现：春暖中国播放3条视频')
    # @allure.story('发现：春暖中国播放3条视频')
    # def test_18_player(self):
    #
    #     recorder().start_recording(max_time=1800)
    #     stop_app('com.yixia.videoeditor')
    #     start_app('com.yixia.videoeditor')
    #     poco(text='发现').click()
    #     if poco(text='春暖中国').exists():
    #         poco(text='春暖中国').click()
    #         for i in range(6):
    #             if poco(yaml_data['cover']).exists():
    #                 poco(yaml_data['layout']).offspring(yaml_data['host']).child(yaml_data['group']) \
    #                     .child(yaml_data['pager']).child(yaml_data['group']).offspring(yaml_data['view']) \
    #                     .child(yaml_data['group'])[i].child(yaml_data['cover']).click()
    #                 sleep(3)
    #                 poco(yaml_data['back']).click()
    #                 i += 1
    #                 if i == 4:
    #                     sleep(1)
    #                     log.debug('当前第%s次' % i)
    #                     swipe((561, 1600), (561, 260))
    #
    #             else:
    #                 log.debug('======春暖中国已下线=====')
    #
    #     poco(text='最新').click()
    #     for i in range(5):
    #         poco(yaml_data['layout']).offspring(yaml_data['host']).child(yaml_data['group']) \
    #             .child(yaml_data['pager']).child(yaml_data['group']).offspring(yaml_data['view']) \
    #             .child(yaml_data['group'])[i].child(yaml_data['cover']).click()
    #         sleep(3)
    #         poco(yaml_data['back']).click()
    #     sleep(1)
    #     get_snapshot('春暖中国')
    #     recorder().stop_recording(output='%s春暖中国.mp4' % RECORDER_PATH)

    def teardown(self) -> None:
        pass


