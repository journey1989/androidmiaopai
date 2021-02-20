from base.tools import *
import unittest,string,random,yaml

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
          poco(text='分享').click()
          share()

      def test_02_share(self):
          '''全屏分享：微信、qq、微博、复制链接、系统分享'''
          poco(yaml_data['des']).click()
          poco(yaml_data['share']).click()
          share1()

      # def test_03_share(self):
      #     '''横屏分享：微信、qq、微博、复制链接、系统分享'''
      #     touch(get_screen_sizes())
      #     poco(yaml_data['horizontal_screen']).click()
      #     #touch(get_screen_sizes())
      #     poco(yaml_data['share']).click()
      #     share1()


      def test_04_share(self):
          '''浸浸式分享：微信、qq、微博、复制链接、系统分享'''
          stars_app()
          poco(yaml_data['follow']).click()
          sim_code_login()
          poco(text='关注').click()
          poco(yaml_data['avatar'])[0].click()
          poco(text='分享').click()
          share1()
          sleep(1)
          keyevent("KEYCODE_BACK")

      def test_05_share(self):
          '''用户主页分享：微信、qq、微博、复制链接'''
          poco(text='精选').click()
          poco(yaml_data['avatar']).click()
          poco(yaml_data['share']).click()
          share2()
          sleep(1)
          get_snapshot('用户主页分享')

      def test_06_share(self):
          '''发现：活动分享'''
          keyevent("KEYCODE_BACK")
          poco(text='发现').click()
          if poco(text='春暖中国').exists():
              poco(yaml_data['topic_share']).click()
              share2()











      def tearDown(self) -> None:
          pass


if __name__ == '__main__':
    t = TestShare()
