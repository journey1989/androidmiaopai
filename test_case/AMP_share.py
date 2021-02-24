from base.tools import *
import unittest,yaml
from base.config import RECORDER_PATH


poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
auto_setup(__file__)





with open('%s/resourceid.yaml'%DATA_PATH) as f:
    yaml_data = yaml.load(f)
'''
分享模块

'''

class TestShare(unittest.TestCase):

      def setUp(self) -> None:
          pass

      def test_01_share(self):
          '''列表分享：微信、qq、微博、复制链接、系统分享'''
          stars_app()
          recorder().start_recording(max_time=1800)
          poco(text='分享').click()
          share()
          recorder().stop_recording(output='%s列表分享.mp4' % RECORDER_PATH)

      def test_02_share(self):
          '''全屏分享：微信、qq、微博、复制链接、系统分享'''
          recorder().start_recording(max_time=1800)
          poco(yaml_data['des']).click()
          poco(yaml_data['share']).click()
          share1()
          recorder().stop_recording(output='%s全屏分享.mp4' % RECORDER_PATH)

      def test_03_share(self):
          '''横屏分享：微信、qq、微博、复制链接、系统分享'''
          stars_app()
          poco(yaml_data['des']).click()
          if poco(yaml_data['horizontal_screen']).exists():
              poco(yaml_data['horizontal_screen']).click()
              touch(get_screen_sizes())
              poco(yaml_data['play']).click()
          else:
              swipe((561, 1686), (561, 245))
              if poco(yaml_data['horizontal_screen']).exists():
                  poco(yaml_data['horizontal_screen']).click()
                  touch(get_screen_sizes())
                  poco(yaml_data['play']).click()
              else:
                  log.debug('========跳过此步骤=======')



      def test_04_share(self):
          '''横屏分享：微信、qq、微博、复制链接、系统分享'''
          recorder().start_recording(max_time=1800)
          share2()
          recorder().stop_recording(output='%s横屏分享.mp4' % RECORDER_PATH)

      def test_05_share(self):
          '''沉浸式分享：微信、qq、微博、复制链接、系统分享'''
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


      def test_06_share(self):
          '''用户主页分享：微信、qq、微博、复制链接'''
          recorder().start_recording(max_time=1800)
          stars_app()
          poco(text='精选').click()
          poco(yaml_data['avatar']).click()
          poco(yaml_data['share']).click()
          share2()
          sleep(1)
          get_snapshot('用户主页分享')
          recorder().stop_recording(output='%s用户主页分享.mp4' % RECORDER_PATH)

      def test_07_share(self):
          '''发现：活动分享'''
          recorder().start_recording(max_time=1800)
          stars_app()
          poco(text='发现').click()
          sleep(0.5)
          if poco(text='春暖中国').exists():
              poco(yaml_data['topic_share']).click()
              share3()
          else:
              log.debug('======春暖中国活动已下线======')
          recorder().stop_recording(output='%s发现活动分享.mp4' % RECORDER_PATH)











      def tearDown(self) -> None:
          pass


if __name__ == '__main__':
    t = TestShare()
