from common.tools import *
import allure, yaml
from base.config import RECORDER_PATH

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
auto_setup(__file__)

with open('%s/resourceid.yaml' % DATA_PATH) as f:
    yaml_data = yaml.load(f)
'''
分享模块

'''


@allure.feature('遍历APP分享模块')
class TestShare:

    def setup(self) -> None:
        pass

    @allure.title('列表分享：微信、qq、微博、复制链接、系统分享')
    @allure.story('列表分享：微信、qq、微博、复制链接、系统分享')
    def test_01_share(self):

        sleep(10)
        log.info('=======分享==========')
        recorder().start_recording(max_time=1800)
        stars_app()
        poco(text='分享').click()
        share()
        recorder().stop_recording(output='%s列表分享.mp4' % RECORDER_PATH)

    @allure.title('全屏分享：微信、qq、微博、复制链接、系统分享')
    @allure.story('全屏分享：微信、qq、微博、复制链接、系统分享')
    def test_02_share(self):

        recorder().start_recording(max_time=1800)
        miaopaiinto()
        poco(yaml_data['des']).click()
        poco(yaml_data['share']).click()
        share1()
        recorder().stop_recording(output='%s全屏分享.mp4' % RECORDER_PATH)

    @allure.title('沉浸式分享：微信、qq、微博、复制链接、系统分享')
    @allure.story('沉浸式分享：微信、qq、微博、复制链接、系统分享')
    def test_03_share(self):

        stars_app()
        recorder().start_recording(max_time=1800)
        poco(yaml_data['follow']).click()
        sim_code_login()
        poco(text='关注').click()
        poco(yaml_data['avatar'])[0].click()
        poco(text='分享').click()
        share1()
        sleep(1)
        keyevent("KEYCODE_BACK")
        recorder().stop_recording(output='%s沉浸式分享.mp4' % RECORDER_PATH)

    @allure.title('发现：活动分享微信')
    @allure.story('发现：活动分享微信')
    def test_04_share(self):

        recorder().start_recording(max_time=1800)
        stars_app()
        poco(text='发现').click()
        sleep(0.5)
        if poco(text='燃情冬奥').exists():
            poco(yaml_data['topic_share']).click()
            if poco(text='微信').exists():
                poco('com.yixia.videoeditor:id/btn_wechat').click()
                sleep(2)
                poco("com.tencent.mm:id/d7d").click()  # 搜索栏
                sleep(0.5)
                poco("com.tencent.mm:id/bxz").click()  # 激活搜索栏
                sleep(0.5)
                text('文件传输助手')  # 输入搜索内容
                poco('com.tencent.mm:id/ir3').click()  # 点击搜索内容
                sleep(0.5)
                poco('com.tencent.mm:id/ffp').click()  # 点击分享
                poco(text='返回秒拍视频').click()  # 点击返回秒拍
                miaopaiinto()
                sleep(1)
                poco(text='发现').click()
                poco(yaml_data['topic_share']).click()
                poco('com.yixia.videoeditor:id/btn_group').click()
                keyevent("KEYCODE_BACK")
        else:
            log.debug('======燃情冬奥已下线======')
        recorder().stop_recording(output='%s发现活动分享.mp4' % RECORDER_PATH)

    @allure.title('发现：活动分享qq')
    @allure.story('发现：活动分享qq')
    def test_05_share(self):

        recorder().start_recording(max_time=1800)
        miaopaiinto()
        poco(text='发现').click()
        sleep(0.5)
        if poco(text='燃情冬奥').exists():
            poco(yaml_data['topic_share']).click()
            if poco('com.yixia.videoeditor:id/btn_qq').exists():
                poco('com.yixia.videoeditor:id/btn_qq').click()
                sleep(2)
                poco('com.tencent.mobileqq:id/text1').click()
                poco("com.tencent.mobileqq:id/dialogRightBtn").click()  # 发送消息
                poco('com.tencent.mobileqq:id/dialogLeftBtn').click()  # 返回秒拍
                miaopaiinto()
                sleep(1)
                poco(text='发现').click()
                poco(yaml_data['topic_share']).click()
                poco('com.yixia.videoeditor:id/btn_qz').click()
                sleep(1)
                poco('com.tencent.mobileqq:id/ivTitleBtnLeft').click()

            else:
                log.debug('手机未安装QQ，不分享QQ')
        else:
            log.debug('======燃情冬奥已下线======')
        recorder().stop_recording(output='%s发现活动分享.mp4' % RECORDER_PATH)

    @allure.title('发现：活动分享微博')
    @allure.story('发现：活动分享微博')
    def test_06_share(self):

        recorder().start_recording(max_time=1800)
        miaopaiinto()
        poco(text='发现').click()
        sleep(0.5)
        if poco(text='燃情冬奥').exists():
            poco(yaml_data['topic_share']).click()
            if poco(text='微博').exists():
                poco('com.yixia.videoeditor:id/btn_weibo').click()
                ele = poco('com.sina.weibo:id/titleBack')
                e = poco.wait_for_any([ele], timeout=1800)
                e.click()
                poco(text='不保存').click()
            else:
                log.debug('手机未安装微博，不分享微博')
        else:
            log.debug('======燃情冬奥已下线======')
        recorder().stop_recording(output='%s发现活动分享.mp4' % RECORDER_PATH)

    @allure.title('发现：活动分享链接')
    @allure.story('发现：活动分享链接')
    def test_07_share(self):

        recorder().start_recording(max_time=1800)
        miaopaiinto()
        poco(text='发现').click()
        sleep(0.5)
        if poco(text='燃情冬奥').exists():
            poco(yaml_data['topic_share']).click()
            poco('com.yixia.videoeditor:id/btn_link').click()
        else:
            log.debug('======燃情冬奥已下线======')
        recorder().stop_recording(output='%s发现活动分享.mp4' % RECORDER_PATH)

    @allure.title('用户主页分享：微信')
    @allure.story('用户主页分享：微信')
    def test_08_share(self):

        recorder().start_recording(max_time=1800)
        miaopaiinto()
        poco(yaml_data['avatar']).click()
        poco(yaml_data['share']).click()
        if poco(text='微信').exists():
            poco('com.yixia.videoeditor:id/btn_wechat').click()
            sleep(2)
            poco("com.tencent.mm:id/d7d").click()  # 搜索栏
            sleep(0.5)
            poco("com.tencent.mm:id/bxz").click()  # 激活搜索栏
            sleep(0.5)
            text('文件传输助手')  # 输入搜索内容
            poco('com.tencent.mm:id/ir3').click()  # 点击搜索内容
            sleep(0.5)
            poco('com.tencent.mm:id/ffp').click()  # 点击分享
            poco(text='返回秒拍视频').click()  # 点击返回秒拍
            miaopaiinto()
            poco(yaml_data['avatar']).click()
            poco('com.yixia.videoeditor:id/btn_share').click()
            poco('com.yixia.videoeditor:id/btn_group').click()
            keyevent("KEYCODE_BACK")
        else:
            log.debug('手机未安装微信，不分享微信')
        sleep(1)
        get_snapshot('用户主页分享')
        recorder().stop_recording(output='%s用户主页微信分享.mp4' % RECORDER_PATH)

    @allure.title('用户主页分享：qq')
    @allure.story('用户主页分享：qq')
    def test_09_share(self):

        recorder().start_recording(max_time=1800)
        miaopaiinto()
        poco(yaml_data['avatar']).click()
        poco(yaml_data['share']).click()
        if poco('com.yixia.videoeditor:id/btn_qq').exists():
            poco('com.yixia.videoeditor:id/btn_qq').click()
            sleep(1)
            keyevent("KEYCODE_BACK")
            sleep(1)
            miaopaiinto()
            poco(yaml_data['avatar']).click()
            poco(yaml_data['share']).click()
            poco('com.yixia.videoeditor:id/btn_qz').click()
            sleep(1)
            poco('com.tencent.mobileqq:id/ivTitleBtnLeft').click()
            keyevent("KEYCODE_BACK")
        else:
            log.debug('手机未安装QQ，不分享QQ')
        sleep(1)
        get_snapshot('用户主页分享')
        recorder().stop_recording(output='%s用户主页qq分享.mp4' % RECORDER_PATH)

    @allure.title('用户主页分享：微博')
    @allure.story('用户主页分享：微博')
    def test_10_share(self):

        recorder().start_recording(max_time=1800)
        miaopaiinto()
        poco(yaml_data['avatar']).click()
        poco(yaml_data['share']).click()
        if poco('com.yixia.videoeditor:id/btn_weibo').exists():
            poco('com.yixia.videoeditor:id/btn_weibo').click()
            ele = poco('com.sina.weibo:id/titleBack')
            e = poco.wait_for_any([ele], timeout=1800)
            e.click()
            poco(text='不保存').click()
        else:
            log.debug('手机未安装微博')
        sleep(1)
        get_snapshot('用户主页分享')
        recorder().stop_recording(output='%s用户主页微博分享.mp4' % RECORDER_PATH)

    @allure.title('用户主页分享：拉黑')
    @allure.story('用户主页分享：拉黑')
    def test_11_share(self):

        recorder().start_recording(max_time=1800)
        miaopaiinto()
        poco(yaml_data['avatar']).click()
        poco(yaml_data['share']).click()
        if poco('com.yixia.videoeditor:id/btn_black_author').exists():
            poco('com.yixia.videoeditor:id/btn_black_author').click()
            sim_code_login()
            poco('com.yixia.videoeditor:id/btn_black_author').click()
            poco("com.yixia.videoeditor:id/btn_ok").click()
        else:
            log.debug('=======不显示拉黑入口===========')
        sleep(1)
        get_snapshot('用户主页分享')
        recorder().stop_recording(output='%s用户主页拉黑.mp4' % RECORDER_PATH)

    @allure.title('用户主页分享：复制链接')
    @allure.story('用户主页分享：复制链接')
    def test_12_share(self):

        recorder().start_recording(max_time=1800)
        miaopaiinto()
        poco(yaml_data['avatar']).click()
        poco(yaml_data['share']).click()
        poco('com.yixia.videoeditor:id/btn_link').click()
        sleep(1)
        get_snapshot('用户主页分享')
        recorder().stop_recording(output='%s用户主页拉黑.mp4' % RECORDER_PATH)

    def teardown(self) -> None:
        pass

    # def teardown_class(cls):
    #     pass
