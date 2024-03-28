# -*- coding:utf-8 -*-

"""
@author: jayzhen
@file: t_se_gesture.py
@time: 2024/03/28 15:33
"""
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from docker.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def run_remote_se3():
    chrome_options = webdriver.ChromeOptions()
    d = DesiredCapabilities.CHROME.copy()
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument('--disable-infobars')
    chrome_options.add_argument('--log-level=0')
    chrome_options.add_experimental_option('w3c', False)
    chrome_options.add_experimental_option("mobileEmulation",
                                           {"deviceMetrics": {"width": 414, "height": 736, "pixelRatio": 3.0},
                                            "userAgent": "Mozilla/5.0 (Linux; U; Android 8.1.0; zh-cn; MI 8 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/9.2 Mobile Safari/537.36"})
    d.update(chrome_options.to_capabilities())
    driver = webdriver.Remote(command_executor='http://192.168.1.18:4444/wd/hub', desired_capabilities=d)
    driver.maximize_window()
    driver.get(
        'https://m.baidu.com/web/searchList.jsp?uID=AAF0MmFlKgAAAAqPLFl94wEAZAM%3D&v=5&dp=1&pid=sogou-waps-7880d7226e872b77&w=1283&t=1570596369820&s_t=1570596606799&s_from=result_up&htprequery=%E5%A4%A9%E6%B0%94%E5%BA%94%E7%94%A8&keyword=%E5%A4%A9%E6%B0%94&pg=webSearchList&rcer=gNz_a8U1sUAKzX9o&s=%E6%90%9C%E7%B4%A2&suguuid=58f46974-4a26-426c-adcb-fc8a1dfa88df&sugsuv=AAF0MmFlKgAAAAqPLFl94wEAZAM&sugtime=1570596606799')

    action = webdriver.ActionChains(driver)
    # elemt = driver.find_element_by_class_name('weather-data-list')
    elemt = driver.find_element(By.CSS_SELECTOR, '.border-top .weather-data-list')

    action.scroll_by_amount(100, 100).perform()
    time.sleep(3)
    action.scroll_to_element(elemt).perform()

    time.sleep(5)
    driver.quit()


def run_remote():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-dev-shm-usage')
    # chrome_options.add_argument('--incognito')
    # chrome_options.add_argument("--window-size=1920,1080")
    # chrome_options.add_argument('--verbose')
    # chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--remote-debugging-port=9222')
    # chrome_options.add_argument('--disable-extensions')
    """
    {"browserName":"chrome","browserVersion":"120.0",
    "goog:chromeOptions":{"binary":"/usr/bin/google-chrome"},
    "platformName":"linux",
    "se:noVncPort":7900,
    "se:vncEnabled":true,
    "se:webDriverExecutable":"/opt/docker/chromedriver-120.0.6099.71"}
    """
    chrome_options.set_capability("browserName", "chrome")
    chrome_options.set_capability("browserVersion", "120.0.6099.71")
    chrome_options.set_capability("platformName", "linux")
    chrome_options.set_capability("se:webDriverVersion", "120.0.6099.71")
    # chrome_options.add_argument('--disable-infobars')
    # chrome_options.add_argument("--disable-blink-features")
    chrome_options.add_argument('--log-level=0')
    chrome_options.add_experimental_option('w3c', False)
    # chrome_options.add_experimental_option("mobileEmulation",
    #                                        {"deviceMetrics": {"width": 414, "height": 736, "pixelRatio": 3.0},
    #                                         "userAgent": "Mozilla/5.0 (Linux; U; Android 8.1.0; zh-cn; MI 8 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/9.2 Mobile Safari/537.36"})

    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    print("+++++++++++++++++++")
    driver = webdriver.Remote(command_executor='http://127.0.0.1:4444', options=chrome_options)
    print("+++++++++++++++++++")
    driver.maximize_window()
    driver.get("https://baidu.com")

    driver.find_element(By.CSS_SELECTOR, "#kw").send_keys("周杰伦")
    driver.find_element(By.CSS_SELECTOR, "#su").click()
    time.sleep(5)
    driver.save_screenshot('test.png')

    # action = webdriver.ActionChains(driver)
    # # elemt = driver.find_element_by_class_name('weather-data-list')
    # elemt = driver.find_element(By.CSS_SELECTOR, '.border-top .weather-data-list')
    #
    # action.scroll_by_amount(100, 100).perform()
    # time.sleep(3)
    # action.scroll_from_origin(ScrollOrigin.from_element(elemt), 300, 0).perform()

    driver.quit()


def run_local():
    chrome_service = Service(executable_path="/Users/jayzhen/tools/docker/chromedriver")
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("no-sandbox")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--incognito')
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument('--remote-debugging-port=9222')
    # chrome_options.set_capability("browserType", "chrome")
    chrome_options.set_capability("browserVersion", "119.0")
    chrome_options.set_capability("platformName", "mac")
    driver = webdriver.Chrome(options=chrome_options, service=chrome_service)
    driver.get("https://baidu.com")
    driver.quit()


# def spider_html():
#     from requests_html import HTMLSession
#     session = HTMLSession()
#
#     r = session.get('https://baike.baidu.com/kexue/d24363794004192780.htm', verify=False)
#     r.html.render()
#     # print(r.html.html)
#     # with open("a.html", "a+") as f:
#     #     f.write(r.html.html)
#     d = r.html.find("span.blue", first=False)
#     for i in d:
#         print(i.attrs["data-url"])


if __name__ == '__main__':
    """
    1. 使用官方提供的 docker/standalone-chrome 容器各个版本都不能使用远程方式调用起来浏览器（java\python）
    2. selenium4 的 python 本地方式打开可以进行测试
    3. selenium4 使用在 mac 上自己搭建的 server + webdriver + chrome 可以进行用例测试
    4. 对于 standalone-server 的启动参数 `--config config.toml` 来说，实验在容器的配置中添加 webdriver-executable 参数依然不起作用
    """

    run_remote()
