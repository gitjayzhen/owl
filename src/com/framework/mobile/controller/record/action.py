#!/usr/bin/env python
#coding:utf-8
__author__ = "liufan"

import subprocess
import os
import platform
import sys
import time

def Adb_Path():
    system = platform.system()
    if "ANDROID_HOME" in os.environ:
        if system == "Windows":
            command = os.path.join(os.environ["ANDROID_HOME"], "platform-tools", "adb.exe")
            return command
        else:
            command = os.path.join(os.environ["ANDROID_HOME"], "platform-tools", "adb")
            return command
    else:
        raise EnvironmentError(
            "Adb not found in $ANDROID_HOME path: %s." % os.environ["ANDROID_HOME"])

def Run_Cmd(cmd):
    popen = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    line = popen.stdout.read().strip('\r\n')
    popen.communicate()
    popen.terminate()
    return line

def Start_Activity(devices,component):
    try:
        start_activity_cmd = 'adb -s %s shell am start -n \"%s\"' %(devices,component)
        Run_Cmd(start_activity_cmd)
        return True
    except:
        print "Start_Activity Exception"
        return False

def Stop_Package(devices,package):
    try:
        stop_activity_cmd = 'adb -s %s shell am force-stop \"%s\"' %(devices,package)
        Run_Cmd(stop_activity_cmd)
        return True
    except:
        print "Stop_Activity Exception"
        return False    
    
