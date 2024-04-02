Docker 容器 (linux) 中运行 Selenium/Chrome, 然后将 mm 的两个目录 copy 到容器里
- ./Extensions/nkbihfbeogaeaoehlefnkodbefgpgknn
- ./Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn


基于 standalone-chrome 进行实验

安装 pip 
sudo apt update
sudo apt install python3-pip
按转 vim
sudo apt install -y vim


docker run --rm -p 4444:4444 -p 7900:7900 --name chrome --shm-size="2gb" --privileged=true --platform linux/amd64 selenium/standalone-chrome:120.0-chromedriver-120.0-grid-4.16.1-20231212

```text
/Users/jayzhen/tools/miniconda/envs/owl/bin/python /Users/jayzhen/Library/CloudStorage/jtest/test-ui/test_selenium.py 
+++++++++++++++++++
Traceback (most recent call last):
  File "/Users/jayzhen/Library/CloudStorage/jtest/test-ui/test_selenium.py", line 135, in <module>
    run_remote()
  File "/Users/jayzhen/Library/CloudStorage/jtest/test-ui/test_selenium.py", line 75, in run_remote
    driver = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub', options=chrome_options)
  File "/Users/jayzhen/tools/miniconda/envs/owl/lib/python3.8/site-packages/selenium/webdriver/remote/webdriver.py", line 205, in __init__
    self.start_session(capabilities)
  File "/Users/jayzhen/tools/miniconda/envs/owl/lib/python3.8/site-packages/selenium/webdriver/remote/webdriver.py", line 289, in start_session
    response = self.execute(Command.NEW_SESSION, caps)["value"]
  File "/Users/jayzhen/tools/miniconda/envs/owl/lib/python3.8/site-packages/selenium/webdriver/remote/webdriver.py", line 344, in execute
    self.error_handler.check_response(response)
  File "/Users/jayzhen/tools/miniconda/envs/owl/lib/python3.8/site-packages/selenium/webdriver/remote/errorhandler.py", line 229, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.SessionNotCreatedException: Message: Could not start a new session. Error while creating session with the driver service. Stopping driver service: Could not start a new session. Response code 500. Message: session not created: Chrome failed to start: exited normally.
  (chrome not reachable)
  (The process started from chrome location /usr/bin/google-chrome is no longer running, so ChromeDriver is assuming that Chrome has crashed.) 
Host info: host: '7232550fda21', ip: '172.17.0.2'
Build info: version: '4.16.1', revision: '9b4c83354e'
System info: os.name: 'Linux', os.arch: 'amd64', os.version: '5.15.49-linuxkit', java.version: '11.0.21'
Driver info: driver.version: unknown
Build info: version: '4.16.1', revision: '9b4c83354e'
System info: os.name: 'Linux', os.arch: 'amd64', os.version: '5.15.49-linuxkit', java.version: '11.0.21'
Driver info: driver.version: unknown
Stacktrace:
    at org.openqa.selenium.grid.node.config.DriverServiceSessionFactory.apply (DriverServiceSessionFactory.java:225)
    at org.openqa.selenium.grid.node.config.DriverServiceSessionFactory.apply (DriverServiceSessionFactory.java:72)
    at org.openqa.selenium.grid.node.local.SessionSlot.apply (SessionSlot.java:147)
    at org.openqa.selenium.grid.node.local.LocalNode.newSession (LocalNode.java:464)
    at org.openqa.selenium.grid.distributor.local.LocalDistributor.startSession (LocalDistributor.java:645)
    at org.openqa.selenium.grid.distributor.local.LocalDistributor.newSession (LocalDistributor.java:564)
    at org.openqa.selenium.grid.distributor.local.LocalDistributor$NewSessionRunnable.handleNewSessionRequest (LocalDistributor.java:824)
    at org.openqa.selenium.grid.distributor.local.LocalDistributor$NewSessionRunnable.lambda$run$1 (LocalDistributor.java:784)
    at java.util.concurrent.ThreadPoolExecutor.runWorker (ThreadPoolExecutor.java:1128)
    at java.util.concurrent.ThreadPoolExecutor$Worker.run (ThreadPoolExecutor.java:628)
    at java.lang.Thread.run (Thread.java:829)

进程已结束,退出代码1

```

