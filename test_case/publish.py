from base.tools import *
import unittest,string,random,yaml

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
auto_setup(__file__)

with open('%s/resourceid.yaml'%DATA_PATH) as f:
    yaml_data = yaml.load(f)
'''
发布模块
'''

class TestRelease(unittest.TestCase):

       def setUp(self) -> None:
           pass

       def test_01_release(self):
           '''发布:调登录'''
           stars_app()
           poco(text='发布').click()
           sim_code_login()

       def test_02_release(self):
           '''发布：拍摄视频'''
           poco(text='发布').click()
           poco(yaml_data['camera']).click()
           if poco(yaml_data['permission_allow_button']).exists():   #相机
               poco(yaml_data['permission_allow_button']).click()
               if poco(yaml_data['permission_allow_button1']).exists():   #麦克风
                   poco(yaml_data['permission_allow_button1']).click()
                   if poco(yaml_data['permission_allow_button2']).exists():  #存储权限
                       poco(yaml_data['permission_allow_button2']).click()
                       poco(yaml_data['start']).click()
                       sleep(4)
                   else:
                       log.debug('=====所有权限弹窗已允许=====')
                       poco(yaml_data['start']).click()
                       sleep(4)
               else:
                   log.debug('=====无麦克风权限弹窗=====')
                   poco(yaml_data['start']).click()
                   sleep(4)
           else:
               log.debug('=====无相机权限弹窗=====')
               poco(yaml_data['start']).click()
               sleep(4)
               if poco(yaml_data['permission_allow_button1']).exists():
                   poco(yaml_data['permission_allow_button1']).click()
                   poco(yaml_data['start']).click()
                   sleep(4)
               else:
                   log.debug('======无麦克风权限弹窗======')
                   poco(yaml_data['start']).click()
                   sleep(4)
       def test_03_release(self):
           '''发布：编辑视频封面+发布视频'''
           poco(yaml_data['cover']).click()
           if poco(yaml_data['media_thumbnail']).exists():
               poco(yaml_data['media_thumbnail'])[0].click()
               poco(yaml_data['menu_crop']).click()
           else:
               keyevent("KEYCODE_BACK")
           poco(yaml_data['edit_title']).set_text('airtest发布视频')
           poco(yaml_data['publish']).click()
           sleep(10)


       def test_04_release(self):
           '''发布：上传视频'''
           poco(text='发布').click()
           poco(yaml_data['album']).click()  #上传
           if poco(yaml_data['media_thumbnail']).exists():
               poco(yaml_data['media_thumbnail'])[1].click()   #vivo手机正常，oppo手机不支持
               poco(yaml_data['edit_title']).set_text('airtest发布视频')
               sleep(1)
               poco(yaml_data['publish']).click()
               sleep(10)
               if poco(yaml_data['publish']).exists():
                   poco(yaml_data['publish']).click()

           else:
               poco(yaml_data['image_cancel']).click()
               poco(yaml_data['cancel']).click()


       def test_05_release(self):
           '''发布：查看发布视频'''
           poco(text='我的').click()
           poco(yaml_data['cover'])[0].click()
           sleep(2)
           keyevent("KEYCODE_BACK")



       def test_06_release(self):
           '''发布：删除发布视频'''
           poco(yaml_data['cover'])[0].long_click()
           poco(text='删除').click()

       def tearDown(self) -> None:
           pass



if __name__ == '__main__':
    t = TestRelease()
    t.test_01_release()