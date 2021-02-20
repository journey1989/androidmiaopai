from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
import os,time
from base.config import log
import pyttsx3
from base.tools import *
import unittest,string,random
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
auto_setup(__file__)


'''
登录模块
1、执行登录模块时，需要检查手机是否有sim卡
2、检查第三方账号是否登录

'''

class TestLogin(unittest.TestCase):

    def setUp(self) -> None:
        pass


    def test_01_login(self):
        '''一键登录'''
        stars_app()
        poco(text='我的').click()
        poco('com.yixia.videoeditor:id/iv_avatar').click()
        sleep(1)
        code_login()
        get_snapshot('一键登录')
        sleep(1)

    def test_02_login(self):
        '''验证码登录'''
        stars_app()
        poco(text='我的').click()
        poco('com.yixia.videoeditor:id/iv_avatar').click()
        sim_code_login()
        get_snapshot('验证码登录')
        sleep(1)

    def test_03_login(self):
        '''微信登录'''
        stars_app()
        poco(text='我的').click()
        poco('com.yixia.videoeditor:id/iv_avatar').click()
        wechat_login()
        get_snapshot('微信登录')
        sleep(1)
        value = poco('com.yixia.videoeditor:id/tv_name').attr('text')
        assert_equal(value, '秒拍微信登录',  msg='微信登录成功')
        sleep(1)

    def test_04_login(self):
        '''qq登录'''
        stars_app()
        poco(text='我的').click()
        poco('com.yixia.videoeditor:id/iv_avatar').click()
        qq_login()
        get_snapshot('qq登录')
        sleep(1)

    def test_05_login(self):
        '''微博登录'''
        stars_app()
        poco(text='我的').click()
        poco('com.yixia.videoeditor:id/iv_avatar').click()
        weibo_login()
        sleep(1)
        get_snapshot('微博登录')
        sleep(1)

    def test_06_login(self):
        '''关注tab:一键关注调登录'''
        stars_app()
        poco(text='关注').click()
        poco('com.yixia.videoeditor:id/btn_follow_all').click()
        sim_code_login()
        get_snapshot('关注tab:一键关注调登录')
        sleep(1)

    def test_07_login(self):
        '''关注tab:单个关注调登录'''
        stars_app()
        poco(text='关注').click()
        poco('com.yixia.videoeditor:id/btn_follow').click()
        sim_code_login()
        get_snapshot('关注tab:单个关注调登录')
        sleep(1)

    def test_08_login(self):
        '''搜索结果：关注调登录'''
        stars_app()
        poco('com.yixia.videoeditor:id/btn_search').click()
        poco('com.yixia.videoeditor:id/edit_input').set_text('电影')
        keyevent("KEYCODE_ENTER")
        poco('com.yixia.videoeditor:id/btn_follow').click()
        sim_code_login()
        sleep(1)

    def test_09_login(self):
        '''精选页面：关注调登录'''
        stars_app()
        poco('com.yixia.videoeditor:id/btn_follow').click()
        sleep(1)
        sim_code_login()
        poco('com.yixia.videoeditor:id/btn_follow').click()
        get_snapshot('精选页面：关注调登录')

    def test_10_login(self):
        '''精选页面：点赞调登录'''
        stars_app()
        poco('com.yixia.videoeditor:id/btn_praise').click()
        sim_code_login()
        poco('com.yixia.videoeditor:id/btn_praise').click()
        get_snapshot('精选页面：点赞调登录')

    def test_11_login(self):
        '''精选页面：分享面板收藏调登录'''
        stars_app()
        sleep(1)
        poco(text='分享').click()
        poco('com.yixia.videoeditor:id/btn_favorites').click()
        sim_code_login()
        poco('com.yixia.videoeditor:id/btn_favorites').click()
        get_snapshot('精选页面：分享面板收藏调登录')

    def test_12_login(self):
        '''全屏页面：关注调登录'''
        stars_app()
        poco('com.yixia.videoeditor:id/tv_des').click()
        sim_code_login()
        get_snapshot('全屏页面：关注调登录')

    def test_13_login(self):
        '''全屏页面：说点什么调登录'''
        stars_app()
        poco('com.yixia.videoeditor:id/tv_des').click()
        poco('com.yixia.videoeditor:id/tv_comment').click()
        sim_code_login()
        poco('com.yixia.videoeditor:id/btn_comment').click()
        value = ''.join(random.sample(string.digits + string.ascii_letters, 2))   #随机生成字母+数字，长度为2位字符
        sleep(1)
        get_snapshot('说点什么调登录，并评论')
        poco('com.yixia.videoeditor:id/et_contact').set_text(value)
        poco('com.yixia.videoeditor:id/btn_submit').click()
        poco('com.yixia.videoeditor:id/btn_back').click()

        sleep(1)

    def test_14_login(self):
        '''全屏页面：点赞调登录'''
        stars_app()
        poco('com.yixia.videoeditor:id/tv_des').click()
        sleep(1)
        poco('com.yixia.videoeditor:id/btn_like').click()
        sim_code_login()
        sleep(1)
        poco('com.yixia.videoeditor:id/btn_like').click()
        get_snapshot('全屏页面：点赞调登录')
        sleep(1)

    def test_15_login(self):
        '''全屏页面：收藏调登录'''
        stars_app()
        poco('com.yixia.videoeditor:id/tv_des').click()
        poco('com.yixia.videoeditor:id/btn_favorites').click()
        sim_code_login()
        poco('com.yixia.videoeditor:id/btn_favorites').click()
        get_snapshot('全屏页面：收藏调登录')
        sleep(1)

    def test_16_login(self):
        '''横屏页面：关注调登录'''
        stars_app()
        poco('com.yixia.videoeditor:id/tv_des').click()
        touch(get_screen_sizes())
        poco('com.yixia.videoeditor:id/btn_horizontal_screen').click()
        poco('com.yixia.videoeditor:id/btn_follow').click()
        sim_code_login()
        poco('com.yixia.videoeditor:id/btn_follow').click()
        get_snapshot('横屏页面：关注调登录')
        sleep(1)

    def test_17_login(self):
        '''横屏页面：点赞调登录'''
        stars_app()
        poco('com.yixia.videoeditor:id/tv_des').click()
        touch(get_screen_sizes())
        poco('com.yixia.videoeditor:id/btn_horizontal_screen').click()
        poco('com.yixia.videoeditor:id/btn_like').click()
        sim_code_login()
        poco('com.yixia.videoeditor:id/btn_like').click()
        get_snapshot('横屏页面：点赞调登录')
        sleep(1)

    def test_18_login(self):
        '''横屏页面：收藏调登录'''
        stars_app()
        poco('com.yixia.videoeditor:id/tv_des').click()
        touch(get_screen_sizes())
        poco('com.yixia.videoeditor:id/btn_horizontal_screen').click()
        poco('com.yixia.videoeditor:id/btn_favorites').click()
        sim_code_login()
        poco('com.yixia.videoeditor:id/btn_favorites').click()
        get_snapshot('横屏页面：收藏调登录')
        sleep(1)

    def test_19_login(self):
        '''精选页面：分享面板举报调登录'''
        stars_app()
        sleep(1)
        poco(text='分享').click()
        poco('com.yixia.videoeditor:id/btn_feedback').click()
        sim_code_login()
        poco('com.yixia.videoeditor:id/btn_feedback').click()
        poco(text='含有广告').click()
        poco("com.yixia.videoeditor:id/btn_ok").click()
        get_snapshot('精选页面：分享面板举报调登录')
        sleep(1)

    def test_20_login(self):
        '''全屏页面：分享面板举报调登录'''
        stars_app()
        poco('com.yixia.videoeditor:id/tv_des').click()
        sleep(1)
        poco('com.yixia.videoeditor:id/btn_share').click()
        poco('com.yixia.videoeditor:id/btn_feedback').click()
        sim_code_login()
        poco('com.yixia.videoeditor:id/btn_feedback').click()
        poco(text='含有广告').click()
        poco("com.yixia.videoeditor:id/btn_ok").click()
        get_snapshot('全屏页面：分享面板举报调登录')
        sleep(1)

    def test_21_login(self):
        '''横屏页面：更多面板举报调登录'''
        stars_app()
        poco('com.yixia.videoeditor:id/tv_des').click()
        touch(get_screen_sizes())
        poco('com.yixia.videoeditor:id/btn_horizontal_screen').click()
        poco('com.yixia.videoeditor:id/btn_more').click()
        poco('com.yixia.videoeditor:id/btn_feedback').click()
        sim_code_login()
        poco('com.yixia.videoeditor:id/btn_feedback').click()
        poco(text='含有广告').click()
        poco("com.yixia.videoeditor:id/btn_ok").click()
        get_snapshot('横屏页面：更多面板举报调登录')
        sleep(1)

    def test_22_login(self):
        '''拉黑调登录'''
        stars_app()
        poco('com.yixia.videoeditor:id/iv_avatar').click()
        poco('com.yixia.videoeditor:id/btn_share').click()
        poco('com.yixia.videoeditor:id/btn_black_author').click()
        sim_code_login()
        poco('com.yixia.videoeditor:id/btn_black_author').click()
        poco('com.yixia.videoeditor:id/btn_ok').click()
        get_snapshot('拉黑用户')
        sleep(1)
        poco('com.yixia.videoeditor:id/btn_black_author').click()
        poco('com.yixia.videoeditor:id/btn_ok').click()
        get_snapshot('取消拉黑用户')
        sleep(1)

    def test_23_login(self):
        '''消息调登录'''
        stars_app()
        poco(text='消息').click()
        poco(text='登录/注册').click()
        sim_code_login()
        sleep(1)
        get_snapshot('消息调登录')
        sleep(2)

    def test_24_login(self):
        '''发布调登录'''
        stars_app()
        poco(text='发布').click()
        sim_code_login()
        sleep(2)



    def test_25_login(self):
        '''用户主页调登录'''
        stars_app()
        poco('com.yixia.videoeditor:id/iv_avatar').click()
        poco('com.yixia.videoeditor:id/btn_action').click()
        sim_code_login()
        poco('com.yixia.videoeditor:id/btn_action').click()
        get_snapshot('用户主页调登录')



    def tearDown(self) -> None:
        pass



if __name__ == '__main__':

  unittest.main()
  #   suit = unittest.TestSuite()
  #   suit.addTest(TestLogin('test_16_login'))
  #   suit.addTest(TestLoin('test_17_login'))
  #   suit.addTest(TestLoin('test_19_login'))
  #   suit.addTest(TestLoin('test_25_login'))
  #   unittest.TextTestRunner.run(suit)