from re import S
from pip import main
import pyautogui
import cvdetect as cvs
import time
import pyperclip
class Screenshot():
    def __init__(self):
        self.data = []
    def screenshot(self,data = (0,0,0,0)):
        pyautogui.screenshot(region=data).save('cv_detect.png')#X,Y,W,H
    def start(self):
        data=pyautogui.locateOnScreen('locate1.png')
        screen_data = (data[0]-200,data[1]+50,400,600)
        self.screenshot(screen_data)
        datas = data[0],data[1]
        scrolls = -1*cvs.detectpic('cv_detect.png').start()
        #time.sleep(1)
        # 浏览页面X，y，边缘滚轮X，y，滚轮次数scrolls
        return [data[0],datas[1]+160],[datas[0]+300,datas[1]+160],scrolls
class secDetector():
    def __init__(self,clickpath = 'contextlocate0.png',closepath = 'contextlocate.png'):
        self.clickpath = clickpath
        self.closepath = closepath
    def start(self,path,nums):#contextlocate.png#contextlocate0.png
        clickdata = pyautogui.locateOnScreen(self.clickpath)
        pyautogui.click(clickdata[0]+clickdata[2],clickdata[1]+80,clicks=1,interval=0,button='left')
        time.sleep(2)
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.hotkey('ctrl', 'c')
        print("copy")
        time.sleep(2)
        data = pyperclip.paste()

        with open('./%s/%s.txt'%(path,nums),'w',encoding ='utf-8') as f:
            f.write(data)
        
        closedata=pyautogui.locateOnScreen(self.closepath)
        pyautogui.click(closedata[0]+closedata[2],closedata[1],clicks=1,interval=0,button='left')
        #pyautogui.click(closedata[0]+closedata[2],closedata[1],clicks=1,interval=0,button='left')
if __name__ == '__main__':
    firtdec = []
    edgescroll = []
    firtdec,edgescroll,scrolls = Screenshot().start()
    cout = 0
    while cout<100:
        pyautogui.click(firtdec[0],firtdec[1],duration=0.5)
        try:
            secDetector().start('11',cout)
        except:
            pyautogui.scroll(-30)
            continue
        pyautogui.click(edgescroll[0],edgescroll[1],duration=0.5)
        pyautogui.scroll(scrolls)
        cout = cout + 1
        
#S = Screenshot().start()
#print(S)