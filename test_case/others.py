from base.tools import *
import unittest,string,random,yaml

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
          stars_app()
          if poco(yaml_data['loopviewpager']).exists():
              poco(yaml_data['loopviewpager']).click()
              for i in range(2):
                  swipe((561, 1686), (561, 245))
              poco(yaml_data['back']).click()
          else:
              log.debug('======顶部广告未配置=====')
          sleep(1)
          get_snapshot('顶部广告')

      def test_02_others(self):
          '''精选头条:3个元素点击操作'''
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

      def tearDown(self) -> None:
          pass



if __name__ == '__main__':
    t = TestOthers()