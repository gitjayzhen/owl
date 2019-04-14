# -*- coding: utf-8 -*- # 
import pythoncom 
import pyHook
import time
import win32api
from Tkinter import *
import os
import subprocess
import threading

VK_CODE = {
    'backspace':0x08,
    'tab':0x09,
    'clear':0x0C,
    'enter':0x0D,
    'shift':0x10,
    'ctrl':0x11,
    'alt':0x12,
    'pause':0x13,
    'caps_lock':0x14,
    'esc':0x1B,
    'spacebar':0x20,
    'page_up':0x21,
    'page_down':0x22,
    'end':0x23,
    'home':0x24,
    'left_arrow':0x25,
    'up_arrow':0x26,
    'right_arrow':0x27,
    'down_arrow':0x28,
    'select':0x29,
    'print':0x2A,
    'execute':0x2B,
    'print_screen':0x2C,
    'ins':0x2D,
    'del':0x2E,
    'help':0x2F,
    '0':0x30,
    '1':0x31,
    '2':0x32,
    '3':0x33,
    '4':0x34,
    '5':0x35,
    '6':0x36,
    '7':0x37,
    '8':0x38,
    '9':0x39,
    'a':0x41,
    'b':0x42,
    'c':0x43,
    'd':0x44,
    'e':0x45,
    'f':0x46,
    'g':0x47,
    'h':0x48,
    'i':0x49,
    'j':0x4A,
    'k':0x4B,
    'l':0x4C,
    'm':0x4D,
    'n':0x4E,
    'o':0x4F,
    'p':0x50,
    'q':0x51,
    'r':0x52,
    's':0x53,
    't':0x54,
    'u':0x55,
    'v':0x56,
    'w':0x57,
    'x':0x58,
    'y':0x59,
    'z':0x5A,
    'numpad_0':0x60,
    'numpad_1':0x61,
    'numpad_2':0x62,
    'numpad_3':0x63,
    'numpad_4':0x64,
    'numpad_5':0x65,
    'numpad_6':0x66,
    'numpad_7':0x67,
    'numpad_8':0x68,
    'numpad_9':0x69,
    'multiply_key':0x6A,
    'add_key':0x6B,
    'separator_key':0x6C,
    'subtract_key':0x6D,
    'decimal_key':0x6E,
    'divide_key':0x6F,
    'F1':0x70,
    'F2':0x71,
    'F3':0x72,
    'F4':0x73,
    'F5':0x74,
    'F6':0x75,
    'F7':0x76,
    'F8':0x77,
    'F9':0x78,
    'F10':0x79,
    'F11':0x7A,
    'F12':0x7B,
    'F13':0x7C,
    'F14':0x7D,
    'F15':0x7E,
    'F16':0x7F,
    'F17':0x80,
    'F18':0x81,
    'F19':0x82,
    'F20':0x83,
    'F21':0x84,
    'F22':0x85,
    'F23':0x86,
    'F24':0x87,
    'num_lock':0x90,
    'scroll_lock':0x91,
    'left_shift':0xA0,
    'right_shift ':0xA1,
    'left_control':0xA2,
    'right_control':0xA3,
    'left_menu':0xA4,
    'right_menu':0xA5,
    'browser_back':0xA6,
    'browser_forward':0xA7,
    'browser_refresh':0xA8,
    'browser_stop':0xA9,
    'browser_search':0xAA,
    'browser_favorites':0xAB,
    'browser_start_and_home':0xAC,
    'volume_mute':0xAD,
    'volume_Down':0xAE,
    'volume_up':0xAF,
    'next_track':0xB0,
    'previous_track':0xB1,
    'stop_media':0xB2,
    'play/pause_media':0xB3,
    'start_mail':0xB4,
    'select_media':0xB5,
    'start_application_1':0xB6,
    'start_application_2':0xB7,
    'attn_key':0xF6,
    'crsel_key':0xF7,
    'exsel_key':0xF8,
    'play_key':0xFA,
    'zoom_key':0xFB,
    'clear_key':0xFE,
    '+':0xBB,
    ',':0xBC,
    '-':0xBD,
    '.':0xBE,
    '/':0xBF,
    '`':0xC0,
    ';':0xBA,
    '[':0xDB,
    '\\':0xDC,
    ']':0xDD,
    "'":0xDE,
    '`':0xC0}

