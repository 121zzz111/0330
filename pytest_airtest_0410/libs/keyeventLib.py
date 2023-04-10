# _*_ coding: utf-8 _*_ #
# @Author   :85340

from common.basePage import BasePage

class KeyeventLib(BasePage):
    def keycode_home(self):
        # HOME键对应keyevent
        self.base_keyevent('3')

    def keycode_back(self):
        # 返回键对应keyevent
        self.base_keyevent('4')