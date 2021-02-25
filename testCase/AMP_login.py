from base.config import RECORDER_PATH
from common.tools import *
import unittest,string,random,yaml

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
auto_setup(__file__)




'''
登录模块
1、执行登录模块时，需要检查手机是否有sim卡
2、检查第三方账号是否是登录的状态
command+option+L 格式化代码

'''

with open('%s/resourceid.yaml'%DATA_PATH) as f:
    yaml_data = yaml.load(f)



class TestLogin(unittest.TestCase):

    def setUp(self) -> None:
        pass



    def test_01_login(self):
        '''一键登录'''
        log.info('=======登录==========')
        stars_app()
        recorder().start_recording(max_time=1800)
        poco(text='我的').click()
        poco(yaml_data['avatar']).click()
        sleep(1)
        one_click_login()
        sleep(1)
        get_snapshot('一键登录')
        recorder().stop_recording(output='%s一键登录1.mp4' % RECORDER_PATH)

    def test_02_login(self):
        '''验证码登录'''
        recorder().start_recording(max_time=1800)
        stars_app()
        poco(text='我的').click()
        poco(yaml_data['avatar']).click()
        sim_code_login()
        get_snapshot('验证码登录')
        sleep(1)
        recorder().stop_recording(output='%s验证码登录2.mp4' % RECORDER_PATH)

    def test_03_login(self):
        '''微信登录'''
        stars_app()
        recorder().start_recording(max_time=1800)
        poco(text='我的').click()
        poco(yaml_data['avatar']).click()
        wechat_login()
        get_snapshot('微信登录')
        value = poco(yaml_data['name']).attr('text')
        assert_equal(value, '秒拍微信登录',  msg='微信登录成功')
        sleep(1)
        recorder().stop_recording(output='%s微信登录3.mp4' % RECORDER_PATH)

    def test_04_login(self):
        '''qq登录'''
        stars_app()
        recorder().start_recording(max_time=1800)
        poco(text='我的').click()
        poco(yaml_data['avatar']).click()
        qq_login()
        get_snapshot('qq登录')
        sleep(1)
        recorder().stop_recording(output='%sqq登录4.mp4' % RECORDER_PATH)

    def test_05_login(self):
        '''微博登录'''
        stars_app()
        recorder().start_recording(max_time=1800)
        poco(text='我的').click()
        poco(yaml_data['avatar']).click()
        weibo_login()
        sleep(1)
        get_snapshot('微博登录')
        sleep(1)
        recorder().stop_recording(output='%s微博登录5.mp4' % RECORDER_PATH)

    def test_06_login(self):
        '''关注tab:一键关注调登录'''
        stars_app()
        recorder().start_recording(max_time=1800)
        poco(text='关注').click()
        poco(yaml_data['follow_all']).click()
        sim_code_login()
        get_snapshot('关注tab:一键关注调登录')
        sleep(1)
        recorder().stop_recording(output='%s一键关注调登录6.mp4' % RECORDER_PATH)

    def test_07_login(self):
        '''关注tab:单个关注调登录'''
        stars_app()
        recorder().start_recording(max_time=1800)
        poco(text='关注').click()
        poco(yaml_data['follow']).click()
        sim_code_login()
        get_snapshot('关注tab:单个关注调登录')
        sleep(1)
        recorder().stop_recording(output='%s单个用户关注登录7.mp4' % RECORDER_PATH)

    def test_08_login(self):
        '''搜索结果：关注调登录'''
        stars_app()
        recorder().start_recording(max_time=1800)
        poco(yaml_data['search']).click()
        poco(yaml_data['input']).set_text('电影')
        keyevent("KEYCODE_ENTER")
        poco(yaml_data['follow']).click()
        sim_code_login()
        sleep(1)
        recorder().stop_recording(output='%s搜索关注调登录8.mp4' % RECORDER_PATH)

    def test_09_login(self):
        '''精选页面：关注调登录'''
        stars_app()
        recorder().start_recording(max_time=1800)
        poco(yaml_data['follow']).click()
        sleep(1)
        sim_code_login()
        poco(yaml_data['follow']).click()
        get_snapshot('精选页面：关注调登录')
        recorder().stop_recording(output='%s精选关注调登录9.mp4' % RECORDER_PATH)

    def test_10_login(self):
        '''精选页面：点赞调登录'''
        stars_app()
        recorder().start_recording(max_time=1800)
        poco(yaml_data['praise']).click()
        sim_code_login()
        poco(yaml_data['praise']).click()
        get_snapshot('精选页面：点赞调登录')
        recorder().stop_recording(output='%s精选点赞调登录10.mp4' % RECORDER_PATH)

    def test_11_login(self):
        '''精选页面：分享面板收藏调登录'''
        stars_app()
        sleep(1)
        recorder().start_recording(max_time=1800)
        poco(text='分享').click()
        poco(yaml_data['favorites']).click()
        sim_code_login()
        poco(yaml_data['favorites']).click()
        get_snapshot('精选页面：分享面板收藏调登录')
        recorder().stop_recording(output='%s分享面板收藏调登录11.mp4' % RECORDER_PATH)

    def test_12_login(self):
        '''全屏页面：关注调登录'''
        stars_app()
        recorder().start_recording(max_time=1800)
        poco(yaml_data['des']).click()
        poco(yaml_data['follow']).click()
        sim_code_login()
        sleep(1)
        get_snapshot('全屏页面：关注调登录')
        recorder().stop_recording(output='%s全屏关注调登录12.mp4' % RECORDER_PATH)

    def test_13_login(self):
        '''全屏页面：说点什么调登录'''
        stars_app()
        recorder().start_recording(max_time=1800)
        sleep(0.5)
        poco(yaml_data['des']).click()
        poco(yaml_data['comment']).click()
        sim_code_login()
        poco(yaml_data['comments']).click()
        value = ''.join(random.sample(string.digits + string.ascii_letters, 2))   #随机生成字母+数字，长度为2位字符
        sleep(1)
        get_snapshot('说点什么调登录，并评论')
        poco(yaml_data['contact']).set_text(value)
        poco(yaml_data['submit']).click()
        poco(yaml_data['back']).click()
        sleep(1)
        recorder().stop_recording(output='%s全屏说点什么调登录13.mp4' % RECORDER_PATH)

    def test_14_login(self):
        '''全屏页面：点赞调登录'''
        stars_app()
        recorder().start_recording(max_time=1800)
        poco(yaml_data['des']).click()
        sleep(1)
        poco(yaml_data['like']).click()
        sim_code_login()
        sleep(1)
        poco(yaml_data['like']).click()
        get_snapshot('全屏页面：点赞调登录')
        sleep(1)
        recorder().stop_recording(output='%s全屏点赞调登录14.mp4' % RECORDER_PATH)

    def test_15_login(self):
        '''全屏页面：收藏调登录'''
        stars_app()
        recorder().start_recording(max_time=1800)
        poco(yaml_data['des']).click()
        poco(yaml_data['favorites']).click()
        sim_code_login()
        poco(yaml_data['favorites']).click()
        get_snapshot('全屏页面：收藏调登录')
        sleep(1)
        recorder().stop_recording(output='%s全屏页面收藏调登录15.mp4' % RECORDER_PATH)

    def test_16_login(self):
        '''test16-18是一条用例：全屏切横屏'''
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



    def test_17_login(self):
        '''test16-18是一条用例：横屏点击关注'''
        poco(yaml_data['follow']).click()


    def test_18_login(self):
        '''test16-18是一条用例：横屏页面关注调登录'''
        recorder().start_recording(max_time=1800)
        sim_code_login()
        poco(yaml_data['follow']).click()
        get_snapshot('横屏页面：关注调登录')
        sleep(1)
        recorder().stop_recording(output='%s横屏关注调登录18.mp4' % RECORDER_PATH)

