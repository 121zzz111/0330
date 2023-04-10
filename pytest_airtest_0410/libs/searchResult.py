# _*_ coding: utf-8 _*_ #
# @Author   :85340

from common.basePage import BasePage

class SearchResult(BasePage):
    def checkSearchResult(self):
        # 断言查询结果
        self.base_assert_exists('头像',(-0.254, -0.914),"断言查询结果")