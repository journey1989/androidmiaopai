from base.config import RECORDER_PATH
from common.tools import *
import allure, string, random, yaml

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
auto_setup(__file__)

with open('%s/resourceid.yaml' % DATA_PATH) as f:
    yaml_data = yaml.load(f)


@allure.feature('遍历APP搜索模块')
class TestSearch:

    def setup(self) -> None:
        pass

    @allure.title('搜索条件:通过关键字查看搜索结')
    @allure.story('搜索条件:通过关键字查看搜索结')
    def test_01_search(self):
        sleep(10)
        log.info('=======搜索==========')
        miaopaiinto()
        recorder().start_recording(max_time=1800)
        poco(yaml_data['search']).click()
        poco(yaml_data['input']).set_text(get_searchdata(0))
        sleep(1)
        poco(yaml_data['title'])[0].click()
        sleep(1)
        get_snapshot('搜索条件:通过关键字查看搜索结果')
        recorder().stop_recording(output='%s搜索关键字.mp4' % RECORDER_PATH)

    @allure.title('搜索条件:纯英文')
    @allure.story('搜索条件:纯英文')
    def test_02_search(self):
        recorder().start_recording(max_time=1800)
        poco(yaml_data['clean']).click()
        poco(yaml_data['input']).click()
        text(get_searchdata(1))
        sleep(1)
        get_snapshot('搜索条件:纯英文')
        recorder().stop_recording(output='%s纯英文.mp4' % RECORDER_PATH)

    @allure.title('搜索条件:纯中文')
    @allure.story('搜索条件:纯中文')
    def test_03_search(self):
        recorder().start_recording(max_time=1800)
        poco(yaml_data['clean']).click()
        poco(yaml_data['input']).click()
        text(get_searchdata(2))
        sleep(1)
        get_snapshot('搜索条件:纯中文')
        recorder().stop_recording(output='%s纯中文.mp4' % RECORDER_PATH)

    @allure.title('搜索条件:纯数字')
    @allure.story('搜索条件:纯数字')
    def test_04_search(self):
        '''搜索条件:纯数字'''
        recorder().start_recording(max_time=1800)
        poco(yaml_data['clean']).click()
        poco(yaml_data['input']).click()
        text(get_searchdata(3))
        sleep(1)
        get_snapshot('搜索条件:纯数字')
        recorder().stop_recording(output='%s纯数字.mp4' % RECORDER_PATH)

    @allure.title('搜索条件:数字字母下划线')
    @allure.story('搜索条件:数字字母下划线')
    def test_05_search(self):
        recorder().start_recording(max_time=1800)
        poco(yaml_data['clean']).click()
        poco(yaml_data['input']).click()
        text(get_searchdata(4))
        sleep(1)
        get_snapshot('搜索条件:数字字母下划线')
        recorder().stop_recording(output='%s数字字母下划线.mp4' % RECORDER_PATH)

    @allure.title('搜索条件:网址')
    @allure.story('搜索条件:网址')
    def test_06_search(self):
        recorder().start_recording(max_time=1800)
        poco(yaml_data['clean']).click()
        poco(yaml_data['input']).click()
        text(get_searchdata(5))
        sleep(1)
        get_snapshot('搜索条件:网址')
        recorder().stop_recording(output='%s网址.mp4' % RECORDER_PATH)

    @allure.title('搜索条件:表情')
    @allure.story('搜索条件:表情')
    def test_07_search(self):
        recorder().start_recording(max_time=1800)
        poco(yaml_data['clean']).click()
        poco(yaml_data['input']).click()
        text(get_searchdata(6))
        sleep(1)
        get_snapshot('搜索条件:表情')
        recorder().stop_recording(output='%s表情.mp4' % RECORDER_PATH)

    @allure.title('搜索条件:特殊字符')
    @allure.story('搜索条件:特殊字符')
    def test_08_search(self):
        recorder().start_recording(max_time=1800)
        poco(yaml_data['clean']).click()
        str = string.punctuation
        poco(yaml_data['input']).set_text(str)
        keyevent("ENTER")
        sleep(1)
        get_snapshot('搜索条件:特殊字符')
        recorder().stop_recording(output='%s特殊字符.mp4' % RECORDER_PATH)

    @allure.title('搜索条件:随机数字+字母组合')
    @allure.story('搜索条件:随机数字+字母组合')
    def test_09_search(self):
        recorder().start_recording(max_time=1800)
        poco(yaml_data['clean']).click()
        vaule = ''.join(random.sample(string.digits + string.ascii_letters, 20))
        poco(yaml_data['input']).set_text(vaule)
        keyevent("ENTER")
        sleep(1)
        get_snapshot('搜索条件:随机数字+字母组合')
        recorder().stop_recording(output='%s数字字母.mp4' % RECORDER_PATH)

    @allure.title('删除搜索某条记录')
    @allure.story('删除搜索某条记录')
    def test_10_search(self):
        recorder().start_recording(max_time=1800)
        poco(yaml_data['clean']).click()
        vaule = ''.join(random.sample(string.digits + string.ascii_letters, 4))
        poco(yaml_data['input']).set_text(vaule)
        keyevent("ENTER")
        poco(yaml_data['clean']).click()
        poco(yaml_data['delete']).click()
        sleep(1)
        get_snapshot('删除搜索某条记录')
        recorder().stop_recording(output='%s删除某条搜索记录.mp4' % RECORDER_PATH)

    @allure.title('删除搜索全部记录')
    @allure.story('删除搜索全部记录')
    def test_11_search(self):
        recorder().start_recording(max_time=1800)
        poco(yaml_data['clear']).click()
        poco(yaml_data['ok']).click()
        sleep(1)
        get_snapshot('删除搜索全部记录')
        recorder().stop_recording(output='%s删除搜索全部记录.mp4' % RECORDER_PATH)

    @allure.title('查看搜索视频')
    @allure.story('查看搜索视频')
    def test_12_search(self):
        recorder().start_recording(max_time=1800)
        poco(yaml_data['input']).set_text(get_searchdata(8))
        keyevent("ENTER")
        sleep(1)
        poco(yaml_data['cover'])[1].click()
        sleep(1)
        get_snapshot('查看搜索视频')
        sleep(2)
        keyevent("KEYCODE_BACK")
        recorder().stop_recording(output='%s查看搜索视频.mp4' % RECORDER_PATH)

    @allure.title('搜索结果：点击查看更多')
    @allure.story('搜索结果：点击查看更多')
    def test_13_search(self):
        recorder().start_recording(max_time=1800)
        poco(text='查看更多')[0].click()  # 查看用户tab
        sleep(1)
        get_snapshot('查看用户tab')
        poco(text='综合').click()
        poco(text='查看更多')[1].click()  # 查看视频tab
        sleep(1)
        get_snapshot('查看视频tab')
        swipe((561, 1686), (561, 245))
        poco(yaml_data['cover']).click()
        sleep(2)
        keyevent("KEYCODE_BACK")
        recorder().stop_recording(output='%s查看更多按钮.mp4' % RECORDER_PATH)

    @allure.title('搜索:取消按钮')
    @allure.story('搜索:取消按钮')
    def test_14_search(self):
        recorder().start_recording(max_time=1800)
        poco(yaml_data['cancel']).click()
        sleep(1)
        get_snapshot('取消搜索，回到精选页面')
        recorder().stop_recording(output='%s退出搜索界面.mp4' % RECORDER_PATH)

    def teardown(self) -> None:
        pass