VK_CODE_reverse = {value:key for key, value in VK_CODE.items()}

def onMouseEvent(event): 

    # 监听鼠标事件     
    event_name = event.MessageName        
    position = event.Position
    op_log_file.write(str(event_name)+'\t'+str(position)+'\n')

    # 返回 True 以便将事件传给其它处理程序     
    # 注意，这儿如果返回 False ，则鼠标事件将被全部拦截     
    # 也就是说你的鼠标看起来会僵在那儿，似乎失去响应了
    return True

def onKeyboardEvent(event):
    # 监听键盘事件     
    event_name = event.MessageName  
    key_id = event.KeyID
    if str(event.Key)=='F12':
        op_log_file.close()
        win32api.PostQuitMessage()
        makeSript()
        cmd = 'taskkill /F /IM %s' %str(self_pid)
        popen2 = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=0)
        popen2.wait()
        popen2.terminate()
    op_log_file.write(str(event_name)+'\t'+str(VK_CODE_reverse[key_id])+'\n')
    
    # 同鼠标事件监听函数的返回值
    return True 

def hook():
    # 创建一个“钩子”管理对象     
    hm = pyHook.HookManager()      
    # 监听所有键盘事件     
    hm.KeyDown = onKeyboardEvent     
    # 设置键盘“钩子”     
    hm.HookKeyboard()      
    # 监听所有鼠标事件     
    hm.MouseAll = onMouseEvent     
    # 设置鼠标“钩子”     
    hm.HookMouse()
    # 进入循环，如不手动关闭，程序将一直处于监听状态     
    pythoncom.PumpMessages()

def makeSript():
    f = open('op.txt','r')
    c = f.readlines()
    f.close()
    if os.path.exists("script.py"):
        popen = subprocess.Popen('del script.py', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=0)
        popen.wait()
        popen.terminate()
    script = open("script.py","a")
    script.write("import time\nfrom action_windows import *\n\n")
    for i in c[:-1]:
        key = i.split('\t')[0]
        value = i.split('\t')[1]
        if key == 'mouse move':
            script.write("time.sleep(0.03)\n")
            line = 'mouse_move%s' %value.strip()
            script.write(line+'\n')
        elif key == 'mouse left down':
            script.write("time.sleep(1)\n")
            line = "mouse_left_click%s" %value.strip()
            script.write(line+'\n')
        elif key == 'key down':
            script.write("time.sleep(0.5)\n")
            line = 'key_input("%s")' %value.strip()
            script.write(line+'\n')
        elif key == 'mouse right down':
            script.write("time.sleep(1)\n")
            line = "mouse_right_click%s" %value.strip()
            script.write(line+'\n')
    script.close()

def start_record():
    if os.path.exists("op.txt"):
        popen1 = subprocess.Popen('del op.txt', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=0)
        popen1.wait()
        popen1.terminate()
    global op_log_file
    op_log_file = open("op.txt","a")
    btn_start['text'] = "recording"
    btn_start['bg'] = '#BEBEBE'
    root.update_idletasks()
    global self_pid
    self_pid = os.getpid()
    hook()
##    a = Process(target=hook)
##    a = threading.Thread(target=hook)
##    a.start()
##    global hook_pid
##    hook_pid = a.pid
##    a.join()


if __name__ == "__main__":     
    root=Tk()
    root.title('record')
    root.maxsize(250,50)
    root.minsize(250,50)
    root.geometry('+600+350')
    frame_main=LabelFrame(height=100,width=500,bg='#C4E1FF',bd=0)
    btn_start=Button (frame_main,text='start record',height=1,width=12,bg='#1AFD9C',command=start_record)
    lab_stop=Label(frame_main,text=u'按F12键停止录制',bg='#C4E1FF',width=13,height=1,anchor="center",bd=1)
    frame_main.grid(row = 0, column = 0,sticky = "wesn")
    btn_start.grid(row = 0, column = 0,sticky = "e",pady=10,padx=15)
    lab_stop.grid(row = 0, column = 1,sticky = "e",pady=10,padx=15)
    root.mainloop()
    