#如果16-18写一个方法的话，横屏无法登录




    def test_19_login(self):
        '''精选页面：分享面板举报调登录'''
        stars_app()
        sleep(1)
        recorder().start_recording(max_time=1800)
        poco(text='分享').click()
        poco(yaml_data['feedback']).click()
        sim_code_login()
        poco(yaml_data['feedback']).click()
        t = ['含有广告', '反动', '色情低俗', '视频无法播放', '欺诈或恶意营销']
        poco(text=random.choice(t)).click()
        poco(yaml_data['ok']).click()
        get_snapshot('精选页面：分享面板举报调登录')
        sleep(1)
        recorder().stop_recording(output='%s精选分享举报调登录19.mp4' % RECORDER_PATH)

    def test_20_login(self):
        '''全屏页面：分享面板举报调登录'''
        stars_app()
        recorder().start_recording(max_time=1800)
        poco(yaml_data['des']).click()
        sleep(1)
        poco(yaml_data['share']).click()
        poco(yaml_data['feedback']).click()
        sim_code_login()
        poco(yaml_data['feedback']).click()
        t = ['含有广告', '反动', '色情低俗', '视频无法播放', '欺诈或恶意营销']
        poco(text=random.choice(t)).click()
        poco(yaml_data["ok"]).click()
        get_snapshot('全屏页面：分享面板举报调登录')
        sleep(1)
        recorder().stop_recording(output='%s全屏分享举报调登录20.mp4' % RECORDER_PATH)



    def test_21_login(self):
        '''拉黑调登录'''
        stars_app()
        recorder().start_recording(max_time=1800)
        poco(yaml_data['avatar']).click()
        poco(yaml_data['share']).click()
        poco(yaml_data['black_author']).click()
        sim_code_login()
        poco(yaml_data['black_author']).click()
        poco(yaml_data['ok']).click()
        get_snapshot('拉黑用户')
        sleep(1)
        poco(yaml_data['black_author']).click()
        poco(yaml_data['ok']).click()
        get_snapshot('取消拉黑用户')
        sleep(1)
        recorder().stop_recording(output='%s拉黑用户调登录21.mp4' % RECORDER_PATH)

    def test_22_login(self):
        '''消息调登录'''
        stars_app()
        recorder().start_recording(max_time=1800)
        poco(text='消息').click()
        poco(text='登录/注册').click()
        sim_code_login()
        sleep(1)
        get_snapshot('消息调登录')
        sleep(2)
        recorder().stop_recording(output='%s消息调登录22.mp4' % RECORDER_PATH)

    def test_23_login(self):
        '''发布调登录'''
        stars_app()
        recorder().start_recording(max_time=1800)
        poco(text='发布').click()
        sim_code_login()
        sleep(2)
        recorder().stop_recording(output='%s发布调登录23.mp4' % RECORDER_PATH)



    def test_24_login(self):
        '''用户主页调登录'''
        stars_app()
        recorder().start_recording(max_time=1800)
        poco(yaml_data['avatar']).click()
        poco(yaml_data['action']).click()
        sim_code_login()
        poco(yaml_data['action']).click()
        get_snapshot('用户主页调登录')
        recorder().stop_recording(output='%s用户主页调登录24.mp4' % RECORDER_PATH)




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