def Get_PhoneInfo(devices):
    try:
        info_cmd='adb -s %s shell cat /system/build.prop' %devices
        popen = subprocess.Popen(info_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        brand,model,androidOS,sdk_version = None,None,None,None
        for i in xrange(100):
            line = popen.stdout.readline().strip('\r\n')
            if line.count('=')==1:
                n,v=line.split('=')
                if n =='ro.product.brand':
                    brand=v
                elif n =='ro.product.model':
                    model=v
                elif n =='ro.build.version.release':
                    androidOS=v
                elif n == 'ro.build.version.sdk':
                    sdk_version = v
            if line == '' and i != 0:break
        popen.communicate()
        popen.terminate()
        return brand,model,androidOS,sdk_version
    except:
        print "Phone_Info Exception"
        return False

def Get_Resolution(devices):
    try:
        resol_cmd='adb -s %s shell dumpsys window |findstr "cur="' %devices
        line = Run_Cmd(resol_cmd)
        cur = line.split("cur=")[1].split(" ")[0]
        app = line.split("app=")[1].split(" ")[0]
        Width = cur.split("x")[0]
        Hight = cur.split("x")[1]
        return Width,Hight
    except:
        print "Get_Resolution Exception"
        return False
    
def Get_DeviceId():
    try:
        device_cmd = 'adb devices'
        device_id = []
        popen = subprocess.Popen(device_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        for i in range(100):
            line = popen.stdout.readline().strip('\r\n')
            if "device" in line and "attached" not in line:
                device_id.append(line.split('\t')[0].strip())
            if line=='':break
        if device_id == None:
            return False
        else:
            return device_id
        popen.communicate()
        popen.terminate()
    except:
        print 'Get_Deviceid Exception'
        return False

def Get_DeviceId_one():
    device_cmd = 'adb get-serialno'
    popen = subprocess.Popen(device_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    return popen.stdout.read().strip()

def Get_PackageName(devices):
    try:
        packagename_cmd = 'adb -s %s shell dumpsys window w | findstr \/ | findstr name=' %devices
        line = Run_Cmd(packagename_cmd)
        p_and_a = line.split("name=")[1].split(")")[0]
        Cur_PackageName = p_and_a.split("/")[0]
        Cur_ActivityName = p_and_a.split("/")[1]
        return Cur_PackageName,Cur_ActivityName
    except:
        print 'Get_PackageName Exception'
        return False

def Get_Battery_Level(devices):
    try:
        get_battery_level_cmd = 'adb -s %s shell dumpsys battery | findstr level' %devices
        level = Run_Cmd(get_battery_level_cmd).split("level: ")[1]
        return level
    except:
        print 'Get_Battery_Level Exception'
        return False

def Get_Third_AppList(devices):
    try:
        get_third_applist_cmd = 'adb -s %s shell pm list packages -3' %devices
        popen = subprocess.Popen(get_third_applist_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        applist = []
        for i in xrange(100):
            line = popen.stdout.readline().strip('\r\n')
            if line == '':break
            applist.append(line.split("package:")[1])
        popen.communicate()
        popen.terminate()
        return applist
    except:
        print 'Get_Third_AppList Exception'
        return False
    
def Get_Start_TotalTime(devices,component):
    try:
        get_start_totaltime_cmd = 'adb shell am start -W %s |findstr TotalTime' %component
        total_time = Run_Cmd(get_start_totaltime_cmd).strip().split("TotalTime: ")[1]
        return total_time
    except:
        print 'Get_Start_TotalTime Exception'
        return False

def Install_App(devices,apk):
    try:
        install_app_cmd = 'adb -s %s install -r %s' %(devices,apk)
        result = Run_Cmd(install_app_cmd)
        if 'Success' in result:
            return True
        else:
            return False
    except:
        print 'Install_App Exception'
        return False

def Is_install(devices,package):
    try:
        applist = Get_Third_AppList(devices)
        if package in applist:
            return True
        else:
            return False
    except:
        print 'Is_install Exception'
        return False

def Uninstall_App(devices,package):
    try:
        uninstall_app_cmd = 'adb -s %s uninstall %s' %(devices,package)
        result = Run_Cmd(uninstall_app_cmd)
        if 'Success' in result:
            return True
        else:
            return False
    except:
        print 'Uninstall_App Exception'
        return False

def Clear_App_Data(devices,package):
    try:
        clear_app_data_cmd = 'adb -s %s shell pm clear %s' %(devices,package)
        result = Run_Cmd(clear_app_data_cmd)
        return True
    except:
        print 'Clear_App_Data Exception'
        return False

def Get_Screencap(devices,picname,path=None):
    try:
        picname = picname.decode('utf-8').encode('gbk')
        screencap_cmd = 'adb -s %s shell /system/bin/screencap -p /sdcard/%s' %(devices,picname)
        if path:
            path = path.decode('utf-8').encode('gbk')
            get_screencap_cmd = 'adb -s %s pull /sdcard/%s %s/%s' %(devices,picname,path,picname)
        else:
            get_screencap_cmd = 'adb -s %s pull /sdcard/%s .' %(devices,picname)
        rm_cmd = 'adb -s %s shell rm /sdcard/%s' %(devices,picname)
        result1 = Run_Cmd(screencap_cmd)
        result2 = Run_Cmd(get_screencap_cmd)
        result3 = Run_Cmd(rm_cmd)
        return True
    except:
        print 'Get_Screencap Exception'
        return False
    
def Send_Key_Event(devices,keycode):
    try:
        send_key_event_cmd = 'adb -s %s shell input keyevent %s' %(devices,str(keycode))
        result = Run_Cmd(send_key_event_cmd)
        time.sleep(0.5)
        return True
    except:
        print 'Send_Key_Event Exception'    
        return False
    
##def Long_Press_Key(devices,keycode):
##    try:
##        send_key_event_cmd = 'adb -s %s shell input keyevent --longpress %s' %(devices,str(keycode))
##        result = Run_Cmd(send_key_event_cmd)
##        time.sleep(1)
##        return True
##    except:
##        print 'Send_Key_Event Exception'
##        return False

def Long_Press(devices,element=None,x1=None,y1=None):
    try:
        if element != None:
            x1 = element[0]
            y1 = element[1]
        x2 = int(x1)+1
        y2 = int(y1)+1
        click_cmd = 'adb -s %s shell input swipe %s %s %s %s %s' %(devices,str(x1),str(y1),str(x2),str(y2),str(2500))
        result = Run_Cmd(click_cmd)
        time.sleep(0.5)
        return True
    except:
        print 'Long_Press Exception'
        return False

def Click(devices,element=None,x=None,y=None):
    try:
        if element != None:
            x = element[0]
            y = element[1]
        click_cmd = 'adb -s %s shell input tap %s %s' %(devices,str(x),str(y))
        result = Run_Cmd(click_cmd)
        time.sleep(0.5)
        return True
    except:
        print 'Click Exception'
        return False

def Swipe(devices,ele1=None,ele2=None,x1=None,y1=None,x2=None,y2=None,duration=" ",width=None,high=None):
    try:
        if ele1 != None:
            x1 = ele1[0]
            y1 = ele1[1]
        if ele2 != None:
            x2 = ele2[0]
            y2 = ele2[1]
        if(0 < float(x1) < 1):
            x1 = float(x1) * int(width)
        if(0 < float(y1) < 1):
            y1 = float(y1)* int(high)
        if(0 < float(x2) < 1):
            x2 = float(x2) * int(width)
        if(0 < float(y2) < 1):
            y2 = float(y2) * int(high)
        swipe_cmd = 'adb -s %s shell input swipe %s %s %s %s %s' %(devices,str(x1),str(y1),str(x2),str(y2),str(duration))
        result = Run_Cmd(swipe_cmd)
        time.sleep(0.5)
        return True
    except:
        print 'Swipe Exception'
        return False

def Swipe_Up(devices,duration=" ",width=None,high=None):
    try:
        Swipe(devices,x1=0.5,y1=0.8,x2=0.5,y2=0.2,duration=duration,width=width,high=high)
        return True
    except:
        print 'Swipe_Up Exception'
        return False

def Swipe_Up_Webview(devices):
    try:
        swipe_cmd = 'adb -s %s shell input keyevent 20' %devices
        for i in range(10):
            Run_Cmd(swipe_cmd)
        return True
    except:
        print 'Swipe_Up_Webview Exception'
        return False
    
def Swipe_Down(devices,duration=" ",width=None,high=None):
    try:
        Swipe(devices,x1=0.5,y1=0.2,x2=0.5,y2=0.8,duration=duration,width=width,high=high)
        return True
    except:
        print 'Swipe_Down Exception'
        return False
    
def Swipe_Right(devices,duration=" ",width=None,high=None):
    try:
        Swipe(devices,x1=0.1,y1=0.5,x2=0.8,y2=0.5,duration=duration,width=width,high=high)
        return True
    except:
        print 'Swipe_Right Exception'
        return False
    
def Swipe_Left(devices,duration=" ",width=None,high=None):
    try:
        Swipe(devices,x1=0.9,y1=0.5,x2=0.2,y2=0.5,duration=duration,width=width,high=high)
        return True
    except:
        print 'Swipe_Left Exception'
        return False  
    
def utf8_gbk(text):
    return text.decode('utf-8').encode('gbk')
def check_ime(devices):
    check_ime_cmd = 'adb -s %s shell ime list -a' %devices
    result = Run_Cmd(check_ime_cmd)
    if "com.android.adbkeyboard/.AdbIME" in result:
        return True
    else:
        return False
def Input_Text(devices,text):
    try:
        if check_ime(devices):
            input_text_cmd = 'adb -s %s shell am broadcast -a ADB_INPUT_TEXT --es msg "%s"' %(devices,utf8_gbk(text))
            result = Run_Cmd(input_text_cmd)
        else:
            print "please use Install_Ime() before Input_Text()"
    except:
        print 'Input_Text Exception'
        return False

def Install_Ime(devices):
    try:
        if "com.android.adbkeyboard" in Get_Third_AppList(devices):
            return True
        else:
            Install_Ime_cmd = 'adb -s %s install %s' %(devices,"ADBKeyBoard.apk")
            result = Run_Cmd(Install_Ime_cmd)
            time.sleep(2)
            change_ime_cmd = 'adb -s %s shell ime set "com.android.adbkeyboard/.AdbIME"' %devices
            result = Run_Cmd(change_ime_cmd)
    except:
        print 'Install_Ime Exception'
        return False    

def Get_CrashByDropBox(devices,package):
    try:
        time_list = []
        get_crashbydropbox_time_cmd = "adb -s %s shell dumpsys dropbox | findstr data_app_crash" %devices
        popen = subprocess.Popen(get_crashbydropbox_time_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        for i in xrange(100):
            line = popen.stdout.readline().strip('\r\n')
            if line == '':break
            crash_time = line.split(" data_app_crash")[0]
            time_list.append(crash_time)
        popen.communicate()
        popen.terminate()
        if time_list:
            log_file = "CrashByDropBox.txt"
            f = open(log_file, "a")
            for time in time_list:
                get_crashbydropbox_cmd ='adb -s %s shell dumpsys dropbox --print %s' %(devices,time)
                cash_log = Run_Cmd(get_crashbydropbox_cmd)
                if package in cash_log:
                    f.write(cash_log)
            f.close()
        else:
            print "Not Found Exception"
            return True
    except:
        print 'Get_CrashByDropBox Exception'
        return False 

def Get_CpuMem(devices,package):
    get_cpumem_cmd = "adb -s %s shell top -n 1|findstr /i %s " %(devices,package)
    result = Run_Cmd(get_cpumem_cmd)
    if result:
        cpu = result.split()[2].strip('%')
        rss_mem = result.split()[6].strip('K')
        return cpu,int(rss_mem)/1024
    else:
        print "Not Found Package"
        return False

def Get_TotalMem(devices):
    try:
        get_totalmem_cmd = 'adb -s %s shell cat /proc/meminfo' %devices
        result = Run_Cmd(get_totalmem_cmd)
        result_split = result.split()
        memtotal = result_split[result_split.index('MemTotal:')+1]
        memfree = result_split[result_split.index('MemFree:')+1]
        return int(memtotal)/1024,int(memfree)/1024
    except:
        print 'Get_TotalMem Exception'
        return False
    
def Get_Traffic(devices,package):
    try:
        get_pid_cmd = 'adb -s %s shell ps|findstr /E %s' %(devices,package)
        pid_result = Run_Cmd(get_pid_cmd)
        pid = pid_result.split()[1]
        if pid:
            get_uid_cmd = 'adb -s %s shell cat /proc/%s/status' %(devices,pid)
            uid_result = Run_Cmd(get_uid_cmd)
            uid = uid_result.split()
            uid = uid[uid.index("Uid:")+1]
            if uid:
                get_traffic_cmd = 'adb -s %s shell cat /proc/net/xt_qtaguid/stats|findstr %s' %(devices,uid)
                popen = subprocess.Popen(get_traffic_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
                receive_data_arr = []
                send_data_arr = []
                for i in xrange(100):
                    line = popen.stdout.readline().strip('\r\n')
                    if line == '':break
                    receive_data = int(line.split()[5])
                    send_data = int(line.split()[7])
                    receive_data_arr.append(receive_data)
                    send_data_arr.append(send_data)
                popen.communicate()
                popen.terminate()
                receive = sum(receive_data_arr)/1024
                send = sum(send_data_arr)/1024
                return receive,send
            else:
                "Not Found Uid"
        else:
            print "Not Found Pid"
    except:
        print 'Get_Traffic Exception'
        return False
    
##if __name__ == '__main__':
##    print Get_TotalMem(Get_DeviceId()[0])
##    print Get_Traffic(Get_DeviceId()[0],"com.sogou.activity.src")
##    print Get_CpuMem(Get_DeviceId()[0],"com.sogou.activity.src")
##    Get_CrashByDropBox(Get_DeviceId()[0],"com.sogou.activity.src")
##    print Get_Resolution(Get_DeviceId()[0])
##    Get_PhoneInfo(Get_DeviceId()[0])
##    Start_Activity(Get_DeviceId()[0],"com.sogou.activity.src/com.sogou.search.entry.EntryActivity")
##    Stop_Package(Get_DeviceId()[0],"com.sogou.activity.src")
##    Get_Battery_Level(Get_DeviceId()[0])
##    Get_Third_AppList(Get_DeviceId()[0])
##    Get_Start_TotalTime(Get_DeviceId(),"com.sogou.activity.src/com.sogou.search.entry.EntryActivity")
##    Install_App(Get_DeviceId()[0],"SogouSearch_Debug.apk")
##    Uninstall_App(Get_DeviceId()[0],"com.sogou.activity.src")
##    Clear_App_Data(Get_DeviceId()[0],"com.sogou.activity.src")
##    Get_Screencap(Get_DeviceId()[0],"中国人.png","图片")
##    Send_Key_Event(Get_DeviceId()[0],"4")
##    Click(Get_DeviceId()[0],x=500,y=500)
##    width = 1080
##    high = 1980
##    Swipe(Get_DeviceId()[0],x1=500,y1=1500,x2=500,y2=500,duration=500)
##    Swipe(Get_DeviceId()[0],x1=0.5,y1=0.8,x2=0.5,y2=0.2,duration=500,width = 1080,high = 1980)
##    Swipe_Up(Get_DeviceId()[0],duration=500)
##    Swipe_Down(Get_DeviceId()[0],duration=500)
##    Swipe_Right(Get_DeviceId()[0],duration=500)
##    for i in range(5):
##        Swipe_Left(Get_DeviceId()[0],duration=500)
##    print Install_Ime(Get_DeviceId()[0])
##    Input_Text(Get_DeviceId()[0],"12вдにす中国人")
##    Get_Start_TotalTime(Get_DeviceId(),"com.sogou.activity.src/com.sogou.search.entry.EntryActivity")
##    Is_install(Get_DeviceId()[0],"com.sogou.activity.src")
##    Long_Press(Get_DeviceId()[0],x1=540,y1=1845)