https://github.com/SeleniumHQ/docker-selenium/issues/1978


```text

/Users/jayzhen/tools/miniconda/envs/owl/bin/python /Users/jayzhen/Library/CloudStorage/jtest/test-ui/test_selenium.py 
+++++++++++++++++++
Traceback (most recent call last):
  File "/Users/jayzhen/Library/CloudStorage/jtest/test-ui/test_selenium.py", line 135, in <module>
    run_remote()
  File "/Users/jayzhen/Library/CloudStorage/jtest/test-ui/test_selenium.py", line 75, in run_remote
    driver = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub', options=chrome_options)
  File "/Users/jayzhen/tools/miniconda/envs/owl/lib/python3.8/site-packages/selenium/webdriver/remote/webdriver.py", line 205, in __init__
    self.start_session(capabilities)
  File "/Users/jayzhen/tools/miniconda/envs/owl/lib/python3.8/site-packages/selenium/webdriver/remote/webdriver.py", line 289, in start_session
    response = self.execute(Command.NEW_SESSION, caps)["value"]
  File "/Users/jayzhen/tools/miniconda/envs/owl/lib/python3.8/site-packages/selenium/webdriver/remote/webdriver.py", line 344, in execute
    self.error_handler.check_response(response)
  File "/Users/jayzhen/tools/miniconda/envs/owl/lib/python3.8/site-packages/selenium/webdriver/remote/errorhandler.py", line 229, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.SessionNotCreatedException: Message: Could not start a new session. Error while creating session with the driver service. Stopping driver service: Could not start a new session. Response code 500. Message: session not created: Chrome failed to start: exited normally.
  (session not created: DevToolsActivePort file doesn't exist)
  (The process started from chrome location /usr/bin/google-chrome is no longer running, so ChromeDriver is assuming that Chrome has crashed.) 
Host info: host: '1990d1d01b6f', ip: '172.17.0.2'
Build info: version: '4.16.1', revision: '9b4c83354e'
System info: os.name: 'Linux', os.arch: 'amd64', os.version: '5.15.49-linuxkit', java.version: '11.0.21'
Driver info: driver.version: unknown
Build info: version: '4.16.1', revision: '9b4c83354e'
System info: os.name: 'Linux', os.arch: 'amd64', os.version: '5.15.49-linuxkit', java.version: '11.0.21'
Driver info: driver.version: unknown
Stacktrace:
    at org.openqa.selenium.grid.node.config.DriverServiceSessionFactory.apply (DriverServiceSessionFactory.java:225)
    at org.openqa.selenium.grid.node.config.DriverServiceSessionFactory.apply (DriverServiceSessionFactory.java:72)
    at org.openqa.selenium.grid.node.local.SessionSlot.apply (SessionSlot.java:147)
    at org.openqa.selenium.grid.node.local.LocalNode.newSession (LocalNode.java:464)
    at org.openqa.selenium.grid.distributor.local.LocalDistributor.startSession (LocalDistributor.java:645)
    at org.openqa.selenium.grid.distributor.local.LocalDistributor.newSession (LocalDistributor.java:564)
    at org.openqa.selenium.grid.distributor.local.LocalDistributor$NewSessionRunnable.handleNewSessionRequest (LocalDistributor.java:824)
    at org.openqa.selenium.grid.distributor.local.LocalDistributor$NewSessionRunnable.lambda$run$1 (LocalDistributor.java:784)
    at java.util.concurrent.ThreadPoolExecutor.runWorker (ThreadPoolExecutor.java:1128)
    at java.util.concurrent.ThreadPoolExecutor$Worker.run (ThreadPoolExecutor.java:628)
    at java.lang.Thread.run (Thread.java:829)

进程已结束,退出代码1

```