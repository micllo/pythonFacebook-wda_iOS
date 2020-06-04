# -*- coding:utf-8 -*-
from TestBase.app_action import Base
import time


class AddPage(Base):

    """
        【 元 素 定 位 】
    """

    # 触摸 Browse 图标
    def touch_browser_cron(self):
        self.touch_click(315, 846)

    # 'Browse'图标
    def browser_cron(self):
        return self.find_ele(xpath='//XCUIElementTypeButton[@name="Browse"]')
        # return self.find_ele(name='Browse')
        # return self.find_ele(nameContains='Bro')  # 匹配name文本包含的内容

    # 搜索文本框
    def search_field(self):
        # return self.find_ele(xpath='//XCUIElementTypeSearchField[@name="Search"]')
        # return self.find_ele(label="Search")
        return self.find_ele(name="Search")

    # "心率"tab
    def heart_rate_tab(self):
        return self.find_ele(nameContains="BPM")

    # '添加数据'按钮
    def add_data_btn(self):
        return self.find_ele(xpath='//XCUIElementTypeButton[@name="Add Data"]')
        # return self.find_ele(xpath='//NavigationBar/Button[2]')
        # return self.find_ele(name="Add Data")

    # '心率'输入框
    def bpm_field(self):
        # return self.find_ele(xpath='//XCUIElementTypeTextField[@name="BPM"]')
        return self.find_ele(label="BPM123")

    # '添加'按钮
    def add_btn(self):
        # return self.find_ele(xpath='//XCUIElementTypeButton[@name="Add"]')
        return self.find_ele(label="Add")

    """
        【 页 面 功 能 】
    """

    def add_heart_rate(self, heart_rate):
        """
        添加心率
        :return:
        """

        # 从屏幕'正中间'往'顶部'划动（效果：屏幕往'下'翻动）
        self.swipe_up()
        time.sleep(2)
        self.screenshot(image_name="heart_rate_1.png")

        # 点击 Browse 图标
        # self.touch_browser_cron()
        self.browser_cron().click()
        time.sleep(2)
        self.screenshot(image_name="heart_rate_2.png")

        # 搜索框输入 Heart
        search_input = self.search_field()
        self.log.info("search_input.name : " + str(search_input.name))
        self.log.info("search_input.bounds.width : " + str(search_input.bounds.width))
        self.log.info("search_input.bounds.height : " + str(search_input.bounds.height))
        search_input.click_exists(timeout=3.0)
        time.sleep(1)
        search_input.set_text("Heart")
        time.sleep(2)
        self.screenshot(image_name="heart_rate_3.png")

        # 判断"Nutrition"内容是否消失
        is_gone = self.content_is_gone("Nutrition", 3.0)
        self.log.info("内容 Nutrition 是否消失: " + str(is_gone))
        time.sleep(2)

        # 判断"Heart Rate"内容是否存在
        is_exist = self.content_is_exist("Heart Rate", 5.0)
        self.log.info("内容 Heart Rate 是否存在: " + str(is_exist))
        time.sleep(2)

        # 点击'心率'tab
        self.heart_rate_tab().click()
        time.sleep(2)
        self.screenshot(image_name="heart_rate_4.png")

        # 点击'添加数据'按钮
        self.add_data_btn().click()
        self.screenshot(image_name="heart_rate_5.png")

        # 输入心率数据
        bpm_input = self.bpm_field()
        bpm_input.click()
        bpm_input.set_text(heart_rate)
        time.sleep(2)
        self.screenshot(image_name="heart_rate_6.png")

        # 点击添加按钮
        self.add_btn().click()
        time.sleep(2)
        self.assert_content_and_screenshot(image_name="heart_rate_7.png", content="哈哈哈",
                                           error_msg="页面跳转失败！- 找不到'哈哈哈'内容")

    # def search_wx(self, content):
    #     """
    #     搜索功能(微信)
    #     :return:
    #     """
    #
    #     # 获取搜索文本框1，并点击
    #     self.screenshot(image_name="wx_1_search_field.png")
    #     self.search_field_1().click()
    #     time.sleep(2)
    #
    #     # 获取搜索文本框2，并输入内容
    #     search_field = self.search_field_2()
    #     search_field.send_keys(content)
    #     time.sleep(2)
    #     self.screenshot(image_name="wx_2_search_field.png")
    #
    #     # 获取搜索按钮，并点击
    #     self.search_btn().click()
    #     time.sleep(2)
    #
    #     # 上滑
    #     self.swipe_up()
    #     time.sleep(2)
    #
    #     # 下滑
    #     self.swipe_down()
    #     time.sleep(2)
    #
    #     # 获取"微信"tab，并点击
    #     wx_tab = self.get_search_ele(content)
    #     wx_tab.click()
    #
    #     # 判断页面内容是否存在，同时截屏、然后断言
    #     self.assert_content_and_screenshot(image_name="wx_2_target_page.png", content="哈哈哈", error_msg="页面跳转失败！- 找不到'哈哈哈'内容")
    #
    # def search_bd(self, content):
    #     """
    #     搜索功能(百度)
    #     :return:
    #     """
    #
    #     # 获取搜索文本框1，并点击
    #     self.screenshot(image_name="bd_1_search_field.png")
    #     self.search_field_1().click()
    #     time.sleep(2)
    #
    #     # 获取搜索文本框2，并输入内容
    #     search_field = self.search_field_2()
    #     search_field.send_keys(content)
    #     time.sleep(2)
    #     self.screenshot(image_name="bd_2_search_field.png")
    #
    #     # 获取搜索按钮，并点击
    #     self.search_btn().click()
    #     time.sleep(2)
    #
    #     # 上滑
    #     self.swipe_up()
    #     time.sleep(2)
    #
    #     # 下滑
    #     self.swipe_down()
    #     time.sleep(2)
    #
    #     # 获取"百度"tab，并点击
    #     wx_tab = self.get_search_ele("哈哈哈")
    #     wx_tab.click()
    #
    #     # 判断页面内容是否存在，同时截屏、然后断言
    #     self.assert_content_and_screenshot(image_name="bd_2_target_page.png", content=content, error_msg="页面跳转失败！- 找不到'" + content + "'内容")
