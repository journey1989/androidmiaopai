# Androidmiaopai


执行自动化前提条件：

1、base-tools-recorder()  设备号进行修改

2、检查手机是否第三方软件是否是登录状态

3、检查自动化的apk包是否是最新包




#base

config:配置路径

tools：公共方法

#data

resourceid.yaml     所有resource的id，后期客户端resource修改了，可以在里面进行修改，不用修改测试用例的代码

searchdata.txt   存放搜索条件，后期可以补充


#log

log.txt   存储代码中的操作记录


#allure_report    存放生成的测试报告

#run    运行测试用例：使用pytest+allure 框架
if __name__ == '__main__':
    pytest.main(["-v", "-s", "%sAMP_my.py" % TEST_PATH, "--alluredir=%s" % REPORT_PATH])    运行指定测试集脚本
    pytest.main(["-v", "-s", "%sAMP_my.py::TestMy::test_01_my" % TEST_PATH, "--alluredir=%s" % REPORT_PATH])    运行指定测试脚本
    
    
    for i in os.listdir(TEST_PATH):
        if i.startswith('AMP') == True:
            pytest.main(["-v", "-s", f"%s{i}" % TEST_PATH, "--alluredir=%s" % REPORT_PATH])     执行所有运行    
    
#snaphot   存放操作过程的截图

#test_case  存放测试用例

#recorder  存放录屏
