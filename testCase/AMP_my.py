from common.tools import *
import allure, string, random, yaml

from base.config import RECORDER_PATH

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
auto_setup(__file__)

'''
我的
'''
with open('%s/resourceid.yaml' % DATA_PATH) as f:
    yaml_data = yaml.load(f)


@allure.feature('遍历APP我的')
class TestMy:

    def setUp(self) -> None:
        pass

    @allure.title('我的：编辑资料')
    @allure.story('我的：编辑资料')
    def test_01_my(self):

        sleep(10)
        log.info('=======我的==========')
        stars_app()
        recorder().start_recording(max_time=1800)
        poco(text='我的').click()
        poco(yaml_data['avatar']).click()
        sim_code_login()
        poco(yaml_data['action']).click()
        poco(text='点击更换头像').click()
        if poco(yaml_data['permission_allow_button']):
            poco(text='始终允许').click()
            poco(text='始终允许').click()

        else:
            log.info('没有出权限弹窗')
        value = random.randint(0, 4)
        poco(yaml_data['thumbnail'])[value].click()
        poco(yaml_data['menu_crop']).click()
        name = ''.join(random.sample(string.ascii_letters + string.digits, 10))
        poco(yaml_data['edit_name']).set_text(name)

        ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))
        poco(yaml_data['edit_open_id']).set_text(ran_str)

        poco(yaml_data['gender']).click()
        list = ['男', '女', '保密']
        sex = random.choice(list)
        poco(text=sex).click()
        poco(yaml_data['change_birthday']).click()

        poco(yaml_data['wv_year']).click()
        swipe((222, 1737), (222, 2191))
        poco(yaml_data['wv_month']).click()
        swipe((533, 1737), (533, 2191))
        poco(yaml_data['wv_day']).click()
        swipe((829, 1737), (829, 2191))
        poco(yaml_data['ok']).click()
        message = ''.join(random.sample(string.ascii_letters + string.digits, 10))
        poco(yaml_data['edit_sign']).set_text(message)
        sleep(1)
        get_snapshot('完成编辑个人资料页面')
        poco(yaml_data['save']).click()
        sleep(1)
        recorder().stop_recording(output='%s我的编辑资料.mp4' % RECORDER_PATH)

    @allure.title('我的：个人粉丝')
    @allure.story('我的：个人粉丝')
    def test_02_my(self):

        recorder().start_recording(max_time=1800)
        poco(yaml_data['follows']).click()
        sleep(2)
        get_snapshot('个人粉丝页面')
        keyevent("KEYCODE_BACK")
        recorder().stop_recording(output='%s个人粉丝页面.mp4' % RECORDER_PATH)

    @allure.title('我的：个人关注页面')
    @allure.story('我的：个人关注页面')
    def test_03_my(self):

        recorder().start_recording(max_time=1800)
        poco(yaml_data['following']).click()
        if poco(yaml_data['follow']).exists():
            poco(yaml_data['follow']).click()
            sleep(1)
            get_snapshot('取消关注')
            keyevent("KEYCODE_BACK")
        else:
            keyevent("KEYCODE_BACK")
        recorder().stop_recording(output='%s个人关注页面.mp4' % RECORDER_PATH)

    @allure.title('我的：个人作品')
    @allure.story('我的：个人作品')
    def test_04_my(self):

        recorder().start_recording(max_time=1800)
        if poco(yaml_data['cover']).exists():
            poco(yaml_data['cover']).click()
            sleep(2)
            keyevent("KEYCODE_BACK")
        else:
            log.debug('======暂无作品')
        poco(yaml_data['cover']).long_click()
        poco(text='删除').click()
        recorder().stop_recording(output='%s个人作品.mp4' % RECORDER_PATH)

    @allure.title('我的：个人收藏')
    @allure.story('我的：个人收藏')
    def test_05_my(self):

        recorder().start_recording(max_time=1800)
        swipe((940, 1500), (120, 1500))
        get_snapshot('个人收藏')
        if poco(yaml_data['cover']).exists():
            poco(yaml_data['cover']).click()
            sleep(2)
            keyevent("KEYCODE_BACK")
        else:
            log.debug('======空空如也======')
        recorder().stop_recording(output='%s个人收藏.mp4' % RECORDER_PATH)

    @allure.title('我的：个人赞过')
    @allure.story('我的：个人赞过')
    def test_06_my(self):

        recorder().start_recording(max_time=1800)
        swipe((940, 1500), (120, 1500))
        get_snapshot('个人赞过')
        if poco(yaml_data['cover']).exists():
            poco(yaml_data['cover']).click()
            sleep(2)
            keyevent("KEYCODE_BACK")
        else:
            log.debug('======空空如也======')
        recorder().stop_recording(output='%s个人赞过.mp4' % RECORDER_PATH)

    @allure.title('用户：粉丝列表')
    @allure.story('用户：粉丝列表')
    def test_07_my(self):

        recorder().start_recording(max_time=1800)
        poco(text='首页').click()
        poco(yaml_data['avatar']).click()
        poco(yaml_data['follows']).click()
        if poco(yaml_data['follow']).exists():
            poco(yaml_data['follow']).click()
            sleep(1)
            get_snapshot('关注用户的粉丝')
            keyevent("KEYCODE_BACK")
        else:
            keyevent("KEYCODE_BACK")
        recorder().stop_recording(output='%s用户粉丝列表.mp4' % RECORDER_PATH)

    @allure.title('用户：关注列表')
    @allure.story('用户：关注列表')
    def test_08_my(self):

        recorder().start_recording(max_time=1800)
        poco(yaml_data['following']).click()
        if poco(yaml_data['follow']).exists():
            poco(yaml_data['follow']).click()
            sleep(1)
            get_snapshot('关注用户的关注用户')
            keyevent("KEYCODE_BACK")
        else:
            keyevent("KEYCODE_BACK")
            log.debug('=====空空如也=====')
        recorder().stop_recording(output='%s用户关注列表.mp4' % RECORDER_PATH)

    @allure.title('用户：用户作品')
    @allure.story('用户：用户作品')
    def test_09_my(self):

        recorder().start_recording(max_time=1800)
        if poco(yaml_data['cover']).exists():
            poco(yaml_data['cover']).click()
            sleep(2)
            get_snapshot('用户作品')
            keyevent("KEYCODE_BACK")
        else:
            log.debug('======空空如也====')
        recorder().stop_recording(output='%s用户作品.mp4' % RECORDER_PATH)

    @allure.title('用户：用户收藏')
    @allure.story('用户：用户收藏')
    def test_10_my(self):

        recorder().start_recording(max_time=1800)
        swipe((940, 1500), (120, 1500))
        get_snapshot('用户收藏')
        if poco(yaml_data['cover']).exists():
            poco(yaml_data['cover']).click()
            sleep(2)
            keyevent("KEYCODE_BACK")
        else:
            log.debug('======空空如也======')
        recorder().stop_recording(output='%s用户收藏.mp4' % RECORDER_PATH)

    @allure.title('用户：用户赞过')
    @allure.story('用户：用户赞过')
    def test_11_my(self):

        recorder().start_recording(max_time=1800)
        swipe((940, 1500), (120, 1500))
        get_snapshot('用户赞过')
        if poco(yaml_data['cover']).exists():
            poco(yaml_data['cover']).click()
            sleep(2)
            keyevent("KEYCODE_BACK")
        else:
            log.debug('======空空如也======')
        recorder().stop_recording(output='%s用户赞过.mp4' % RECORDER_PATH)

    def tearDown(self) -> None:
        pass
