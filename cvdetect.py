import numpy as np
import cv2
class detectpic():
    def __init__(self,path):
        self.path = path
    def locatepic(self,img):
        #查找255
        maps = np.where(img==255)[0]
        #筛选255数量，选取最大的
        indexs = np.unique(maps,return_counts=True)#第几行，数量
        num = 0
        for i in indexs[1]:
            if i>10:
                break
            num += 1
        return indexs[0][num]
    def start(self):
        image = cv2.imread(self.path)
        image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)#将图像转化为灰度图像
        lap = cv2.Laplacian(image,cv2.CV_64F)#拉普拉斯边缘检测
        lap = np.uint8(np.absolute(lap))##对lap去绝对值
        #进行二值化处理
        lap[lap>100]=255
        lap[lap<100]=0
        lap = lap[self.locatepic(lap):,:]
        #图片进行切割
        screen = [int(lap.shape[0]/2),int(lap.shape[1]/2)]
        return int(screen[0]+self.locatepic(lap[screen[0]:,:]))

#demo
#print(detectpic('cv_detect.png').start())