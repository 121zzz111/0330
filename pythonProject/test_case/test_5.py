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
    # 首页点击底部的+号，选择图片创作
    base_poco("com.mihoyo.hyperion:id/mHomePageIvPost").click()
    sleep(1.0)
    base_poco("com.mihoyo.hyperion:id/addImagePostTv").click()
    # poco("com.android.permissioncontroller:id/permission_allow_button").click()
    # sleep(1.0)
    # 选择步骤四保存的动图,点击下一步
    base_poco("android.widget.LinearLayout").offspring("android:id/content").offspring(
        "com.mihoyo.hyperion:id/picture_recycler").child("android.widget.RelativeLayout")[1].offspring(
        "com.mihoyo.hyperion:id/check").click()
    base_poco("com.mihoyo.hyperion:id/picture_tv_ok").click()
    sleep(5.0)
    # 输入标题:兼容图片帖；输入内容:兼容图片帖
    base_poco("com.mihoyo.hyperion:id/post_edit_et").click()
    text("兼容图片贴")
    #base_poco("com.mihoyo.hyperion:id/post_edit_et").click()
    #text("兼容图片贴")
    sleep(1.0)
    base_poco("com.mihoyo.hyperion:id/postImageContentEt").click()
    text("兼容图片贴")
    sleep(1.0)
    # 点击@搜索心外无物后选择
    text("@")
    base_poco("com.mihoyo.hyperion:id/searchEt").click()
    text("心外无物")
    sleep(1.0)
    base_poco("android.widget.LinearLayout").offspring("com.mihoyo.hyperion:id/rootLayout").offspring(
        "com.mihoyo.hyperion:id/atUserRv").child("android.view.ViewGroup")[1].click()
    sleep(3.0)
    # 添加抽奖,参与方式\关注条件默认,开奖时间默认选择当前时间一小时后,奖品名称:wetest抽奖,中奖人数:10,奖品发放选择需要邮寄,勾选抽奖协议后点击完成

    # 点击发布按钮
    base_poco("com.mihoyo.hyperion:id/action_bar_menu_tv").click()
    sleep(1.0)
    # 选择大别野下的同人,点击确认
    base_poco("android.widget.FrameLayout").child("android.widget.LinearLayout").offspring("android:id/content").offspring(
        "com.mihoyo.hyperion:id/mPostSelectForumRv").child("android.widget.LinearLayout")[1].child(
        "com.mihoyo.hyperion:id/mPostSelectForumBlockRv").child("android.widget.LinearLayout")[0].child(
        "com.mihoyo.hyperion:id/mPostSelectForumIvIcon").click()
    base_poco("com.mihoyo.hyperion:id/confirmTv").click()
    sleep(1.0)
    # 点击发布
    base_poco("com.mihoyo.hyperion:id/action_bar_menu_tv").click()
    time.sleep(1)
    result_1 = base_poco("com.mihoyo.hyperion:id/mCommentHeaderAllCommentTv").exists()
    assert result_1 == True
    print("end...")

#if __name__ == '__main__':
   # pytest.main()