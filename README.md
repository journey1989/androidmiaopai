# androidmiaopai
androidmiaopaiuiautomaitor

#base
bases；暂无使用
config:配置路径
tools：公共方法

#data
resourceid.yaml     所有resource的id，后期客户端resource修改了，可以在里面进行修改，不用修改测试用例的代码
searchdata.txt   存放搜索条件，后期可以补充


#log
log.txt   存储代码中的操作记录


#report    存放生成的测试报告

#run    运行测试用例
discover = unittest.defaultTestLoader.discover(TEST_PATH, 'player.py')    运行播放器模块的用例
discover = unittest.defaultTestLoader.discover(TEST_PATH, '*.py')    运行全部的用例

#snaphot   存放操作过程的截图

#test_case  存放测试用例

#recorder  增加录屏
