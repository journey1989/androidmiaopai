from base.tools import *
import unittest,string,random,yaml
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
auto_setup(__file__)

'''
我的
'''
with open('%s/resourceid.yaml') as f:
    yaml_data = yaml.load(f)

class TestMy(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def test_01_my(self):
        '''我的：编辑资料'''
        stars_app()
        poco(text='我的').click()
        poco('com.yixia.videoeditor:id/iv_avatar').click()
        sim_code_login()
        poco('com.yixia.videoeditor:id/btn_action').click()
        poco('com.yixia.videoeditor:id/image_user_edit_profile_photo').click()
        if poco('com.android.permissioncontroller:id/permission_allow_button'):
            poco('com.android.permissioncontroller:id/permission_allow_button').click()
            poco('com.yixia.videoeditor:id/image_user_edit_profile_photo').click()
            value = random.randint(0, 4)
            poco('com.yixia.videoeditor:id/media_thumbnail')[value].click()
            poco('com.yixia.videoeditor:id/menu_crop').click()
        else:
            poco('com.yixia.videoeditor:id/image_user_edit_profile_photo').click()
            value = random.randint(0,4)
            poco('com.yixia.videoeditor:id/media_thumbnail')[value].click()
            poco('com.yixia.videoeditor:id/menu_crop').click()
        name = ''.join(random.sample(string.ascii_letters + string.digits, 10))
        poco('com.yixia.videoeditor:id/edit_name').set_text(name)

        ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))
        poco('com.yixia.videoeditor:id/edit_open_id').set_text(ran_str)

        poco('com.yixia.videoeditor:id/btn_gender').click()
        list = ['男', '女', '保密']
        sex = random.choice(list)
        poco(text=sex).click()
        poco('com.yixia.videoeditor:id/btn_change_birthday').click()

        poco('com.yixia.videoeditor:id/wv_year').click()
        swipe((222,1737),(222,2191))
        poco('com.yixia.videoeditor:id/wv_month').click()
        swipe((533,1737),(533,2191))
        poco('com.yixia.videoeditor:id/wv_day').click()
        swipe((829,1737),(829,2191))
        poco('com.yixia.videoeditor:id/btn_ok').click()
        message = ''.join(random.sample(string.ascii_letters + string.digits, 10))
        poco('com.yixia.videoeditor:id/edit_sign').set_text(message)
        sleep(1)
        get_snapshot('完成编辑个人资料页面')
        poco('com.yixia.videoeditor:id/btn_save').click()
        sleep(1)

    def test_02_my(self):
        '''个人粉丝'''
        poco('com.yixia.videoeditor:id/btn_followers').click()
        sleep(2)
        get_snapshot('个人粉丝页面')
        keyevent("KEYCODE_BACK")


    def test_03_my(self):
        '''个人关注页面'''
        poco('com.yixia.videoeditor:id/btn_following').click()
        if poco('com.yixia.videoeditor:id/btn_follow').exists():
            poco('com.yixia.videoeditor:id/btn_follow').click()
            sleep(1)
            get_snapshot('取消关注')
            keyevent("KEYCODE_BACK")
        else:
            keyevent("KEYCODE_BACK")


    def test_04_my(self):
        '''个人作品'''
        if poco('com.yixia.videoeditor:id/iv_cover').exists():
            poco('com.yixia.videoeditor:id/iv_cover').click()
            sleep(2)
            keyevent("KEYCODE_BACK")
        else:
            log.debug('======暂无作品')



    def test_05_my(self):
        '''个人收藏'''
        swipe((940, 1500),(120, 1500))
        get_snapshot('个人收藏')
        if poco('com.yixia.videoeditor:id/iv_cover').exists():
            poco('com.yixia.videoeditor:id/iv_cover').click()
            sleep(2)
            keyevent("KEYCODE_BACK")
        else:
            log.debug('======空空如也======')


    def test_06_my(self):
        '''个人赞过'''
        swipe((940, 1500),(120, 1500))
        get_snapshot('个人赞过')
        if poco('com.yixia.videoeditor:id/iv_cover').exists():
            poco('com.yixia.videoeditor:id/iv_cover').click()
            sleep(2)
            keyevent("KEYCODE_BACK")
        else:
            log.debug('======空空如也======')


    def test_07_my(self):
        '''用户：粉丝列表'''
        poco(text='首页').click()
        poco('com.yixia.videoeditor:id/iv_avatar').click()
        poco('com.yixia.videoeditor:id/btn_followers').click()
        if poco('com.yixia.videoeditor:id/btn_follow').exists():
            poco('com.yixia.videoeditor:id/btn_follow').click()
            sleep(1)
            get_snapshot('关注用户的粉丝')
            keyevent("KEYCODE_BACK")
        else:
            keyevent("KEYCODE_BACK")

    def test_08_my(self):
        '''用户：关注列表'''
        poco('com.yixia.videoeditor:id/btn_following').click()
        if poco('com.yixia.videoeditor:id/btn_follow').exists():
            poco('com.yixia.videoeditor:id/btn_follow').click()
            sleep(1)
            get_snapshot('关注用户的关注用户')
            keyevent("KEYCODE_BACK")
        else:
            keyevent("KEYCODE_BACK")
            log.debug('=====空空如也=====')


    def test_09_my(self):
        '''用户作品'''
        if poco('com.yixia.videoeditor:id/iv_cover').exists():
            poco('com.yixia.videoeditor:id/iv_cover').click()
            sleep(2)
            get_snapshot('用户作品')
            keyevent("KEYCODE_BACK")
        else:
            log.debug('======空空如也====')

    def test_10_my(self):
        '''用户收藏'''
        swipe((940, 1500), (120, 1500))
        get_snapshot('用户收藏')
        if poco('com.yixia.videoeditor:id/iv_cover').exists():
            poco('com.yixia.videoeditor:id/iv_cover').click()
            sleep(2)
            keyevent("KEYCODE_BACK")
        else:
            log.debug('======空空如也======')

    def test_11_my(self):
        '''用户赞过'''
        swipe((940, 1500),(120, 1500))
        get_snapshot('用户赞过')
        if poco('com.yixia.videoeditor:id/iv_cover').exists():
            poco('com.yixia.videoeditor:id/iv_cover').click()
            sleep(2)
            keyevent("KEYCODE_BACK")
        else:
            log.debug('======空空如也======')




    def tearDown(self) -> None:
        pass