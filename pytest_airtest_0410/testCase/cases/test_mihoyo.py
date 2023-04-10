# _*_ coding: utf-8 _*_ #
# @Author   :85340

import os
import allure
import pytest
from libs.homePage import HomePage
from libs.keyeventLib import KeyeventLib
from libs.searchResult import SearchResult
from libs.start import Start
from utils.get_absolute_path import reports_path
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

@allure.epic('mihoyo')
@allure.feature('米游社app测试')
class Test_search_taobao(object):
    @allure.story('首页用例')
    @allure.title('测试通过')
    def test_search_taobao(self,back_to_home):
        with allure.step('1-打开米游社app'):
            start = Start()
            start.stop_mihoyo()
            start.base_sleep(2)
            start.start_mihoyo()
        with allure.step('2-首页用例'):
            homePage = HomePage()   # 点击搜索框
            homePage.changePage()
            homePage.checkIn()
            homePage.base_sleep(1)
            homePage.clickPlus()
            homePage.selectPicture()
            homePage.base_sleep(3)
            homePage.assertAndInputText()
            homePage.clickPublish()
        with allure.step('3-断言'):
            searchResult = SearchResult()
            searchResult.checkSearchResult()

if __name__ == '__main__':
    pytest.main(['-sv',__file__,'--alluredir', reports_path,'--clean-alluredir'])
    os.system(f'allure serve  {reports_path}')