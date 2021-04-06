from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
import time,pyttsx3
from base.config import SNAPSHOT_PATH,log
from airtest.core.android.recorder import *
from airtest.core.android.adb import *


poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
auto_setup(__file__)

'''
共公方法
'''
def  stars_app():
    log.debug('=====执行清除数据，启动app=====')
    clear_app('com.yixia.videoeditor')
    start_app('com.yixia.videoeditor')
    if poco('com.yixia.videoeditor:id/btn_agree').exists():
        poco('com.yixia.videoeditor:id/btn_agree').click()
    elif poco(text='允许').exists():
        poco(text='允许').click()
    elif poco(text='始终允许').exists():
        poco(text='始终允许').click()
    elif poco('com.yixia.videoeditor:id/tv_quit_app').exists():
        poco('com.yixia.videoeditor:id/tv_quit_app').click()



'''
截图
'''
def get_snapshot(snapshotname):

    nowtime = time.strftime('%Y%m%d %H%M%S')

    return snapshot(filename=f'%s'%SNAPSHOT_PATH + nowtime + snapshotname + '.jpg', msg=snapshotname)


'''
有sim卡：验证码登录
'''
def sim_code_login():
    sleep(2)
    if poco('com.yixia.videoeditor:id/btn_switch').exists():
        poco('com.yixia.videoeditor:id/authsdk_checkbox_view').click()

        poco(text='本机号码一键登录').click()
    else:
        sleep(1)
        poco('com.yixia.videoeditor:id/edit_login_phone_number').set_text('12212345678')  # 输入手机号
        poco('com.yixia.videoeditor:id/edit_login_verify_code').set_text('123456')  # 输入验证码
        poco('com.yixia.videoeditor:id/tv_login_authentication_check').click()  # 同意用户协议
        poco('com.yixia.videoeditor:id/btn_login').click()  # 登录/注册
        log.debug('======当前设备没有sim卡，无法使用一键登录======')


'''
一键登录，如果没有sim卡，就使用兜底验证码登录
'''
def one_click_login():
    sleep(2)
    if poco('com.yixia.videoeditor:id/btn_switch').exists():
        poco('com.yixia.videoeditor:id/authsdk_checkbox_view').click()

        poco(text='本机号码一键登录').click()
    else:
        sleep(1)
        log.debug('======当前设备没有sim卡，无法使用一键登录======')



'''
我的-退出登录
'''
def my_loginout_app():
    poco(text='我的').click()
    poco('com.yixia.videoeditor:id/btn_back').click()
    poco('com.yixia.videoeditor:id/tv_setting_logout').click()
    poco('com.yixia.videoeditor:id/btn_ok').click()


'''
退出登录
'''
def loginout_app():

    poco('com.yixia.videoeditor:id/btn_back').click()
    poco('com.yixia.videoeditor:id/tv_setting_logout').click()
    poco('com.yixia.videoeditor:id/btn_ok').click()





'''
微信登录
'''
def wechat_login():
    sleep(3)
    if poco('com.yixia.videoeditor:id/btn_switch').exists():
       poco('com.yixia.videoeditor:id/btn_switch').click()   #切换其他登录方式
       if poco('com.yixia.videoeditor:id/btn_login_wx').exists():
           poco('com.yixia.videoeditor:id/btn_login_wx').click()
           poco('com.yixia.videoeditor:id/btn_protection_guideline_agree').click()
           sleep(3)
           if poco('com.yixia.videoeditor:id/btn_bind_phone_skip').exists():
               poco('com.yixia.videoeditor:id/btn_bind_phone_skip').click()
           else:
               log.debug('======当前账号已绑定手机号=======')

       else:
           log.debug('======当前设备未安装微信，无法使用微信登录======')
    else:
        if poco('com.yixia.videoeditor:id/btn_login_wx').exists():
            poco('com.yixia.videoeditor:id/btn_login_wx').click()
            poco('com.yixia.videoeditor:id/btn_protection_guideline_agree').click()
            sleep(3)
            if poco('com.yixia.videoeditor:id/btn_bind_phone_skip').exists():
                 poco('com.yixia.videoeditor:id/btn_bind_phone_skip').click()
            else:
                log.debug('======当前账号已绑定手机号=======')

        else:
            log.debug('======当前设备未安装微信，无法使用微信登录======')

