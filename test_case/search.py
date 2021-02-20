import pyttsx3
from base.tools import *
import unittest,string,random
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
auto_setup(__file__)


class TestSearch(unittest.TestCase):


    def setUp(self) -> None:
        pass


    def test_01_search(self):
        '''搜索条件:通过关键字查看搜索结果'''
        stars_app()
        poco('com.yixia.videoeditor:id/btn_search').click()
        poco('com.yixia.videoeditor:id/edit_input').set_text(get_searchdata(0))
        sleep(1)
        poco('com.yixia.videoeditor:id/tv_title')[0].click()
        sleep(1)
        get_snapshot('搜索条件:通过关键字查看搜索结果')


    def test_02_search(self):
        '''搜索条件:纯英文'''
        poco('com.yixia.videoeditor:id/btn_clean').click()
        poco('com.yixia.videoeditor:id/edit_input').click()
        text(get_searchdata(1))
        sleep(1)
        get_snapshot('搜索条件:纯英文')

    def test_03_search(self):
        '''搜索条件:纯中文'''
        poco('com.yixia.videoeditor:id/btn_clean').click()
        poco('com.yixia.videoeditor:id/edit_input').click()
        text(get_searchdata(2))
        sleep(1)
        get_snapshot('搜索条件:纯中文')

    def test_04_search(self):
        '''搜索条件:纯数字'''
        poco('com.yixia.videoeditor:id/btn_clean').click()
        poco('com.yixia.videoeditor:id/edit_input').click()
        text(get_searchdata(3))
        sleep(1)
        get_snapshot('搜索条件:纯数字')


    def test_05_search(self):
        '''搜索条件:数字字母下划线'''
        poco('com.yixia.videoeditor:id/btn_clean').click()
        poco('com.yixia.videoeditor:id/edit_input').click()
        text(get_searchdata(4))
        sleep(1)
        get_snapshot('搜索条件:数字字母下划线')

    def test_06_search(self):
        '''搜索条件:网址'''
        poco('com.yixia.videoeditor:id/btn_clean').click()
        poco('com.yixia.videoeditor:id/edit_input').click()
        text(get_searchdata(5))
        sleep(1)
        get_snapshot('搜索条件:网址')

    def test_07_search(self):
        '''搜索条件:表情'''
        #poco('com.yixia.videoeditor:id/btn_cancel').click()
        #poco('com.yixia.videoeditor:id/btn_search').click()
        poco('com.yixia.videoeditor:id/btn_clean').click()
        poco('com.yixia.videoeditor:id/edit_input').click()
        text(get_searchdata(6))
        sleep(1)
        get_snapshot('搜索条件:表情')

    def test_08_search(self):
        '''搜索条件:特殊字符'''
        poco('com.yixia.videoeditor:id/btn_clean').click()
        str = string.punctuation
        poco('com.yixia.videoeditor:id/edit_input').set_text(str)
        keyevent("ENTER")
        sleep(1)
        get_snapshot('搜索条件:特殊字符')

    def test_09_search(self):
        '''搜索条件:随机数字+字母组合'''
        poco('com.yixia.videoeditor:id/btn_clean').click()
        vaule = ''.join(random.sample(string.digits + string.ascii_letters, 20))
        poco('com.yixia.videoeditor:id/edit_input').set_text(vaule)
        keyevent("ENTER")
        sleep(1)
        get_snapshot('搜索条件:随机数字+字母组合')

    def test_10_search(self):
        '''删除搜索某条记录'''
        poco('com.yixia.videoeditor:id/btn_clean').click()
        vaule = ''.join(random.sample(string.digits + string.ascii_letters, 4))
        poco('com.yixia.videoeditor:id/edit_input').set_text(vaule)
        keyevent("ENTER")
        poco('com.yixia.videoeditor:id/btn_clean').click()
        poco('com.yixia.videoeditor:id/btn_delete').click()
        sleep(1)
        get_snapshot('删除搜索某条记录')

    def test_11_search(self):
        '''删除搜索全部记录'''
        poco('com.yixia.videoeditor:id/btn_clear').click()
        poco('com.yixia.videoeditor:id/btn_ok').click()
        sleep(1)
        get_snapshot('删除搜索全部记录')

    def test_12_search(self):
        '''查看搜索视频'''
        poco('com.yixia.videoeditor:id/edit_input').set_text(get_searchdata(8))
        keyevent("ENTER")
        sleep(1)
        poco('com.yixia.videoeditor:id/iv_cover')[1].click()
        sleep(1)
        get_snapshot('查看搜索视频')
        sleep(2)
        keyevent("KEYCODE_BACK")

    def test_13_search(self):
        '''搜索结果：点击查看更多'''
        poco(text='查看更多')[0].click()  #查看用户tab
        sleep(1)
        get_snapshot('查看用户tab')
        poco(text='综合').click()
        poco(text='查看更多')[1].click()   #查看视频tab
        sleep(1)
        get_snapshot('查看视频tab')
        swipe((561, 1686), (561, 245))
        poco('com.yixia.videoeditor:id/iv_cover').click()
        sleep(2)
        keyevent("KEYCODE_BACK")

    def test_14_search(self):
        '''搜索:取消按钮'''
        poco('com.yixia.videoeditor:id/btn_cancel').click()
        sleep(1)
        get_snapshot('取消搜索，回到精选页面')


    def tearDown(self) -> None:
        pass



if __name__ == '__main__':
    unittest.main(verbosity=2)