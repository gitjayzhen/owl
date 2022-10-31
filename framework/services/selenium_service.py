# -*- coding:UTF-8 -*-

import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from framework.utils.reporter.logging_porter import LoggingPorter


class SeleniumDriverBrowser(object):
    """
        这边是通过驱动实例化selenium webdriver，的服务启动者, 并返回webdriver
    """
    def __init__(self, properties):
        self.log4py = LoggingPorter()
        self.driver = None
        self.properties = properties
        # self.waitTimeout = properties.waitTimeout
        # self.scriptTimeout = properties.scriptTimeout
        # self.pageLoadTimeout = properties.pageLoadTimeout

    def init_browser(self):
        """
        根据实例对象的参数，来具体启动浏览器，不管启动是否成功或启动异常，都会返回driver
        :return:
        """
        browser_name = self.properties.browser
        if "chrome" == browser_name:
            self.driver = self.start_chrome_browser()
        elif "ie" == browser_name:
            self.driver = self.start_ie_browser()
        elif "firefox" == browser_name:
            self.driver = self.start_firefox_browser()
        else:
            self.driver = self.start_firefox_browser()
        return self.driver

    def start_firefox_browser(self):
        driver = None
        try:
            # 设置浏览器的配置参数
            # fp = webdriver.FirefoxProfile()
            # fp.set_preference("browser.download.folderList", 2)
            # fp.set_preference("browser.download.manager.showWhenStarting", False)
            # fp.set_preference("browser.download.dir", os.getcwd())
            # fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")
            # fp.add_extension("path: url, path to .xpi, or directory of addons")
            # browser = webdriver.Firefox(firefox_profile=fp)

            if self.properties.type == '0':
                # 实例化remote driver
                pass
            elif self.properties.type == '1':
                os.environ["webdriver.firefox.driver"] = self.properties.browserdriver
                log_path = os.path.join(self.properties.logsPath, "geckodriver.log")
                driver = webdriver.Firefox(executable_path=self.properties.browserdriver, log_path=log_path)
            self.config_browser(driver)
            self.log4py.debug("初始化火狐浏览器成功")
        except Exception as e:
            self.log4py.error("getFirefoxDriver()方法发生异常，异常信息：" + str(e))
            driver.quit()
            return None
        return driver

    def start_chrome_browser(self):
        driver = None
        try:
            chrome_options = Options()
            d = DesiredCapabilities.CHROME.copy()
            # 启动浏览器的时候不想看的浏览器运行，那就加载浏览器的静默模式，让它在后台偷偷运行。用headless
            # chrome_options.add_argument("headless")
            chrome_options.add_argument("--disable-extensions")
            # 忽略掉这个警告提示语
            chrome_options.add_argument('--disable-infobars')
            chrome_options.add_argument('--log-level=0')
            # chrome_options.add_argument('--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1')
            # chrome_options.add_experimental_option("mobileEmulation", {"deviceName": "iPhone X"})
            d.update(chrome_options.to_capabilities())

            # 添加chrome的插件
            # chrome_options.add_extension("extension: path to the *.crx file")

            if self.properties.type == '0':
                remote = self.properties.remoteProfile.pop('url')
                d.update(self.properties.remoteProfile)
                d.update(chrome_options.to_capabilities())
                driver = webdriver.Remote(command_executor=remote, desired_capabilities=d)
            elif self.properties.type == '1':
                # 设置chrome 浏览器的驱动环境变量
                os.environ["webdriver.chrome.driver"] = self.properties.browserdriver
                # 设置chrome 的二进制可执行文件: 启动不在默认安装路径的firefox浏览器
                # os.environ["webdriver.chrome.bin"] = "/path/to/chrome/32/chrome.exe"
                driver = webdriver.Chrome(executable_path=self.properties.browserdriver, desired_capabilities=d)
            self.config_browser(driver)
            self.log4py.debug("初始化谷歌浏览器成功")
        except Exception as e:
            self.log4py.error("getChromeDriver()方法出现异常 : " + str(e))
            try:
                driver.quit()
            except Exception as e:
                self.log4py.error("及时没有启动浏览器，也要有关闭操作")
            return None
        return driver

    def start_ie_browser(self):
        driver = None
        try:
            ie_dc = DesiredCapabilities.INTERNETEXPLORER
            ie_dc['INTRODUCE_FLAKINESS_BY_IGNORING_SECURITY_DOMAINS'] = True
            ie_dc['ignoreProtectedModeSettings'] = True
            ie_dc['NATIVE_EVENTS'] = False
            ie_dc["unexpectedAlertBehaviour"] = "accept"

            os.environ["webdriver.ie.driver"] = self.properties.browserdriver
            driver = webdriver.Ie(self.properties.browserdriver, ie_dc)
            self.config_browser(driver)
            self.log4py.debug("初始化IE浏览器成功")
        except Exception as e:
            self.log4py.error("getInternetExplorerDriver()方法出现异常"+ str(e))
            driver.quit()
            return None
        return driver

    def config_browser(self, driver):
        driver.set_page_load_timeout(self.properties.pageLoadTimeout)
        self.log4py.debug("set pageLoadTimeout : " + self.properties.pageLoadTimeout)
        driver.implicitly_wait(self.properties.waitTimeout)
        self.log4py.debug("set waitTimeout : " + self.properties.waitTimeout)
        driver.set_script_timeout(self.properties.scriptTimeout)
        self.log4py.error("set scriptTimeout : " + self.properties.scriptTimeout)
        driver.maximize_window()
        self.get(driver, self.properties.baseURL, 3)

    def stop_browser(self):
        try: 
            self.driver.quit()
            self.log4py.debug("stop Driver")
        except Exception as e:
            self.log4py.error("执行stopWebDriver()方法发生异常，异常信息："+ str(e))

    def get(self, driver, url, action_count=2):
        for i in range(action_count):
            try:
                driver.get(url)
                self.log4py.debug("navigate to url [ " + url + " ]")
                break
            except Exception as e:
                self.log4py.error("访问初始化URL报错 ： " + str(e))