'''
qq登录
'''
def qq_login():
    sleep(3)
    if poco('com.yixia.videoeditor:id/btn_switch').exists():
       poco('com.yixia.videoeditor:id/btn_switch').click()   #切换其他登录方式
       sleep(1)
       if poco('com.yixia.videoeditor:id/btn_login_qq').exists():
           poco('com.yixia.videoeditor:id/btn_login_qq').click()
           poco('com.yixia.videoeditor:id/btn_protection_guideline_agree').click()
           sleep(3)
           poco('com.tencent.mobileqq:id/fds').click()
           poco('com.tencent.mobileqq:id/b7p').click()
           sleep(3)
           if poco('com.yixia.videoeditor:id/btn_bind_phone_skip').exists():
               poco('com.yixia.videoeditor:id/btn_bind_phone_skip').click()
           else:

               log.debug('======当前账号已绑定手机号=======')

       else:

           log.debug('======当前设备未安装qq，无法使用qq登录======')
    else:
        sleep(1)
        if poco('com.yixia.videoeditor:id/btn_login_qq').exists():
            poco('com.yixia.videoeditor:id/btn_login_qq').click()
            poco('com.yixia.videoeditor:id/btn_protection_guideline_agree').click()
            sleep(3)
            poco('com.tencent.mobileqq:id/fds').click()
            poco('com.tencent.mobileqq:id/b7p').click()
            sleep(3)
            if poco('com.yixia.videoeditor:id/btn_bind_phone_skip').exists():
                poco('com.yixia.videoeditor:id/btn_bind_phone_skip').click()
            else:

                log.debug('======当前账号已绑定手机号=======')

        else:

            log.debug('======当前设备未安装qq，无法使用qq登录======')

'''
微博登录
'''
def weibo_login():
    sleep(3)
    if poco('com.yixia.videoeditor:id/btn_switch').exists():
        poco('com.yixia.videoeditor:id/btn_switch').click()   #切换其他登录方式
        sleep(1)
        if poco('com.yixia.videoeditor:id/btn_login_wb').exists():
            poco('com.yixia.videoeditor:id/btn_login_wb').click()
            poco('com.yixia.videoeditor:id/btn_protection_guideline_agree').click()
            sleep(3)
            # poco('com.sina.weibo:id/new_bnLogin').click()
            # sleep(3)
            if poco('com.yixia.videoeditor:id/btn_bind_phone_skip').exists():
                poco('com.yixia.videoeditor:id/btn_bind_phone_skip').click()
            else:
                log.debug('======当前账号已绑定手机号=======')
        else:
            log.debug('======当前设备未安装微博，无法使用微博登录======')
    else:
        sleep(1)
        if poco('com.yixia.videoeditor:id/btn_login_wb').exists():
            poco('com.yixia.videoeditor:id/btn_login_wb').click()
            poco('com.yixia.videoeditor:id/btn_protection_guideline_agree').click()
            sleep(3)
            # poco('com.sina.weibo:id/new_bnLogin').click()
            # sleep(3)
            if poco('com.yixia.videoeditor:id/btn_bind_phone_skip').exists():
                 poco('com.yixia.videoeditor:id/btn_bind_phone_skip').click()
            else:
                log.debug('======当前账号已绑定手机号=======')
        else:
            log.debug('======当前设备未安装微博，无法使用微博登录======')



'''
获取手机分辨率，并获取中心坐标，touch api需要用
'''
def get_screen_sizes():

    wh = poco.get_screen_size()
    w = wh[0]/2
    h = wh[1]/2
    return w, h



from base.config import DATA_PATH

'''
搜索条件用
'''
def get_searchdata(num):
    list_dir = f'%s/searchdata.txt' % DATA_PATH

    with open(list_dir, 'r') as f:
        l = f.readlines()

    return l[num]

'''
设置青少年模式
'''
def teenager_mode():
    clear_app('com.yixia.videoeditor')
    start_app('com.yixia.videoeditor')
    poco('com.yixia.videoeditor:id/btn_agree').click()
    if poco('com.android.permissioncontroller:id/permission_allow_button1').exists():
        poco('com.android.permissioncontroller:id/permission_allow_button1').click()
        sleep(1)
        poco('com.yixia.videoeditor:id/tv_set_teenager_mode').click()
    else:
        poco('com.yixia.videoeditor:id/tv_set_teenager_mode').click()

    poco('com.yixia.videoeditor:id/btn_kids_mode').click()



