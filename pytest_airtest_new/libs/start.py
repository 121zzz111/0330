# _*_ coding: utf-8 _*_ #

from common.basePage import BasePage

class Start(BasePage):
    def start_mihoyo(self):
        # 启动米游社app
        self.start("com.mihoyo.hyperion")

    def stop_mihoyo(self):
        # 关闭米游社app
        self.stop("com.mihoyo.hyperion")