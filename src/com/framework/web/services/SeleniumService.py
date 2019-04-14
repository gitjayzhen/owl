# -*- coding:UTF-8 -*-
'''
Created on 2016年4月26日
@author: jayzhen
'''
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from com.framework.utils.reporterUtil.LoggingPorter import LoggingPorter
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class InitWebDriver(object):
    """
        这边是通过驱动实例化selenium webdriver，的服务启动者, 并返回webdriver
    """
    def __init__(self, properties):
        self.log4py = LoggingPorter()
        self.driver = None
        self.properties = properties
        self.waitTimeout = properties.waitTimeout
        self.scriptTimeout = properties.scriptTimeout
        self.pageLoadTimeout = properties.pageLoadTimeout

    def run_browser(self):
        """
        根据实例对象的参数，来具体启动浏览器，不管启动是否成功或启动异常，都会返回driver
        :return:
        """
        browsername = self.properties.browser
        if "chrome" == browsername:
            self.driver = self.start_chrome_driver()
        elif "ie" == browsername:
            self.driver = self.start_ie_driver()
        elif "firefox" == browsername:
            self.driver = self.start_firefox_driver()
        else:
            self.driver = self.start_firefox_driver()
        return self.driver

    def start_firefox_driver(self):
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
            driver.set_page_load_timeout(self.pageLoadTimeout)
            self.log4py.debug("set pageLoadTimeout : "+self.pageLoadTimeout)
            driver.implicitly_wait(self.waitTimeout)
            self.log4py.debug("set waitTimeout : " + self.waitTimeout)
            driver.set_script_timeout(self.scriptTimeout)
            self.log4py.error("set scriptTimeout : " + self.scriptTimeout)
            self.log4py.debug("初始化火狐浏览器成功")
            driver.maximize_window()
            self.get(driver, self.properties.baseURL, 3)
        except Exception, e:
            self.log4py.error("getFirefoxDriver()方法发生异常，异常信息：" + str(e))
            driver.quit()
            return None
        return driver

    def start_chrome_driver(self):
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
            driver.set_page_load_timeout(self.pageLoadTimeout)
            self.log4py.debug("set pageLoadTimeout : " + self.pageLoadTimeout)
            driver.implicitly_wait(self.waitTimeout)
            self.log4py.debug("set waitTimeout : " + self.waitTimeout)
            driver.set_script_timeout(self.scriptTimeout)
            self.log4py.debug("set scriptTimeout : " + self.scriptTimeout)
            self.log4py.debug("初始化谷歌浏览器成功")
            driver.maximize_window()
            self.get(driver, self.properties.baseURL, 3)
        except Exception, e:
            self.log4py.error("getChromeDriver()方法出现异常 : " + str(e))
            try:
                driver.quit()
            except Exception, e:
                self.log4py.error("及时没有启动浏览器，也要有关闭操作")
            return None
        return driver

    def start_ie_driver(self):
        driver = None
        try:
            ie_dc = DesiredCapabilities.INTERNETEXPLORER
            ie_dc['INTRODUCE_FLAKINESS_BY_IGNORING_SECURITY_DOMAINS'] = True
            ie_dc['ignoreProtectedModeSettings'] = True
            ie_dc['NATIVE_EVENTS'] = False
            ie_dc["unexpectedAlertBehaviour"] = "accept"

            os.environ["webdriver.ie.driver"] = self.properties.browserdriver
            driver = webdriver.Ie(self.properties.browserdriver, ie_dc)

            driver.set_page_load_timeout(self.pageLoadTimeout)
            self.log4py.debug("set pageLoadTimeout : " + self.pageLoadTimeout)
            driver.implicitly_wait(self.waitTimeout)
            self.log4py.debug("set waitTimeout : " + self.waitTimeout)
            driver.set_script_timeout(self.scriptTimeout)
            self.log4py.debug("set scriptTimeout : " + self.scriptTimeout)
            driver.maximize_window()
            
            self.log4py.debug("初始化IE浏览器成功")
            self.get(driver, self.properties.baseURL, 3)
        except Exception, e:
            self.log4py.error("getInternetExplorerDriver()方法出现异常"+ str(e))
            driver.quit()
            return None
        return driver

    def stop_web_driver(self):
        try: 
            self.driver.quit()
            self.log4py.debug("stop Driver")
        except Exception, e:
            self.log4py.error("执行stopWebDriver()方法发生异常，异常信息："+ str(e))

    def get(self, driver, url, actionCount):
        for i in range(actionCount):
            try:
                driver.get(url)
                self.log4py.debug("navigate to url [ " + url + " ]")
                break
            except Exception, e:
                self.log4py.error("访问初始化URL报错 ： " + str(e))



