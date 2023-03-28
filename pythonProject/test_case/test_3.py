# -*- encoding=utf8 -*-
__author__ = "85340"
import pytest
from airtest.core.api import *
import time
#@pytest.fixture(scope='function', params='android://127.0.0.1:5037/RFCM80422EP?cap_method=MINICAP&&ori_method=MINICAPORI&&touch_method=MAXTOUCH,')
@pytest.fixture()
def base_poco():
    '''
    构造新的poco，完成测试用例执行前、后的步骤
    @return: 返回新的poco对象
    '''
    from poco.drivers.android.uiautomation import AndroidUiautomationPoco
    connect_device("android://127.0.0.1:5037/RFCM80422EP?cap_method=MINICAP&&ori_method=MINICAPORI&&touch_method=MAXTOUCH")
    #connect_device(request.param)
    base_poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
    base_poco.device.wake()
    start_app("com.mihoyo.hyperion")
    sleep(2)
    yield base_poco
    sleep(2)
    stop_app("com.mihoyo.hyperion")
    sleep(2)

def test_start(base_poco):
    print("start...")
    base_poco(text="原神").click()
    sleep(1.0)
    # 签到
    base_poco("com.mihoyo.hyperion:id/mIvIcon").click()
    sleep(3.0)
    # 返回主界面
    base_poco("com.mihoyo.hyperion:id/closeImageButton").click()
    sleep(1.0)
    # 首页下拉
    #swipe(Template(r"tpl1679476578696.png", record_pos=(-0.319, -0.335), resolution=(1440, 3040)),vector=[-0.0088, 0.1122])
    base_poco("com.mihoyo.hyperion:id/mHomeOfficialTitleTv").swipe([0, 0.2])
    sleep(1.0)
    # 向上滑动屏幕直到游戏业务吸顶
    for _ in range(2):
        base_poco("com.mihoyo.hyperion:id/bottomWidget").swipe([0, -1])
    # （自兼容）原神发现tab页面上下翻页

    # 点击原神业务下面的硬核讨论区
    base_poco(text="硬核").click()
    # 点击版区介绍弹框里的我知道了
    #base_poco("com.mihoyo.hyperion:id/confirmTv").click()
    # 原神硬核讨论区上下翻页
    #keyevent("TAB")
    # airtest 获取当前屏幕分辨率
    #width = G.DEVICE.display_info['width']
    #height = G.DEVICE.display_info['height']
    # 向上向下翻页
    base_poco("com.mihoyo.hyperion:id/dividerView").swipe([0, -1])
    sleep(2.0)
    base_poco("com.mihoyo.hyperion:id/dividerView").swipe([0, 1])
    sleep(2.0)
    # 首页点击底部的动态
    base_poco("android.widget.FrameLayout").child("android.widget.LinearLayout").offspring(
        "com.mihoyo.hyperion:id/mHomePageRbDynamic").offspring("com.mihoyo.hyperion:id/mHomeTabRadioBtnIv").click()
    sleep(1.0)
    # 首页点击底部的消息
    base_poco("android.widget.FrameLayout").child("android.widget.LinearLayout").offspring(
        "com.mihoyo.hyperion:id/mHomePageRbMessage").offspring("com.mihoyo.hyperion:id/mHomeTabRadioBtnIv").click()
    sleep(1.0)
    # 首页点击底部的我的
    base_poco("android.widget.FrameLayout").child("android.widget.LinearLayout").offspring(
        "com.mihoyo.hyperion:id/mHomePageRbMessage").offspring("com.mihoyo.hyperion:id/mHomeTabRadioBtnIv").click()
    sleep(1.0)
    # 首页点击底部的首页
    base_poco("android.widget.FrameLayout").child("android.widget.LinearLayout").offspring(
        "com.mihoyo.hyperion:id/mHomePageRbHome").offspring("com.mihoyo.hyperion:id/mHomeTabRadioBtnIv").click()
    time.sleep(1)
    result_1 = base_poco(text="发现").exists()
    assert result_1 == True
    print("end...")

#if __name__ == '__main__':
   # pytest.main()