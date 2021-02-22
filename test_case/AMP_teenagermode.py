from base.tools import *
import unittest,string,random,yaml
from base.config import RECORDER_PATH



poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
auto_setup(__file__)




with open('%s/resourceid.yaml'%DATA_PATH) as f:
    yaml_data = yaml.load(f)



class TestTeenager(unittest.TestCase):
    def setUp(self) -> None:
        pass
        #os.system('adb devices')


    def test_01_teenager(self):
        '''青少年模式：首次启动进入青少年模式'''
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

    def test_02_teenager(self):
        '''青少年模式：滑动10条数据并播放视频'''
        recorder().start_recording(max_time=1800)
        if poco().exists():
            for i in range(1, 11):
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
    def test_03_teenager(self):
        '''青少年模式：列表页面元素点击'''
        recorder().start_recording(max_time=1800)
        poco(yaml_data['avatar']).click()  #头像
        poco(yaml_data['name']).click()  #名称
        poco(yaml_data['follow']).click() #关注
        poco(yaml_data['praise']).click()   #点赞
        poco(text='分享').click()
        recorder().stop_recording(output='%s列表元素点击.mp4' % RECORDER_PATH)

    def test_04_teenager(self):
        '''青少年模式：全屏播放元素点击'''
        recorder().start_recording(max_time=1800)
        poco(text='评论').click()
        poco(yaml_data['back']).click()
        sleep(1)
        poco(yaml_data['des']).click()#视频标题
        sleep(1)
        poco(yaml_data['share']).click()
        poco(yaml_data['follow']).click()
        poco(yaml_data['avatar']).click()
        poco(yaml_data['name']).click()
        poco(yaml_data['comment']).click()  #说点什么
        poco(yaml_data['favorites']).click() #收藏
        poco(yaml_data['like']).click()  #点赞
        recorder().stop_recording(output='%s全屏元素点击.mp4' % RECORDER_PATH)

    def test_05_teenager(self):
        '''青少年模式：全屏播放向下滑动10条进行播放'''
        recorder().start_recording(max_time=1800)
        for i in range(1, 11):
            sleep(5)
            swipe((561, 1686), (561, 245))
            log.debug('=====全屏播放已滑动%s次======' % i)
        recorder().stop_recording(output='%s全屏滑动.mp4' % RECORDER_PATH)



    def test_06_teenager(self):
        '''青少年模式：横屏播放向下滑动10条进行播放'''
        recorder().start_recording(max_time=1800)
        poco(yaml_data['horizontal_screen']).click()
        for i in range(1, 11):
            sleep(5)
            swipe((1120, 941), (1120, 165))
            log.debug('=====横屏播放已滑动%s次=====' % i)
        log.debug('=====滑动任务完成=====')
        recorder().stop_recording(output='%s横屏滑动.mp4' % RECORDER_PATH)


    def test_07_teenager(self):
        '''青少年模式：横屏播放元素点击'''
        recorder().start_recording(max_time=1800)
        touch(get_screen_sizes())
        poco(yaml_data['share']).click()
        touch(get_screen_sizes())
        poco(yaml_data['more']).click()  # 更多
        touch(get_screen_sizes())
        poco(yaml_data['follow']).click()
        touch(get_screen_sizes())
        sleep(1)
        poco(yaml_data['avatar']).click()
        touch(get_screen_sizes())
        poco(yaml_data['name']).click()
        touch(get_screen_sizes())
        poco(yaml_data['favorites']).click()  # 收藏
        touch(get_screen_sizes())
        poco(yaml_data['like']).click()  # 点赞
        recorder().stop_recording(output='%s横屏元素点击.mp4' % RECORDER_PATH)

    def test_08_teenager(self):
        '''青少年模式：横屏返回到全屏'''
        recorder().start_recording(max_time=1800)
        touch(get_screen_sizes())
        poco(yaml_data['back']).click()
        sleep(1)
        #横屏不能直接返回到全屏，再返回到列表，会引起无法退出青少年模式
        recorder().stop_recording(output='%s横屏返回全屏.mp4' % RECORDER_PATH)


    def test_09_teenager(self):
        '''退出青少年模式'''
        recorder().start_recording(max_time=1800)
        poco(yaml_data['back']).click()
        sleep(1)
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

       # os.system('adb reboot')





if __name__ == '__main__':
    t = TestTeenager()
    t.test_01_teenager()