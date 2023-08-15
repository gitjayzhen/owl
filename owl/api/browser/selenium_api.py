# -*- coding:UTF-8 -*-

import random
import time

from selenium.common import exceptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from owl.lib.date.date_formatter import get_formate_time
from owl.lib.reporter.logging_porter import LoggingPorter

'''
 * 封装整体思路：
 * 1、封装常用方法
 * 2、对于封装过的方法，失败的操作在operationCheck中进行截图
'''


class SeleniumWorkApi(object):
    """
    对 selenium 的原生 api 进行一定的改造和封装
    """

    def __init__(self, driver, properties):
        self.log4py = LoggingPorter()

        self.capturePath = properties.capturePath
        self.pauseTime = int(properties.pauseTime)
        self.implicitly_wait_time = int(properties.waitTimeout)

        self.driver = driver
        self.Find = By

    def stop_web_driver(self):
        try:
            self.driver.quit()
            self.log4py.debug("stop web driver")
        except Exception as e:
            self.log4py.error("执行stopWebDriver()方法发生异常，异常信息：" + str(e))

    def pause(self, second):
        """
        睡眠操作
        :param second: 秒单位
        :return: 无
        """
        try:
            time.sleep(second)
        except Exception as e:
            self.log4py.error("pause error:" + str(e))

    def capture_screenshot(self, file_path):
        """
         截取屏幕截图并保存到指定路径
        :param file_path: 保存屏幕截图完整文件名称及路径
        :return: 无
        """
        try:
            self.log4py.info("截图文件请查看：{}".format(file_path))
            self.driver.get_screenshot_as_file(file_path)
        except Exception as e:
            self.log4py.error("保存屏幕截图失败，失败信息：" + str(e))

    def capture(self):
        date_time = get_formate_time("%Y%m%d-%H%M%S%f")
        capture_name = self.capturePath + date_time + ".png"
        self.capture_screenshot(capture_name)

    def operation_check(self, method_name, is_succeed):
        """
        就是校验方法时候执行成功，如果没有就进行截图操作
        :param method_name:  执行的方法
        :param is_succeed:  判断条件
        :return:
        """
        if is_succeed:
            self.log4py.info("method 【" + method_name + "】 运行通过！")
        else:
            date_time = get_formate_time("-%Y%m%d-%H%M%S%f")
            capture_name = self.capturePath + method_name + date_time + ".png"
            self.capture_screenshot(capture_name)
            self.log4py.error("method 【" + method_name + "】 运行失败，请查看截图快照：" + capture_name)

    def get(self, url, action_count=2):
        """
        * rewrite the get method, adding user defined log</BR>
        * 地址跳转方法，使用WebDriver原生get方法，加入失败重试的次数定义。
        :param url: 访问的网页地址
        :param action_count:错误尝试次数
        :return:
        """
        is_succeed = False
        for i in range(action_count):
            try:
                self.driver.get(url)
                is_succeed = True
                self.log4py.debug("navigate to url [ " + url + " ]")
                break
            except Exception as e:
                self.log4py.error(e)
        self.operation_check("get", is_succeed)

    def navigate_back(self):
        """
        navigate back</BR> 地址跳转方法，与WebDriver原生navigate.back方法内容完全一致。
        :return:
        """
        self.driver.back()
        self.log4py.debug("navigate back")

    def navigate_forward(self):
        """
        navigate forward</BR> 地址跳转方法，与WebDriver原生navigate.forward方法内容完全一致。
        :return:
        """
        self.driver.forward()
        self.log4py.debug("navigate forward")

    def is_alert_exists(self, timeout):
        """
        在指定的时间内判断弹出的对话框（Dialog）是否存在。
        :param timeout:  超时时间
        :return:
        """
        is_succeed = False
        time_begins = time.time()
        while time.time() - time_begins <= timeout * 1000:
            try:
                self.driver.switch_to.alert()
                is_succeed = True
                break
            except Exception as e:
                self.log4py.error(e)
        self.operation_check("isAlertExists", is_succeed)
        return is_succeed

    def find_element(self, by, value, timeout=3):
        """
        重写api的方法，按照指定的定位方式寻找象。
        :param by: 寻找元素的方式
        :param value: 元素
        :param timeout: 超时时间
        :return: 元素对象
        """
        is_succeed = False
        self.log4py.debug("find elements [" + str(value) + "]")
        element = None
        time_begins = time.time()
        while time.time() - time_begins <= timeout:
            try:
                element = self.driver.find_element(by, value)
                is_succeed = True
                self.log4py.debug("find element [" + str(value) + "] success")
                break
            except Exception as e:
                self.log4py.error(e)
        self.operation_check("find_element", is_succeed)
        return element

    def find_elements(self, by, value, timeout):
        """
        重写api的方法，按照指定的定位方式寻找象。
        :param by: 寻找元素的方式
        :param value: 元素
        :param timeout: 超时时间
        :return: 元素对象
        """
        is_succeed = False
        self.log4py.debug("find elements [" + str(value) + "]")
        elements = None
        time_begins = time.time()
        while time.time() - time_begins <= timeout:
            try:
                elements = self.driver.find_elements(by, value)
                is_succeed = True
                self.log4py.debug("find element [" + str(value) + "] success")
                break
            except Exception as e:
                self.log4py.error(e)
        self.operation_check("find_elements", is_succeed)
        return elements

    def get_window_title(self):
        """
        * rewrite the getTitle method, adding user defined log
        * 与工具原生API作用完全一致，只是增加了操作结果检查和日志记录。
        :return: 返回网页的title
        """
        title = self.driver.title
        self.log4py.debug("current window title is :" + title)
        return title

    def get_current_url(self):
        """
        * rewrite the getCurrentUrl method, adding user defined log</BR>
        * 与工具原生API作用完全一致，只是增加了操作结果检查和日志记录。
        * @return the url on your current session
        :return:
        """
        url = self.driver.current_url()
        self.log4py.debug("current page url is :" + url)
        return url

    def get_window_handles(self):
        """
        * rewrite the getWindowHandles method, adding user defined log</BR>
        * 与工具原生API作用完全一致，只是增加了操作结果检查和日志记录。
        :return:
        """
        handles = self.driver.window_handles()
        self.log4py.debug("window handles are: " + handles)
        return handles

    def get_window_handle(self):
        """
        * rewrite the getWindowHandle method, adding user defined log</BR>
        * 与工具原生API作用完全一致，只是增加了操作结果检查和日志记录。
        *return the window handle
        """
        handle = self.driver.current_window_handle()
        self.log4py.debug("current window handle is:" + handle)
        return handle

    def get_page_source(self):
        """
        * rewrite the getPageSource method, adding user defined log</BR>
        * 与工具原生API作用完全一致，只是增加了操作结果检查和日志记录。
        * @return the page source
        """
        source = self.driver.page_source()
        # 日志就不打印了  内容太多了
        # log4py.debug("get PageSource : [ " + source + " ]")
        return source

    def get_tag_tame(self, by, value):
        """
        * rewrite the getTagName method, find the element   and get its tag
        * name</BR> 与工具原生API作用完全一致，只是增加了操作结果检查和日志记录。
        :param by:
        :param value:  the locator you want to find the element
        :return:
        """
        tag_name = self.driver.find_element(by, value).tag_name()
        self.log4py.debug("element [ " + str(by) + " ]'s TagName is: " + tag_name)
        return tag_name

    def get_attribute(self, by, value, attribute_name):
        """
        * rewrite the getAttribute method, find the element   and get its
        * attribute value</BR> 与工具原生API作用完全一致，只是增加了操作结果检查和日志记录。
        * @param :the locator you want to find the element
        * @param attributeName:the name of the attribute you want to get
        * @return the attribute value
        :param by:
        :param value:
        :param attributeName:
        :return:
        """
        value = self.driver.find_element(by, value).get_attribute(attribute_name)
        self.log4py.debug("element [ " + str(by) + " ]'s " + attribute_name + "is: " + value)
        return value

    def clear(self, element):
        """
        * rewrite the clear method, adding user defined log</BR>
        * 与工具原生API作用完全一致，只是增加了操作结果检查和日志记录。
        * @param element:the webelement you want to operate
        :param element:
        :return:
        """
        element.clear()
        self.log4py.debug("element [ " + element + " ] cleared")

    def click(self, by, value):
        """
        * rewrite the click method, adding user defined log</BR>
        * 与工具原生API作用完全一致，只是增加了操作结果检查和日志记录。
        * @param element:the webelement you want to operate
        :param by:
        :param value:
        :return:
        """
        self.driver.implicitly_wait(self.implicitly_wait_time)
        element = self.find_element(by, value, self.implicitly_wait_time)
        element.click()
        self.log4py.debug("click on element [ " + str(element) + " ] ")

    def execute_js(self, js):
        if js is not None or js != "":
            self.driver.execute_script(js)

    def key_event(self, event):
        ActionChains(self.driver).send_keys(event)

    def send_keys(self, by, value, text):
        """
        * rewrite the sendKeys method, adding user defined log</BR>
        * 与工具原生API作用完全一致，只是增加了操作结果检查和日志记录。
        * @param element:the webelement you want to operate
        :param by:
        :param value:
        :param text:
        :return:
        """
        try:
            element = self.find_element(by, value, self.implicitly_wait_time)
            element.clear()
            element.send_keys(text)
            self.log4py.debug("input text [ " + text + " ] to element [ " + str(element) + " ]")
        except exceptions.NoSuchElementException as e:
            self.log4py.error("send_keys func happend NoSuchElementException : {}".format(str(e)))

    def is_selected(self, by, value):
        """
        * rewrite the isSelected method, the element to be find  </BR>
        * 与工具原生API作用完全一致，只是增加了操作结果检查和日志记录。
        * @param :the locator you want to find the element
        * @return the bool value of whether is the WebElement selected
        :param by:
        :param value:
        :return:
        """
        is_selected = self.driver.find_element(by, value).is_selected()
        self.log4py.debug("element [ " + value + " ] selected? " + str(is_selected))
        return is_selected

    def is_element_present(self, by, value, timeout):
        """
        查看父元素
        :param by:
        :param value:
        :param timeout:
        :return:
        """
        is_succeed = False
        self.log4py.debug("find element [" + value + "]")
        time_begins = time.time()
        while time.time() - time_begins <= timeout:
            try:
                self.driver.find_element(by, value)
                is_succeed = True
                self.log4py.debug("find element [" + value + "] success")
                break
            except Exception as e:
                self.log4py.error(e)
            self.pause(self.pauseTime)
        self.operation_check("is_element_present", is_succeed)
        return is_succeed

    def weblist_random_select(self, by, value, timeout):
        """
        对一个元素集进行随机选择
        :param by:
        :param value:
        :param timeout:
        :return:
        """
        is_succeed = False
        time_begins = time.time()
        while time.time() - time_begins <= timeout:
            try:
                web_select = self.driver.find_element(by, value)
                select_element = Select(web_select)
                ooptions = select_element.options
                ooption = random.choice(ooptions)
                item_value = ooption.get_attribute("value")
                select_element.select_by_value(item_value)
                is_succeed = True
                self.log4py.debug("item selected by item value [ " + item_value + " ] on [ " + str(by) + " ]")
                break
            except Exception as e:
                self.log4py.error(e)
            self.pause(self.pauseTime)
        self.operation_check("weblist_random_select", is_succeed)

    def select_by_value(self, by, value, item_value, timeout):
        is_succeed = False
        try:
            if self.is_element_present(by, value, timeout):
                element = self.driver.find_element(by, value)
                select = Select(element)
                select.select_by_value(item_value)
                self.log4py.debug("item selected by item value [ " + item_value + " ] on [ " + value + " ]")
                is_succeed = True
        except Exception as e:
            self.log4py.error(e)
        self.operation_check("selectByValue", is_succeed)

    def is_enabled(self, by, value):
        """
        * rewrite the isEnabled method, the element to be find  </BR>
        * 与工具原生API作用完全一致，只是增加了操作结果检查和日志记录。
        * @param ：the locator you want to find the element
        * @return the bool value of whether is the WebElement enabled
        :param by:
        :param value:
        :return:
        """
        is_enable = self.driver.find_element(by, value).is_enabled()
        self.log4py.debug("element [ " + str(by) + " ] enabled? " + str(is_enable))
        return is_enable

    def get_text(self, by, value):
        """
        * rewrite the getText method, find the element   and get its own
        * text</BR> 与工具原生API作用完全一致，只是增加了操作结果检查和日志记录。
        * @param :the locator you want to find the element
        * @return the text
        :param by:
        :param value:
        :return:
        """
        text = self.driver.find_element(by, value).text
        self.log4py.debug("element [ " + value + " ]'s text is: " + text)
        return text

    def is_displayed(self, by, value):
        """
        * rewrite the isDisplayed method, the element to be find  </BR>
        * 与工具原生API作用完全一致，只是增加了操作结果检查和日志记录。
        * @param :the locator you want to find the element
        * @return the bool value of whether is the WebElement displayed
        :param by:
        :param value:
        :return:
        """
        is_display = False
        try:
            is_display = self.driver.find_element(by, value).is_displayed()
            self.log4py.debug("element [ " + str(by) + " ] displayed? " + str(is_display))
        except Exception as e:
            self.log4py.error("element元素没有点位到" + str(e))
        return is_display

    def clear_handle_cache(self, window_handles):
        """
        根据窗口list，如果存在就保留，不存在就清除handle
        :param window_handles:
        :return:
        """
        errors = []
        for handle in window_handles:
            try:
                self.driver.switch_to().window(handle)
                self.driver.title()
            except Exception as e:
                errors.append(str(handle))
                self.log4py.debug("window handle " + str(errors) + " does not exist acturely!")
        for i in range(len(errors)):
            window_handles.remove(errors[i])
        return window_handles

    def select_window_handle(self, win_handle):
        """
        * switch to window  handle</BR> 按照指定句柄选择窗口。切换到一个存在句柄（或者说当前还存在的）的窗口。
        * @param windowHandle:the handle of the window to be switched to
        :param window_handle:
        :return:
        """
        is_succeed = False
        try:
            window_handles = self.driver.window_handles()
            window_handles = self.clear_handle_cache(window_handles)
            for handle in window_handles:
                if win_handle.equals(handle):
                    self.driver.switch_to().window(handle)
                    is_succeed = True
                    break
        except Exception as e:
            self.log4py.error(e)
        self.operation_check("select_window_handle", is_succeed)

    def scrollbar_slide_to_bottom(self, element_id):
        """
        通过元素将页面滑动到页面最下方：将页面滚动条拖到底部
        """
        # js="var q=document.documentElement.scrollTop=10000"
        js = "var q=document.getElementById('%s').scrollTop=10000" % element_id
        self.driver.execute_script(js)
        time.sleep(3)
        self.log4py.debug("将元素id为%s滑动到底部" % element_id)

    def scrollbar_slide_to_top(self, elementid):
        # 将页面滚动条拖到顶部
        # js="var q=document.documentElement.scrollTop=0"
        js = "var q=document.getElementById('%s').scrollTop=0" % elementid
        self.driver.execute_script(js)
        time.sleep(3)
        self.log4py.debug("将元素%s滑动到底部" % elementid)

    def fouse(self, by, value):
        # 元素聚焦：
        target = self.find_element(by, value)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)

    def accept_alert(self):
        try:
            self.driver.switch_to.alert().accept()
            self.log4py.debug("切换到弹窗，并点击确定按钮")
        except Exception as e:
            self.log4py.error("接受弹窗，出现异常：" + str(e))

    def close_window(self, window_title, index):
        """
        * close window  window title and its index if has the same title,
        *  full pattern</BR> 按照网页标题选择并且关闭窗口，重名窗口按照指定的重名的序号关闭
        * </BR>适用于有重名title的窗口，标题内容需要全部匹配。
        * @param windowTitle:the title of the window to be closed.
        * @param index:the index of the window which shared the same title, beginswith 1.
        :param window_title:
        :param index:
        :return:
        """
        is_succeed = False
        try:
            win_list = []
            window_handles = self.driver.window_handles()
            window_handles = self.clear_handle_cache(window_handles)
            for handle in window_handles:
                self.driver.switch_to.window(handle)
                if window_title.equals(self.get_window_title()):
                    win_list.append(handle)
            self.driver.switch_to.window(win_list[index - 1])
            self.driver.close()
            self.log4py.debug("window [ " + window_title + " ] closed  index [" + index + "]")
            is_succeed = True
        except Exception as e:
            self.log4py.error(e)

        self.operation_check("close_window", is_succeed)

    def close_window_except(self, window_title, index):
        """
        @TODO 逻辑还有问题，待完善
        :param window_title:
        :param index:
        :return:
        """
        is_succeed = False
        try:
            window_handles = self.driver.window_handles()
            window_handles = self.clear_handle_cache(window_handles)
            for handle in window_handles:
                self.driver.switch_to.window(handle)
                title = self.driver.title()
                if window_title.equals(title):
                    self.driver.switch_to.default_content()
                    self.driver.close()
            win_list = self.driver.window_handles()
            for i in range(len(win_list)):
                if i + 1 != index:
                    self.driver.switch_to.default_content()
                    self.driver.close()
            self.log4py.debug("keep only window [ " + window_title + " ]  title index [ " + index + " ]")
            is_succeed = True
        except Exception as e:
            self.log4py.error(e)
        self.operation_check("close_window_except", is_succeed)

    def close_window_handle(self, window_handle):
        """
        * close window  specified window hanlde,   full pattern</BR>
        * 关闭指定句柄的窗口。
        * @param windowHandle:the hanlde of the window to be closed.
        :param windowHandle:
        :return:
        """
        is_succeed = False
        try:
            window_handles = self.driver.window_handles()
            window_handles = self.clear_handle_cache(window_handles)
            for handle in window_handles:
                if window_handle.equals(handle):
                    self.driver.switch_to.window(handle)
                    self.driver.close()
                    break
            self.log4py.debug("window [ " + window_handle + " ] closed ")
            is_succeed = True
        except Exception as e:
            self.log4py.error(e)
        self.operation_check("close_window_handle", is_succeed)

    def close_window_except_handle(self, window_handle):
        """
        * close windows except specified window hanlde,   full pattern</BR>
        * 关闭除了指定句柄之外的所有窗口。
        * @param windowHandle: the hanlde of the window not to be closed.
        :param windowHandle:
        :return:
        """
        is_succeed = False
        try:
            window_handles = self.driver.window_handles()
            #            window_handles = clearHandleCache(window_handles)
            for handle in window_handles:
                if window_handle != handle:
                    self.driver.switch_to.window(handle)
                    self.driver.close()
            self.log4py.debug("all windows closed except handle [ " + window_handle + " ]")
            is_succeed = True
        except Exception as e:
            self.log4py.error(e)
        self.operation_check("close_window_except_handle", is_succeed)

    def double_click(self, by, value, timeout):
        is_succeed = False
        try:
            element = self.find_element(by, value, timeout)
            ActionChains(self.driver).double_click(element).perform()
            self.log4py.debug("doubleClick on element [ " + str(by) + " ] ")
            is_succeed = True
        except Exception as e:
            self.log4py.error(e)
        self.operation_check("double_click", is_succeed)

    def move_to_element(self, by, value, timeout):
        """
        Moving the mouse to the middle of an element.
        to_element: The element to move to.
        :param by:
        :param value:
        :param timeout:
        :return:
        """
        is_succeed = False
        try:
            element = self.find_element(by, value, timeout)
            ActionChains(self.driver).move_to_element(element).perform()
            self.log4py.debug("moveToElement [ " + str(by) + " ] ")
            is_succeed = True

        except Exception as e:
            self.log4py.error(e)
        self.operation_check("move_to_element", is_succeed)

    def right_click(self, by, value, timeout):
        """
        * right click on the element</BR> 在等到对象可见之后鼠标右键点击指定的对象。
        * @param
        *            the locator you want to find the element
        * @param timeout
        *            超时时间，单位：秒
        :param by:
        :param timeout:
        :return:
        """
        is_succeed = False
        try:
            element = self.find_element(by, value, timeout)
            ActionChains(self.driver).context_click(element).perform()
            self.log4py.debug("rightClick on element [ " + str(by) + " ] ")
            is_succeed = True
        except Exception as e:
            self.log4py.error(e)
        self.operation_check("right_click", is_succeed)

    def submit_form(self, by, value, timeout):
        is_succeed = False
        try:
            if self.is_element_present(by, value, timeout):
                self.find_element(by, value).submit()
                self.log4py.debug("submit on element [ " + str(by) + " ]")
                is_succeed = True
        except Exception as e:
            self.log4py.error(e)
        self.operation_check("submit", is_succeed)

    def drag_and_drop(self, by, value1, value2, timeout):
        is_succeed = False
        try:
            source = self.find_element(by, value1, timeout)
            target = self.find_element(by, value2, timeout)
            ActionChains(self.driver).drag_and_drop(source, target).perform()
            self.log4py.info("drap and drop func had exce")
            is_succeed = True
        except Exception as e:
            self.log4py.error("drag and drop func happed error: " + str(e))
        self.operation_check("drag_and_drop", is_succeed)