'''
#列表分享
'''
def share():
    if poco(text='微信').exists():
        poco('com.yixia.videoeditor:id/btn_wechat').click()
        sleep(2)
        poco('com.tencent.mm:id/c55').click()  # 搜索栏
        sleep(0.5)
        poco('com.tencent.mm:id/bhn').click()  # 激活搜索栏
        sleep(0.5)
        text('文件传输助手')  # 输入搜索内容
        poco('com.tencent.mm:id/gbv').click()  # 点击搜索内容
        sleep(0.5)
        poco('com.tencent.mm:id/doz').click()  # 点击分享
        poco('com.tencent.mm:id/dom').click()  # 点击返回秒拍
        poco(text='分享').click()
        poco('com.yixia.videoeditor:id/btn_group').click()
        keyevent("KEYCODE_BACK")

    else:
        log.debug('手机未安装微信，不分享微信')

    poco(text='分享').click()
    if poco(text='QQ').exists():
        poco('com.yixia.videoeditor:id/btn_qq').click()
        ele1 = poco('com.tencent.mobileqq:id/text1')
        e = poco.wait_for_any([ele1], timeout=1800)
        e.click()
        poco("com.tencent.mobileqq:id/dialogRightBtn").click()   #发送消息
        poco('com.tencent.mobileqq:id/dialogLeftBtn').click()  #返回秒拍

       # poco('com.tencent.mobileqq:id/ivTitleBtnLeftButton').click()
        sleep(1)
        poco(text='分享').click()
        poco('com.yixia.videoeditor:id/btn_qz').click()
        sleep(1)
        poco('com.tencent.mobileqq:id/ivTitleBtnLeft').click()

    else:
        log.debug('手机未安装QQ，不分享QQ')

    poco(text='分享').click()
    if poco(text='微博').exists():
        poco('com.yixia.videoeditor:id/btn_weibo').click()
        ele = poco(text='取消')
        e = poco.wait_for_any([ele],timeout=1800)
        e.click()
        poco(text='不保存').click()
    else:
        log.debug('手机未安装微博，不分享微博')

    poco(text='分享').click()
    swipe((879,1620),(356,1620))
    poco('com.yixia.videoeditor:id/btn_link').click()

    poco(text='分享').click()
    swipe((879, 1620), (356, 1620))
    if poco('com.yixia.videoeditor:id/btn_system').exists():
       poco('com.yixia.videoeditor:id/btn_system').click()
       keyevent("KEYCODE_BACK")
    else:
        log.debug('=====无系统分享=====')
        poco('com.yixia.videoeditor:id/btn_cancel').click()

'''
#全屏分享
'''
def share1():
    if poco(text='微信').exists():
        poco('com.yixia.videoeditor:id/btn_wechat').click()
        sleep(2)
        poco('com.tencent.mm:id/c55').click()  # 搜索栏
        sleep(0.5)
        poco('com.tencent.mm:id/bhn').click()  # 激活搜索栏
        sleep(0.5)
        text('文件传输助手')  # 输入搜索内容
        poco('com.tencent.mm:id/gbv').click()  # 点击搜索内容
        sleep(0.5)
        poco('com.tencent.mm:id/doz').click()  # 点击分享
        poco('com.tencent.mm:id/dom').click()  # 点击返回秒拍
        poco('com.yixia.videoeditor:id/btn_share').click()
        poco('com.yixia.videoeditor:id/btn_group').click()
        keyevent("KEYCODE_BACK")

    else:
        log.debug('手机未安装微信，不分享微信')
    sleep(1)
    poco('com.yixia.videoeditor:id/btn_share').click()
    if poco(text='QQ').exists():
        poco('com.yixia.videoeditor:id/btn_qq').click()
        sleep(2)
        poco('com.tencent.mobileqq:id/text1').click()
        poco("com.tencent.mobileqq:id/dialogRightBtn").click()   #发送消息
        poco('com.tencent.mobileqq:id/dialogLeftBtn').click()  #返回秒拍

       # poco('com.tencent.mobileqq:id/ivTitleBtnLeftButton').click()
        sleep(1)
        poco('com.yixia.videoeditor:id/btn_share').click()
        poco('com.yixia.videoeditor:id/btn_qz').click()
        sleep(1)
        poco('com.tencent.mobileqq:id/ivTitleBtnLeft').click()

    else:
        log.debug('手机未安装QQ，不分享QQ')

    poco('com.yixia.videoeditor:id/btn_share').click()
    if poco(text='微博').exists():
        poco('com.yixia.videoeditor:id/btn_weibo').click()
        ele = poco('com.sina.weibo:id/titleBack')
        e = poco.wait_for_any([ele], timeout=1800)
        e.click()
        poco(text='不保存').click()
    else:
        log.debug('手机未安装微博，不分享微博')

    poco('com.yixia.videoeditor:id/btn_share').click()
    swipe((889,1358),(129,1358))
    poco('com.yixia.videoeditor:id/btn_link').click()

    poco('com.yixia.videoeditor:id/btn_share').click()
    swipe((889,1358),(129,1358))
    poco('com.yixia.videoeditor:id/btn_system').click()
    keyevent("KEYCODE_BACK")

'''
 #横屏分享
 '''
