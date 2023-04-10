# _*_ coding: utf-8 _*_ #

from common.basePage import BasePage

class HomePage(BasePage):
    def changePage(self):
        # 切换至原神业务
        self.base_touch('原神', (-0.401, -0.914))


    def checkIn(self):
        # 点击右上角的签到按钮并返回
        self.base_touch('签到按钮', (0.386, -0.812))
        self.wait_and_touch('返回', (-0.444, -0.92))

    def clickPlus(self):
        # 点击底部的加号，选择图片创作
        self.base_touch('加号', (0.002, 0.989))
        self.wait_and_touch('图片创作', (-0.003, 0.55))

    def selectPicture(self):
        # 选择图片创作
        self.base_touch('选择圆圈', (-0.048, -0.805))
        self.base_touch('下一步', (0.368, 0.987))

    def assertAndInputText(self):
        # 断言是否存在标题框和文本框并输入文本内容
        self.base_assert_exists('标题框',(-0.344, -0.764),"断言是否存在标题框")
        self.base_text('兼容图片帖')
        self.base_assert_exists('文本框', (-0.326, -0.608), "断言是否存在文本框")
        self.base_text('兼容图片帖')

    def clickPublish(self):
        # 点击发布
        self.base_touch('发布', (0.393, -0.914))
        # 选择大别野下的同人, 点击确认
        self.wait_and_touch('同人', (-0.297, -0.398))
        self.wait_and_touch('确定', (0.425, -0.922))
        self.wait_and_touch('发布', (0.393, -0.914))
