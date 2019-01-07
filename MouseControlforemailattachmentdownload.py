# -*- coding: utf-8 -*-
"""
This script( with the help of pyautogui package) work the Mouse click movement over the screen(size(1366, 768)). basically it is working on the open Outlook ( tab icon on 5th position from left to right). first it search the email with the subject line then download the attachment in document folder.

limitation:

unable to handle
a. "Find More on the server message" in outlook mail box.
b. scroll disappear from mail box. it is working but needs to comment fews of code line
c. "more" in outlook mailbox.

"""

import pyautogui
import time
 
time.sleep(2)
tt1 =pyautogui.moveTo(270, 750, duration = 1)  ### clicking on outlook
pyautogui.click(tt1)
time.sleep(5)
pyautogui.scroll(100)
tt11 =pyautogui.moveTo(140, 320, duration = 1) ### clicking on Daily report
pyautogui.click(tt11)  
tt2 =pyautogui.moveTo(270, 156, duration = 1) ### clicking on search space
pyautogui.click(tt2)
pyautogui.typewrite("subject:(xxx_Banccccccth_Wcccceb_Ret_Hoy_3)") 
time.sleep(5)
tt3 =pyautogui.moveTo(300, 255, duration = 1) ### clicking on 1st finding
pyautogui.click(tt3)
pyautogui.hotkey("ctrlleft", "a") 
##### Looping for downloading activities ########


count = 0
#yy = 255
while (count < 3):     
    count = count + 1
    rtr = count
    if rtr >= 2:
        yy = 320
        #tt3 =pyautogui.moveTo(300, 255, duration = 1) ### clicking on 1st finding
        tt3 =pyautogui.moveTo(300, yy, duration = 1) ### clicking on 1st finding
        pyautogui.click(tt3)
        time.sleep(2)
        pyautogui.rightClick(x=1000, y=300)
        tt33 =pyautogui.moveTo(x=1020, y=385, duration = 1)
        pyautogui.click(tt33)
        tt333 =pyautogui.moveTo(x=1211, y=595, duration = 1)
        name ="subject:"xxx_Banccccccth_Wcccceb_Ret_Hoy_3_"+ str(count) +".csv"
        print(name)
        pyautogui.typewrite(name) 
        tt333 =pyautogui.moveTo(x=1211, y=695, duration = 1)
        pyautogui.click(tt333)
        tt3333 =pyautogui.moveTo(x=628, y=695, duration = 1)
        pyautogui.click(tt333)
        #yy = yy + 61
        print(yy)
        print("count:",count,"_",name,"completed")
    else:
        #tt3 =pyautogui.moveTo(300, 255, duration = 1) ### clicking on 1st finding
        tt3 =pyautogui.moveTo(300, 255, duration = 1) ### clicking on 1st finding
        pyautogui.click(tt3)
        time.sleep(2)
        pyautogui.rightClick(x=1000, y=300)
        tt33 =pyautogui.moveTo(x=1020, y=385, duration = 1)
        pyautogui.click(tt33)
        tt333 =pyautogui.moveTo(x=1211, y=595, duration = 1)
        name ="xxx_Banccccccth_Wcccceb_Ret_Hoy_3_"+ str(count) +".csv"
        print(name)
        pyautogui.typewrite(name) 
        tt333 =pyautogui.moveTo(x=1211, y=695, duration = 1)
        pyautogui.click(tt333)
        tt3333 =pyautogui.moveTo(x=628, y=695, duration = 1) ## click for scroll down 
        pyautogui.click(tt333)
        #yy = yy + 61
        #print(yy)
        print("count:",count,"_",name,"completed")
