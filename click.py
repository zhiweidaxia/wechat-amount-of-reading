# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#encoding:utf-8

#
#laplacian边缘检测
#


import pyautogui
import pynput.keyboard as pk
import pynput.mouse as pm
import copy
class Click():
    def __init__(self) -> None:
        self.data = []
    def on_click(self,x, y, button, pressed):# 监听鼠标点击
        if pressed:
            self.data.append([x,y])
        if not pressed:
            return False
    def start(self):
        # 开始监听
        nums = 0
        while nums < 2:
            with pm.Listener(on_click=self.on_click) as listener:
                listener.join()
                #print(self.data)
                nums += 1
        return self.data
'''demo
a = Click().start()
print(a)
'''

"""
image = cv2.imread("H:\\img\\lena.jpg")
image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)#将图像转化为灰度图像
cv2.imshow("Original",image)
cv2.waitKey()

#拉普拉斯边缘检测
lap = cv2.Laplacian(image,cv2.CV_64F)#拉普拉斯边缘检测
lap = np.uint8(np.absolute(lap))##对lap去绝对值
cv2.imshow("Laplacian",lap)
cv2.waitKey()
"""