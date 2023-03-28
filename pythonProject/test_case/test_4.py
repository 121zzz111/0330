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
    # 进入我的页面点击个人主页
    base_poco("com.mihoyo.hyperion:id/mHomePageRbMe").click()
    sleep(1.0)
    base_poco("com.mihoyo.hyperion:id/homepageTv").click()
    result=base_poco("com.mihoyo.hyperion:id/mUserHomeUserInfoTvName").exists()
    assert result == True
    print("end...")