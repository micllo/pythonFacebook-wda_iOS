import time
from Common.com_func import log
from Project.pro_demo_1.page_object.heart_page import AddPage
from TestBase.test_case_unit import ParaCase
from TestBase.app_action import Base


class HealthTest(ParaCase):

    """ Health 用 例 集"""

    def test_add_heart_rate(self):
        """ 测试搜索'添加心率'(通过)  """
        log.info("user(test_add_heart_rate): " + self.user)
        log.info("passwd(test_add_heart_rate): " + self.passwd)

        # 根据不同用例特定自定义设置（也可以不设置）
        self.client.implicitly_wait(5)

        # 通过Base类调用实例方法 ：self（测试用例实例对象）
        Base.screenshot(self, "home.png")

        add_page = AddPage(self)
        add_page.add_heart_rate("66")
        # self.assertIn('test_search', "test_search", "test_search用例测试失败")

    # def test_search_wx(self):
    #     """ 测试搜索'微信'(失败)  """
    #     log.info("user(test_search_wx): " + self.user)
    #     log.info("passwd(test_search_wx): " + self.passwd)
    #
    #     search_page = SearchPage(self)
    #     search_page.search_wx("微信")
    #
    # def test_search_bd(self):
    #     """ 测试搜索'百度'(错误)  """
    #     log.info("user(test_search_bd): " + self.user)
    #     log.info("passwd(test_search_bd): " + self.passwd)
    #
    #     search_page = SearchPage(self)
    #     search_page.search_bd("百度")

