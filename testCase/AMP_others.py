from common.tools import *
import unittest, yaml

from base.config import RECORDER_PATH
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
auto_setup(__file__)






with open('%s/resourceid.yaml'%DATA_PATH) as f:
    yaml_data = yaml.load(f)
'''
其他
'''

class TestOthers(unittest.TestCase):

      def setUp(self) -> None:
          pass




      def test_01_others(self):
          '''精选顶部广告'''
          sleep(10)
          log.info('=======其他==========')
          stars_app()
          recorder().start_recording(max_time=1800)
          if poco(yaml_data['loopviewpager']).exists():
              poco(yaml_data['loopviewpager']).click()
              for i in range(2):
                  swipe((561, 1686), (561, 245))
              poco(yaml_data['back']).click()
          else:
              log.debug('======顶部广告未配置=====')
          sleep(1)
          get_snapshot('顶部广告')
          recorder().stop_recording(output='%s精选顶部广告.mp4' % RECORDER_PATH)

      def test_02_others(self):
          '''精选头条:3个元素点击操作'''
          recorder().start_recording(max_time=1800)
          if poco(yaml_data['icon']).exists():
              poco(yaml_data['icon']).click()
              sleep(3)
              poco(yaml_data['back']).click()
              poco(yaml_data['msg']).click()
              sleep(3)
              poco(yaml_data['back']).click()
              poco(yaml_data['icon_enter']).click()
              sleep(3)
              poco(yaml_data['back']).click()
          else:
              log.debug('=====头条广告未配置=====')
          recorder().stop_recording(output='%s头条广告.mp4' % RECORDER_PATH)

      def tearDown(self) -> None:
          pass



if __name__ == '__main__':
    t = TestOthers()