def share2():
    poco('com.yixia.videoeditor:id/btn_link').click()
    if poco('com.yixia.videoeditor:id/btn_weibo').exists():
        poco('com.yixia.videoeditor:id/btn_weibo').click()
        ele = poco('com.sina.weibo:id/titleBack')
        e = poco.wait_for_any([ele], timeout=1800)
        e.click()
        poco(text='不保存').click()
    else:
        log.debug('手机未安装微博')
    if poco('com.yixia.videoeditor:id/btn_black_author').exists():
        poco('com.yixia.videoeditor:id/btn_black_author').click()
        sim_code_login()
        poco('com.yixia.videoeditor:id/btn_black_author').click()
        poco("com.yixia.videoeditor:id/btn_ok").click()
    else:
        log.debug('=======不显示拉黑入口===========')

    if poco(text='微信').exists():
        poco('com.yixia.videoeditor:id/btn_wechat').click()
        poco('com.tencent.mm:id/c55').click()  # 搜索栏
        sleep(0.5)
        poco('com.tencent.mm:id/bhn').click()  # 激活搜索栏
        sleep(0.5)
        text('文件传输助手')  # 输入搜索内容
        poco('com.tencent.mm:id/gbv').click()  # 点击搜索内容
        sleep(0.5)
        poco('com.tencent.mm:id/doz').click()  # 点击分享
        poco('com.tencent.mm:id/dom').click()  # 点击返回秒拍
        poco('com.yixia.videoeditor:id/btn_group').click()
        keyevent("KEYCODE_BACK")
    else:
        log.debug('手机未安装微信，不分享微信')
    if poco(text='QQ').exists():
        poco('com.yixia.videoeditor:id/btn_qq').click()
        sleep(1)
        keyevent("KEYCODE_BACK")
        sleep(1)
        poco('com.yixia.videoeditor:id/btn_qz').click()
        sleep(1)
        poco('com.tencent.mobileqq:id/ivTitleBtnLeft').click()
        keyevent("KEYCODE_BACK")
    else:
        log.debug('手机未安装QQ，不分享QQ')




def recorder():
    adb = ADB(serialno="SJE0217B18002911")
    recorder = Recorder(adb)  # 实例化
    return recorder





'''用例执行完成，进行语音通知'''
def test_finsih():
    engine = pyttsx3.init()
    engine.say('秒拍自动化测试任务执行完成，请查看测试结果')
    engine.runAndWait()


def share3():
    if poco('com.yixia.videoeditor:id/btn_black_author').exists():
        poco('com.yixia.videoeditor:id/btn_black_author').click()
        sim_code_login()
        poco('com.yixia.videoeditor:id/btn_black_author').click()
        poco("com.yixia.videoeditor:id/btn_ok").click()
    else:
        log.debug('=======不显示拉黑入口===========')
    if poco(text='微信').exists():
        poco('com.yixia.videoeditor:id/btn_wechat').click()
        sleep(2)
        poco('com.tencent.mm:id/c55').click()  # 搜索栏
        sleep(0.5)
        poco('com.tencent.mm:id/bhn').click()  # 激活搜索栏
        sleep(0.5)
        text('文件传输助手')  # 输入搜索内容
        poco('com.tencent.mm:id/gbv').click()  # 点击搜索内容
        sleep(0.5)
        poco('com.tencent.mm:id/doz').click()  # 点击分享
        poco('com.tencent.mm:id/dom').click()  # 点击返回秒拍
        sleep(2)
        poco('com.yixia.videoeditor:id/btn_group').click()
        keyevent("KEYCODE_BACK")
    else:
        log.debug('手机未安装微信，不分享微信')
    if poco(text='QQ').exists():
        poco('com.yixia.videoeditor:id/btn_qq').click()
        sleep(1)
        poco('com.tencent.mobileqq:id/text1').click()
        poco("com.tencent.mobileqq:id/dialogRightBtn").click()   #发送消息
        poco('com.tencent.mobileqq:id/dialogLeftBtn').click()  #返回秒拍
        sleep(1)
        poco('com.yixia.videoeditor:id/btn_qz').click()
        sleep(1)
        poco('com.tencent.mobileqq:id/ivTitleBtnLeft').click()
    else:
        log.debug('手机未安装QQ，不分享QQ')
    if poco(text='微博').exists():
        poco('com.yixia.videoeditor:id/btn_weibo').click()
        ele = poco('com.sina.weibo:id/titleBack')
        e = poco.wait_for_any([ele], timeout=1800)
        e.click()
        poco(text='不保存').click()
    else:
        log.debug('手机未安装微博，不分享微博')
    poco('com.yixia.videoeditor:id/btn_link').click()
    if poco('com.yixia.videoeditor:id/btn_system').exists():
       poco('com.yixia.videoeditor:id/btn_system').click()
       keyevent("KEYCODE_BACK")
    else:
        log.debug('=====无系统分享=====')
        poco('com.yixia.videoeditor:id/btn_cancel').click()


def miaopaiinto():
    stop_app('com.yixia.videoeditor')
    start_app('com.yixia.videoeditor')