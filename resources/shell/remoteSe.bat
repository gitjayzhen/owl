@echo off

chcp 65001

:: '节点启动服务，并连接上注册中心，配置上被访问的参数' 
:: rem "-role node -hub http://10.134.101.182:4444/grid/register"
java -jar selenium-server-standalone-2.53.1.jar   -browser "browserName=chrome,maxinstance=5,platform=WINDOWS" -Dwebdriver.chrome.driver="..\\driver\\exe\\67chrome2.40\\chromedriver.exe" -log node.log

pause